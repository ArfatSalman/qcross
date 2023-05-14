import json
import os
import sqlite3 as sl
from functools import reduce
from os.path import join
from pathlib import Path
from random import uniform

import cirq
import numpy as np
import pandas as pd
from jsonpath_ng import parse

from qcross.morphq import MorphQAdaptor
from qcross.transpiler_cirq import CirqCircuit
from qcross.transpiler_pyquil import PyQuilCircuit
from qcross.utils import Log, convert_morphq_metadata
from qcross.utils import detect_divergence as _detect_divergence
from qcross.utils import fix_cx3, timed_execute_single_py_program
from qcross.quilc_wrapper import restart_quilc

morphq_adaptor = MorphQAdaptor()


def add_unitary_in_qiskit(py_content: str):
    py_content = py_content.replace(
        "# NAME: MEASUREMENT",
        """
# NAME: MEASUREMENT
# Execute the circuit and obtain the unitary matrix
from qiskit import Aer, transpile, execute
result = execute(qc.reverse_bits(), backend=Aer.get_backend('unitary_simulator')).result()
UNITARY = result.get_unitary(qc).data
""",
    )
    return py_content


class DB:
    def __init__(self, table_name: str) -> None:
        self.table_name = table_name
        self.con = self.get_database_connection(self.table_name)

    def get_database_connection(self, db_filename: str = "status.db"):
        """Get the database."""
        DB_PATH = os.path.join("qcross-data", db_filename)
        con = sl.connect(DB_PATH)
        return con

    def update_database(self, record):
        """Update the RERUN database with the following result."""
        df_single = pd.json_normalize([record])
        dict_is_col_list = (df_single.applymap(type) == list).all()
        for c in df_single.columns:
            if dict_is_col_list[c]:
                df_single[c] = df_single[c].astype("str")
        df_single.to_sql(self.table_name, self.con, if_exists="append")


def execute_with_log(source: str, label: str, add_unitary: bool = False):
    metadata = {
        "result": None,
        "time_taken": None,
        "exception": None,
    }
    try:
        Log.yellow(f"Executing {label}")
        res, unitary, time = timed_execute_single_py_program(source)
        metadata["result"] = res
        metadata["time_taken"] = f"{time / 10 ** 6} ms"
        if add_unitary:
            if unitary is None:
                raise ValueError("Unitary not calculated but required")
            metadata["unitary"] = unitary
        Log.green(f"Execution of {label} source successful")
    except Exception as error:
        Log.red(f"Execution of {label} failed with error: {str(error)}")
        metadata["exception"] = str(error).strip("'\"")

    return metadata


def detect_divergence(a, b):
    if isinstance(a, list) or isinstance(b, list):
        print("a", a)
        print("b", b)
        raise ValueError("results should be a dict")
    return _detect_divergence(a, b)


def write_content_to_file(data: dict, path: str):
    Path(path).mkdir(parents=True, exist_ok=True)
    for d in data:
        with open(os.path.join(path, d + ".py"), "w", encoding="utf-8") as f:
            f.write(data[d])


def write_metadata(metadata: dict, path: str):
    Path(path).mkdir(parents=True, exist_ok=True)
    with open(os.path.join(path, "exec-metadata.json"), "w", encoding="utf-8") as f:
        f.write(json.dumps(metadata, indent=4, sort_keys=True))


def replace_qasm_2_with_3(qiskit_src):
    qasm_2_str = "qc = QuantumCircuit.from_qasm_str(qc.qasm())"

    if qasm_2_str in qiskit_src:
        qasm3_roundtrip_str = """
from qiskit.qasm3 import loads, dumps
qc = loads(dumps(qc))
"""
        return qiskit_src.replace(qasm_2_str, qasm3_roundtrip_str)

    multi_qasm_1 = "qc_1 = QuantumCircuit.from_qasm_str(qc_1.qasm())"
    multi_qasm_2 = "qc_2 = QuantumCircuit.from_qasm_str(qc_2.qasm())"
    if multi_qasm_1 in qiskit_src and multi_qasm_1 in qiskit_src:
        qasm3_roundtrip_str = """
from qiskit.qasm3 import loads, dumps
qc_1 = loads(dumps(qc_1))
"""
        qc_2 = """
qc_2 = loads(dumps(qc_2))
"""
        return qiskit_src.replace(multi_qasm_1, qasm3_roundtrip_str).replace(
            multi_qasm_2, qc_2
        )

    raise ValueError("MR relation has QASM rountrip but no QASM calls found")


