import os
import json
import sys
import uuid

from os.path import join
from pathlib import Path

import sqlite3 as sl
import pandas as pd

from qcross.transpiler_pyquil import PyQuilCircuit
from qcross.transpiler_cirq import CirqCircuit
from qcross.utils import (
    timed_execute_single_py_program,
    Log,
    detect_divergence,
    convert_morphq_metadata,
    fix_cx3,
)


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


def execute_with_log(source: str, label: str):
    metadata = {
        "result": None,
        "time_taken": None,
        "exception": None,
    }
    try:
        Log.yellow(f"Executing {label} source")
        res, _unitary, time = timed_execute_single_py_program(source)
        metadata["result"] = res
        metadata["time_taken"] = f"{time / 10 ** 6} ms"
        Log.green(f"Execution of {label} source successful")
    except Exception as error:
        Log.red(f"Execution of {label} failed with error: {str(error)}")
        metadata["exception"] = str(error).strip("'\"")

    return metadata


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

assert circuit_state_vector_are_equal(
    old_qc.remove_final_measurements(inplace=False),
    qc.remove_final_measurements(inplace=False)
)
"""
        return qiskit_src.replace(qasm_2_str, qpy_roundtrip_str)

    multi_qasm_1 = "qc_1 = QuantumCircuit.from_qasm_str(qc_1.qasm())"
    multi_qasm_2 = "qc_2 = QuantumCircuit.from_qasm_str(qc_2.qasm())"
    if multi_qasm_1 in qiskit_src and multi_qasm_1 in qiskit_src:
        qpy_roundtrip_str = f"""
{fn}
old_qc_1 = qc_1

qc_1 = qpy_roundtrip(qc_1)
assert circuit_state_vector_are_equal(
    old_qc_1.remove_final_measurements(inplace=False),
    qc_1.remove_final_measurements(inplace=False)
)
"""
        qc_2 = """
old_qc_2 = qc_2
qc_2 = qpy_roundtrip(qc_2)

assert circuit_state_vector_are_equal(
    old_qc_2.remove_final_measurements(inplace=False),
    qc_2.remove_final_measurements(inplace=False)
)
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
    qiskit_metadata["qiskit_followup"] = followup_source_metadata

    qiskit_metadata["source_followup_divergence"] = None
    if (
        qiskit_source_metadata["result"] is not None
        and followup_source_metadata["result"] is not None
    ):
        qiskit_metadata["source_followup_divergence"] = detect_divergence(
            qiskit_source_metadata["result"], followup_source_metadata["result"]
        )

    sources = {}
    if "ToQasmAndBack" in source_metadata["followup"]["metamorphic_transformations"]:
        # QASM3 roundtrip
        qasm3_source, qasm3_metadata = qasm3_roundtrip(followup_source)
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
        if (
            qasm3_metadata["result"] is not None
            and followup_source_metadata["result"] is not None
        ):
            qiskit_metadata["qasm3_followup_divergence"] = detect_divergence(
                qasm3_metadata["result"], followup_source_metadata["result"]
            )

        # QPY roundtrip
        qpy_source, qpy_metadata = qpy_roundtrip(followup_source, source_metadata)
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
        if (
            qpy_metadata["result"] is not None
            and followup_source_metadata["result"] is not None
        ):
            qiskit_metadata["qpy_followup_divergence"] = detect_divergence(
                qpy_metadata["result"], followup_source_metadata["result"]
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

    metadata["source_followup_divergence"] = None
    if exec_metadata["result"] is not None and followup_metadata["result"] is not None:
        metadata["source_followup_divergence"] = detect_divergence(
            exec_metadata["result"], followup_metadata["result"]
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
            followup_metadata["result"] is not None
            and cirq_qasm_qiskit_metadata["result"] is not None
        ):
            metadata["followup_cirq_qasm_qiskit_divergence"] = detect_divergence(
                followup_metadata["result"], cirq_qasm_qiskit_metadata["result"]
            )

    return {
        "cirq_metadata": metadata,
        "sources": {
            "cirq_source": source_cirq,
            "cirq_followup": followup_cirq,
            **sources,
        },
    }


def execute_cirq_qasm_qiskit(qiskit_source: str, source_metadata: dict):
    pass


def pyquil_related_execs(
    qiskit_source: str, followup_source: str, source_metadata: dict
):
    metadata = {}
    _, source_pyquil = PyQuilCircuit(qiskit_source).get_follow_up({})

    exec_metadata = execute_with_log(source_pyquil, "PyQuil source")
    metadata["pyquil_source"] = exec_metadata

    config = convert_morphq_metadata(source_metadata)
    metadata["config"] = config

    _, followup_pyquil = PyQuilCircuit(followup_source).get_follow_up(config)
    followup_metadata = execute_with_log(followup_pyquil, "PyQuil followup")
    metadata["pyquil_followup"] = followup_metadata

    metadata["source_followup_divergence"] = None
    if exec_metadata["result"] is not None and followup_metadata["result"] is not None:
        metadata["source_followup_divergence"] = detect_divergence(
            exec_metadata["result"], followup_metadata["result"]
        )

    return {
        "pyquil_metadata": metadata,
        "sources": {
            "pyquil_source": source_pyquil,
            "pyquil_followup": followup_pyquil,
        },
    }


def main(prog_id: str, qiskit_source: str, followup_source: str, source_metadata: dict):
    saved_location_folder = "qcross-data/completed-execs/"
    metadata = {
        "prog_id": prog_id,
    }

    execute_qiskit = True
    execute_cirq = True
    execute_pyquil = True

    if execute_qiskit:
        qiskit_metadata = qiskit_related_execs(
            qiskit_source, followup_source, source_metadata
        )
        write_content_to_file(
            qiskit_metadata["sources"],
            os.path.join(saved_location_folder, prog_id, "qiskit"),
        )

        metadata["qiskit"] = qiskit_metadata["qiskit_metadata"]

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
    manual_exlusions = ["e3a4d2dff93e4dc39349b2d17471723c"]
    if prog_id in manual_exlusions or prog_id in os.listdir(
        join("qcross-data", "completed-execs")
    ):
        Log.yellow(f"Skipping {prog_id} since it is already executed")
        return False
    return True


def use_morphq_data(folder):
    Path(join("qcross-data", "completed-execs")).mkdir(parents=True, exist_ok=True)
    i = 0
    for file in os.listdir(join(folder, "source")):
        prog_id = file.split(".")[0]

        if not should_execute(prog_id):
            continue

        if i == 20:
            break

        Log.blue(f"Processing '{os.path.join(folder, file)}' ...")
        result = get_all_content(folder, file)
        if result is None:
            continue

        qiskit_source, followup_source, source_metadata = result

        main(prog_id, fix_cx3(qiskit_source), fix_cx3(followup_source), source_metadata)
        i += 1


if __name__ == "__main__":
    use_morphq_data("data/qmt_v56/programs")