def replace_qasm_2_with_qpy(qiskit_src):
    qasm_2_str = "qc = QuantumCircuit.from_qasm_str(qc.qasm())"

    fn = """

def circuit_state_vector_are_equal(qc1, qc2):
    from qiskit.quantum_info import Statevector
    return Statevector.from_instruction(qc1).equiv(Statevector.from_instruction(qc2))

def qpy_roundtrip(qiskit_qc):
    from qiskit import qpy
    import os
    import uuid
    qc_id = uuid.uuid4().hex
    with open(f'{qc_id}.qpy', 'wb') as fd:
        qpy.dump(qiskit_qc, fd)

    with open(f'{qc_id}.qpy', 'rb') as fd:
        new_qc = qpy.load(fd)[0]

    os.remove(f'{qc_id}.qpy')
    return new_qc
"""

    if qasm_2_str in qiskit_src:
        qpy_roundtrip_str = f"""
{fn}
old_qc = qc
qc = qpy_roundtrip(qc)

assert old_qc == qc
# assert circuit_state_vector_are_equal(
#     old_qc.remove_final_measurements(inplace=False),
#     qc.remove_final_measurements(inplace=False)
# )
"""
        return qiskit_src.replace(qasm_2_str, qpy_roundtrip_str)

    multi_qasm_1 = "qc_1 = QuantumCircuit.from_qasm_str(qc_1.qasm())"
    multi_qasm_2 = "qc_2 = QuantumCircuit.from_qasm_str(qc_2.qasm())"
    if multi_qasm_1 in qiskit_src and multi_qasm_1 in qiskit_src:
        qpy_roundtrip_str = f"""
{fn}
old_qc_1 = qc_1

qc_1 = qpy_roundtrip(qc_1)

assert old_qc_1 == qc_1
# assert circuit_state_vector_are_equal(
#     old_qc_1.remove_final_measurements(inplace=False),
#     qc_1.remove_final_measurements(inplace=False)
# )
"""
        qc_2 = """
old_qc_2 = qc_2
qc_2 = qpy_roundtrip(qc_2)

assert old_qc_2 == qc_2
# assert circuit_state_vector_are_equal(
#     old_qc_2.remove_final_measurements(inplace=False),
#     qc_2.remove_final_measurements(inplace=False)
# )
"""
        return qiskit_src.replace(multi_qasm_1, qpy_roundtrip_str).replace(
            multi_qasm_2, qc_2
        )

    raise ValueError("MR relation has QASM rountrip but no QASM calls found")


def qasm3_roundtrip(source: str):
    Log.yellow("Found a QASM2 roundtirp. Transforming to QASM3 Roundtrip")
    new_source = replace_qasm_2_with_3(source)
    metadata = execute_with_log(new_source, "QASM3 Roundtrip")
    return new_source, metadata


def qpy_roundtrip(source: str, metadata: dict):
    if "ToQasmAndBack" not in metadata["followup"]["metamorphic_transformations"]:
        return
    Log.yellow("Found a QASM2 roundtirp. Transforming to QPY Roundtrip")
    new_source = replace_qasm_2_with_qpy(source)
    metadata = execute_with_log(new_source, "QPY Roundtrip")
    return new_source, metadata


def recontruct_partitioned_result_if_needed(
    followup_source_metadata: dict, source_metadata: dict
):
    jsonpath_expr = parse("$..mapping")

    full_mapping = (
        len(jsonpath_expr.find(source_metadata)) == 1
        and "RunIndependentPartitions"
        in source_metadata["followup"]["metamorphic_transformations"]
        and "ChangeQubitOrder"
        not in source_metadata["followup"]["metamorphic_transformations"]
    )

    if full_mapping and followup_source_metadata["result"] is not None:
        followup_source_metadata["result_original"] = followup_source_metadata["result"]
        followup_source_metadata[
            "result"
        ] = morphq_adaptor.reconstruct_partitioned_results(
            followup_source_metadata["result"],
            jsonpath_expr.find(source_metadata)[0].value,
        )


def reconstruct_change_qubit_order_results_if_needed(
    followup_source_metadata: dict, source_metadata: dict
):
    jsonpath_expr = parse("$..mapping")

    full_mapping = (
        len(jsonpath_expr.find(source_metadata)) == 1
        and "ChangeQubitOrder"
        in source_metadata["followup"]["metamorphic_transformations"]
        and "RunIndependentPartitions"
        not in source_metadata["followup"]["metamorphic_transformations"]
    )

    if full_mapping and followup_source_metadata["result"] is not None:
        followup_source_metadata["result_original"] = followup_source_metadata["result"]
        followup_source_metadata[
            "result"
        ] = morphq_adaptor.reconstruct_changed_qubit_order_result(
            followup_source_metadata["result"],
            eval(jsonpath_expr.find(source_metadata)[0].value),
        )


def qiskit_related_execs(
    qiskit_source: str, followup_source: str, source_metadata: dict
):
    qiskit_metadata = {}

    # execute qiskit source and followup source
    # Why?: testing to see how many MorphQ bugs were fixed by Qiskit
    # and how many bugs were introduced in a newer version of Qiskit
    qiskit_source_metadata = execute_with_log(qiskit_source, "Qiskit source")
    qiskit_metadata["qiskit_source"] = qiskit_source_metadata

    # Qiskit followup
    followup_source_metadata = execute_with_log(followup_source, "Qiskit Followup")

    recontruct_partitioned_result_if_needed(followup_source_metadata, source_metadata)
    reconstruct_change_qubit_order_results_if_needed(
        followup_source_metadata, source_metadata
    )
    followup_result = followup_source_metadata["result"]

    qiskit_metadata["qiskit_followup"] = followup_source_metadata

    qiskit_metadata["source_followup_divergence"] = None
    if (
        qiskit_source_metadata["result"] is not None
        and followup_source_metadata["result"] is not None
    ):
        qiskit_metadata["source_followup_divergence"] = detect_divergence(
            qiskit_source_metadata["result"], followup_result
        )

    sources = {}
    if "ToQasmAndBack" in source_metadata["followup"]["metamorphic_transformations"]:
        # QASM3 roundtrip
        qasm3_source, qasm3_metadata = qasm3_roundtrip(followup_source)
        recontruct_partitioned_result_if_needed(qasm3_metadata, source_metadata)
        reconstruct_change_qubit_order_results_if_needed(
            qasm3_metadata, source_metadata
        )
        sources["qasm3_source"] = qasm3_source
        qiskit_metadata["qasm3_roundtrip"] = qasm3_metadata

        qiskit_metadata["qasm3_source_divergence"] = None

        if (
            qasm3_metadata["result"] is not None
            and qiskit_source_metadata["result"] is not None
        ):
            qiskit_metadata["qasm3_source_divergence"] = detect_divergence(
                qasm3_metadata["result"], qiskit_source_metadata["result"]
            )

        qiskit_metadata["qasm3_followup_divergence"] = None
        if qasm3_metadata["result"] is not None and followup_result is not None:
            qiskit_metadata["qasm3_followup_divergence"] = detect_divergence(
                qasm3_metadata["result"], followup_result
            )

        # QPY roundtrip
        qpy_source, qpy_metadata = qpy_roundtrip(followup_source, source_metadata)
        recontruct_partitioned_result_if_needed(qpy_metadata, source_metadata)
        reconstruct_change_qubit_order_results_if_needed(qpy_metadata, source_metadata)
        sources["qpy_source"] = qpy_source
        qiskit_metadata["qpy_roundtrip"] = qpy_metadata

        qiskit_metadata["qpy_source_divergence"] = None
        if (
            qpy_metadata["result"] is not None
            and qiskit_source_metadata["result"] is not None
        ):
            qiskit_metadata["qpy_source_divergence"] = detect_divergence(
                qpy_metadata["result"], qiskit_source_metadata["result"]
            )

        qiskit_metadata["qpy_followup_divergence"] = None
        if qpy_metadata["result"] is not None and followup_result is not None:
            qiskit_metadata["qpy_followup_divergence"] = detect_divergence(
                qpy_metadata["result"], followup_result
            )

    return {
        "qiskit_metadata": qiskit_metadata,
        "sources": {
            "qiskit_source": qiskit_source,
            "followup_source": followup_source,
            **sources,
        },
    }


def cirq_related_execs(qiskit_source: str, followup_source: str, source_metadata: dict):
    metadata = {}

    _, source_cirq = CirqCircuit(qiskit_source).get_follow_up({})

    exec_metadata = execute_with_log(source_cirq, "Cirq source")
    metadata["cirq_source"] = exec_metadata

    config = convert_morphq_metadata(source_metadata)
    metadata["config"] = config

    _, followup_cirq = CirqCircuit(followup_source).get_follow_up(config)
    followup_metadata = execute_with_log(followup_cirq, "Cirq followup")
    metadata["cirq_followup"] = followup_metadata

    jsonpath_expr = parse("$..mapping")

    full_mapping = (
        len(jsonpath_expr.find(source_metadata)) == 1
        and "RunIndependentPartitions"
        in source_metadata["followup"]["metamorphic_transformations"]
        and "ChangeQubitOrder"
        not in source_metadata["followup"]["metamorphic_transformations"]
    )
    followup_result = followup_metadata["result"]
    if full_mapping and followup_metadata["result"] is not None:
        followup_result = morphq_adaptor.reconstruct_partitioned_results(
            followup_metadata["result"], jsonpath_expr.find(source_metadata)[0].value
        )

    metadata["source_followup_divergence"] = None
    if exec_metadata["result"] is not None and followup_result is not None:
        metadata["source_followup_divergence"] = detect_divergence(
            exec_metadata["result"], followup_result
        )

    sources = {}
    if "qasm_roundtrip" in config:
        config.update({"cirq_qasm_qiskit": True})
        del config["qasm_roundtrip"]

        _, followup_cirq_qasm_qiskit = CirqCircuit(followup_source).get_follow_up(
            config
        )
        sources["cirq_qasm_qiskit"] = followup_cirq_qasm_qiskit
        cirq_qasm_qiskit_metadata = execute_with_log(
            followup_cirq_qasm_qiskit, "Cirq QASM Qiskit Roundtrip"
        )
        metadata["cirq_qasm_qiskit"] = cirq_qasm_qiskit_metadata

        metadata["source_cirq_qasm_qiskit_divergence"] = None
        if (
            exec_metadata["result"] is not None
            and cirq_qasm_qiskit_metadata["result"] is not None
        ):
            metadata["source_cirq_qasm_qiskit_divergence"] = detect_divergence(
                exec_metadata["result"], cirq_qasm_qiskit_metadata["result"]
            )

        metadata["followup_cirq_qasm_qiskit_divergence"] = None
        if (
            followup_result is not None
            and cirq_qasm_qiskit_metadata["result"] is not None
        ):
            metadata["followup_cirq_qasm_qiskit_divergence"] = detect_divergence(
                followup_result, cirq_qasm_qiskit_metadata["result"]
            )

    return {
        "cirq_metadata": metadata,
        "sources": {
            "cirq_source": source_cirq,
            "cirq_followup": followup_cirq,
            **sources,
        },
    }


def pyquil_related_execs(
    qiskit_source: str, followup_source: str, source_metadata: dict
):
    metadata = {}
    _, source_pyquil = PyQuilCircuit(qiskit_source).get_follow_up({})

    exec_metadata = execute_with_log(source_pyquil, "PyQuil source")
    metadata["pyquil_source"] = exec_metadata

    if exec_metadata["exception"] is not None and (
        "COMPILER-DOES-NOT-APPLY" in exec_metadata["exception"]
        or "timed out" in exec_metadata["exception"]
        or "Timeout" in exec_metadata["exception"]
    ):
        print("Restarting quilc")
        restart_quilc()

    config = convert_morphq_metadata(source_metadata)
    metadata["config"] = config

    _, followup_pyquil = PyQuilCircuit(followup_source).get_follow_up(config)
    followup_metadata = execute_with_log(followup_pyquil, "PyQuil followup")
    if followup_metadata["exception"] is not None and (
        "COMPILER-DOES-NOT-APPLY" in followup_metadata["exception"]
        or "timed out" in followup_metadata["exception"]
        or "Timeout" in followup_metadata["exception"]
    ):
        print("Restarting quilc")
        restart_quilc()

    jsonpath_expr = parse("$..mapping")

    full_mapping = (
        len(jsonpath_expr.find(source_metadata)) == 1
        and "RunIndependentPartitions"
        in source_metadata["followup"]["metamorphic_transformations"]
        and "ChangeQubitOrder"
        not in source_metadata["followup"]["metamorphic_transformations"]
    )

    followup_result = followup_metadata["result"]
    if full_mapping and followup_metadata["result"] is not None:
        followup_result = morphq_adaptor.reconstruct_partitioned_results(
            followup_metadata["result"], jsonpath_expr.find(source_metadata)[0].value
        )

    metadata["pyquil_followup"] = followup_metadata

    metadata["source_followup_divergence"] = None
    if exec_metadata["result"] is not None and followup_result is not None:
        metadata["source_followup_divergence"] = detect_divergence(
            exec_metadata["result"], followup_result
        )

    return {
        "pyquil_metadata": metadata,
        "sources": {
            "pyquil_source": source_pyquil,
            "pyquil_followup": followup_pyquil,
        },
    }


def unitary_related_checks(qiskit_followup: str, source_metadata: dict):
    metadata = {}

    instrumented_circuit = add_unitary_in_qiskit(qiskit_followup)

    qiskit_unitary_metadata = execute_with_log(
        instrumented_circuit, "Qiskit followup with unitary", add_unitary=True
    )

    config = convert_morphq_metadata(source_metadata)

    config.update({"add_unitary": True})
    _, followup_cirq = CirqCircuit(qiskit_followup).get_follow_up(config)

    cirq_unitary_metadata = execute_with_log(
        followup_cirq, "Cirq followup with unitary", add_unitary=True
    )

    _, followup_pyquil = PyQuilCircuit(qiskit_followup).get_follow_up(config)
    pyquil_unitary_metadata = execute_with_log(
        followup_pyquil, "PyQuil followup with unitary", add_unitary=True
    )

    if (
        qiskit_unitary_metadata["exception"] is None
        and cirq_unitary_metadata["exception"] is None
    ):
        if cirq.equal_up_to_global_phase(
            qiskit_unitary_metadata["unitary"], cirq_unitary_metadata["unitary"]
        ):
            Log.green('Unitary check: "Qiskit" and "Cirq" unitaries are equal')
            if pyquil_unitary_metadata[
                "exception"
            ] is None and cirq.equal_up_to_global_phase(
                cirq_unitary_metadata["unitary"], pyquil_unitary_metadata["unitary"]
            ):
                Log.green('Unitary check: "Cirq" and "PyQuil" unitaries are equal')
                metadata["unitary"] = True
            else:
                metadata["unitary"] = False
        else:
            Log.red('Unitary check: "Qiskit" and "Cirq" unitaries are not equal')

    for d in [qiskit_unitary_metadata, cirq_unitary_metadata, pyquil_unitary_metadata]:
        if "unitary" in d:
            del d["unitary"]

    metadata["qiskit_unitary"] = qiskit_unitary_metadata
    metadata["cirq_unitary"] = cirq_unitary_metadata
    metadata["pyquil_unitary"] = pyquil_unitary_metadata

    return {
        "unitary_metadata": metadata,
        "sources": {
            "qiskit_followup": instrumented_circuit,
            "cirq_followup": followup_cirq,
            "pyquil_followup": followup_pyquil,
        },
    }


def main(
    prog_id: str,
    qiskit_source: str,
    followup_source: str,
    source_metadata: dict,
    folder="qcross-data/completed-execs/",
):
    saved_location_folder = folder
    metadata = {
        "prog_id": prog_id,
    }

    print("Listed Transformations: ")
    print(source_metadata["followup"]["metamorphic_transformations"])

    if (
        "QdiffG7CCNOTDecomposition"
        in source_metadata["followup"]["metamorphic_transformations"]
    ):
        print("Skipping QdiffG7CCNOTDecomposition")
        return

    execute_qiskit = True
    execute_cirq = True
    execute_pyquil = True
    execute_unitary = uniform(0, 1) < 0.1

    if execute_qiskit:
        qiskit_metadata = qiskit_related_execs(
            qiskit_source, followup_source, source_metadata
        )
        write_content_to_file(
            qiskit_metadata["sources"],
            os.path.join(saved_location_folder, prog_id, "qiskit"),
        )

        metadata["qiskit"] = qiskit_metadata["qiskit_metadata"]

    if execute_unitary:  # 10% chance of executing unitary checks
        unitary_metadata = unitary_related_checks(followup_source, source_metadata)
        write_content_to_file(
            unitary_metadata["sources"],
            os.path.join(saved_location_folder, prog_id, "unitary"),
        )

        metadata["unitary"] = unitary_metadata["unitary_metadata"]

    if execute_cirq:
        cirq_metadata = cirq_related_execs(
            qiskit_source, followup_source, source_metadata
        )
        write_content_to_file(
            cirq_metadata["sources"],
            os.path.join(saved_location_folder, prog_id, "cirq"),
        )
        metadata["cirq"] = cirq_metadata["cirq_metadata"]

    if execute_pyquil:
        pyquil_metadata = pyquil_related_execs(
            qiskit_source, followup_source, source_metadata
        )

        write_content_to_file(
            pyquil_metadata["sources"],
            os.path.join(saved_location_folder, prog_id, "pyquil"),
        )

        metadata["pyquil"] = pyquil_metadata["pyquil_metadata"]

    write_metadata(
        metadata,
        os.path.join(saved_location_folder, prog_id),
    )


def get_paths(folder, file):
    src = join(folder, "source", file)
    followup = join(folder, "followup", file)
    prog_id = file.split(".")[0]
    metadata = join(folder, "metadata", prog_id + ".json")

    return src, followup, metadata


def get_all_content(folder, prog_id):
    src, followup, metadata = get_paths(folder, prog_id)

    try:
        with open(src, "r", encoding="utf-8") as f:
            qiskit_source = f.read()
    except FileNotFoundError:
        Log.red(f"For {prog_id}, the source file was not found")
        return None

    try:
        with open(followup, "r", encoding="utf-8") as f:
            followup_source = f.read()
    except FileNotFoundError:
        Log.red(f"For {prog_id}, the followup file was not found")
        return None

    try:
        with open(metadata, "r", encoding="utf-8") as f:
            source_metadata = json.load(f)
    except FileNotFoundError:
        Log.red(f"For {prog_id}, the metadata file was not found")
        return None

    return qiskit_source, followup_source, source_metadata


def should_execute(prog_id: str) -> bool:
    manual_exclusions = [
        "e3a4d2dff93e4dc39349b2d17471723c",
        "aa8c369525a64cbf81de991e58101ee4",
        "ae3bbf48e2c44b47b7dacd5ce3f1ea86",
        "b8c0da5d20a34b3c85b7886a2fe6426d",
        "e72010e17db0408fa9c544b869c64ac2",
        "3f539042cc0b43fe9813f053c440d658",
        "f438624aef78412285662ea8b54da3fe",
        "12df5a179bec4776be5a41c2f0b84f2f",
        "d0e2789f149c4a2fb4d4c6655c676598",
        "ac4ef7f04f6947498b9cd84c8b725b81",
        "2a6ddb3ddeb349a88d8642bbb512da92",
        "d8c615601f6f4f3694554f89f2535f54",
        "222939fd09a248069aac58fdd982668d",
        "9841c515aecf4748b9dc9d8b34cd261e",
        "69bb6a74058e4c579bc8fa8e4ad97b45",
        "a9a94ab233134ec38bff6d8ad31018a1",
        "c4d3359157af43aaa9d51180ce095ef0",
        "735021e569654163a70ff97b7cc19904",
        "7a6abd08d5e644229ba551ef5ae8fbdd",
        "45e4ba1b69634b3295678950e1b0f5bb",
        "e4485894b2514ba28fa5a01b62fd7c36",
    ]
    if prog_id in manual_exclusions or prog_id in os.listdir(
        join("qcross-data", "completed-execs")
    ):
        # Log.yellow(f"Skipping {prog_id} since it is already executed")
        return False
    return True


def use_morphq_data(folder):
    Path(join("qcross-data", "completed-execs")).mkdir(parents=True, exist_ok=True)
    i = 0
    for file in os.listdir(join(folder, "source")):
        prog_id = file.split(".")[0]

        if not should_execute(prog_id):
            continue

        if i == 200:
            break

        Log.blue(f"{i} Processing '{os.path.join(folder, 'source', file)}' ...")
        result = get_all_content(folder, file)
        if result is None:
            continue

        qiskit_source, followup_source, source_metadata = result

        main(prog_id, fix_cx3(qiskit_source), fix_cx3(followup_source), source_metadata)
        i += 1


def run_new_programs(count: int = 20):
    saved_location_folder = join("qcross-data", "new-completed-execs")
    Path(saved_location_folder).mkdir(parents=True, exist_ok=True)
    for _ in range(count):
        result = morphq_adaptor.produce_qiskit_program_couple()
        print(f'Processing {result["program_id"]}')
        main(
            result["program_id"],
            result["qiskit_source_code"],
            result["qiskit_followup_code"],
            result["all_metadata"],
            saved_location_folder,
        )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        prog="QCross",
        description="QCross is a tool to cross-check the correctness of quantum stacks",
    )
    parser.add_argument(
        "--run-new-programs",
        default=False,
        dest="new",
        action="store_true",
        help="Use this flag to run the new programs",
    )
    parser.add_argument(
        "--existing-programs-src",
        default="data/qmt_v53/programs",
        dest="src",
        action="store",
        help="Use this flag to run the new programs",
    )
    args = parser.parse_args()

    restart_quilc()
    if args.new:
        run_new_programs(100)
    else:
        use_morphq_data(args.src)
