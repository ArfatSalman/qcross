import os
import re


from time import perf_counter_ns
from pathlib import Path
from datetime import datetime
import cirq
from termcolor import colored
from json import dumps
from lib.detectors import JS_Detector, KS_Detector
from random import shuffle
from copy import deepcopy
from itertools import chain, combinations, permutations


import numpy as np

np.seterr(divide="ignore")
np.seterr(invalid="ignore")

from transpiler import CirqCircuit


def linear_subsequences(arr):
    res = []
    for i in range(1, len(arr) + 1):
        res.append(arr[0:i])
    return res


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


qiskit_circuits_folder = "data/qmt_v53/programs/source/"
cirq_circuits_folder = "data/qmt-cirq-new-check/cirq-src/"
exec_metadata_path = "data/qmt-cirq-new-check/exec-metadata/"

Path(cirq_circuits_folder).mkdir(parents=True, exist_ok=True)
Path(exec_metadata_path).mkdir(parents=True, exist_ok=True)


def detect_divergence(exec_metadata, detector):
    stat, pval = detector.check(
        result_A=exec_metadata["res_A"], result_B=exec_metadata["res_B"]
    )
    return {"statistic": stat, "p-value": pval}


def execute_single_py_program(py_content: str):
    """Execute a single python program."""
    GLOBALS = {"RESULT": None, "UNITARY": None}
    exec(py_content, GLOBALS)
    return GLOBALS["RESULT"], GLOBALS["UNITARY"]


def timed_execute_single_py_program(py_content: str):
    time_start = perf_counter_ns()
    res, unitary = execute_single_py_program(py_content)
    time_end = perf_counter_ns()

    return res, unitary, time_end - time_start


def write_metadata_file(filename, qiskit_res, cirq_res, exec_time, divergence, **args):
    metadata = {
        "qiskit_res": qiskit_res,
        "cirq_result": cirq_res,
        "exec_time": exec_time,
        "divergence": divergence,
    }

    metadata.update(args)

    filename_without_ext = filename.split(".")[0]

    with open(f"{exec_metadata_path + filename_without_ext}.json", "w") as f:
        f.write(dumps(metadata, indent=4))


def add_unitary_measurements_to_qiskit_source(src: str):
    if src.find("# NAME: MEASUREMENT") == -1:
        raise ValueError("can not add unitary measurements to qiskit source")

    return src.replace(
        "# NAME: MEASUREMENT",
        """
# NAME: MEASUREMENT
import qiskit.quantum_info as qi
UNITARY = qi.Operator(qc.reverse_bits()).data
""",
    )

QasmUGate_Pattern = re.compile(r'QasmUGate\(.*\)')

def write_file(path, content):
    with open(path, "w", encoding="ascii") as f:
        f.write(content)


def execute_with_few_optimizations(filename, config, transpiler_obj, res_to_check, write_to_file=False):
    print(colored(f"===== RUNNING SUBSETS ======", "red", attrs=["bold"]))

    subsets = permutations(config["transformations"])
    subset_metadata = {}
    count = 0
    for i, subset in enumerate(subsets):
        count += 1
        if count > 100:
            break
        # transpiler_obj = CirqCircuit(qiskit_source)
        subset_followup_metadata, subset_followup = transpiler_obj.get_follow_up(
            {"transformations": list(subset)}
        )
        subset_metadata[i] = {
            "subset": subset_followup_metadata["transformations_order"]
        }
        # print(colored(f"Executing SUBSET FOLLOWUP {i}", "blue", attrs=["bold"]))
        try:
            (
                res_followup,
                _,
                time_followup,
            ) = timed_execute_single_py_program(subset_followup)
        except:
            write_file(f"cirq_followup_temp_subset_{i}_filename", subset_followup)
            raise
        subset_metadata[i].update(
            {
                "subset_res": res_followup,
                "divergence_from_qiskit": detect_divergence(
                    {"res_A": res_to_check, "res_B": res_followup},
                    KS_Detector(),
                ),
            }
        )
        if write_to_file:
            with open(f"{cirq_circuits_folder}subset_{i}_{filename}", "w") as f:
                f.write(subset_followup)

    return subset_metadata


base_config = {
    "add_unitary": True,
    "transformations": None # [
    #     "defer_measurements",
    #     "merge_k_qubit_unitaries",
    #     "drop_empty_moments",
    #     "eject_z",
    #     "eject_phased_paulis",
    #     "drop_negligible_operations",
    #     "stratified_circuit",
    #     "synchronize_terminal_measurements",
    # ],
}


def execute(files):
    count = 0
    for filename in files:
        qiskit_circuit_fullpath = qiskit_circuits_folder + filename
        filename_without_ext = filename.split(".")[0]
        if os.path.exists(exec_metadata_path + f"{filename_without_ext}.json"):
            # print(colored(f"Skipping QISKIT {filename}", "green", attrs=["bold"]))
            count += 1
            continue

        with open(qiskit_circuit_fullpath) as file:
            print(colored(f"Opening QISKIT {filename}", "green"))
            qiskit_source = file.read()
            transpiler_obj = CirqCircuit(qiskit_source)
            cirq_source = transpiler_obj.get_equivalent()

            config = deepcopy(base_config)
            # shuffle(config["transformations"])

            followup_metadata, cirq_source_follow_up = transpiler_obj.get_follow_up(
                config
            )

        instrumented_qiskit_source = add_unitary_measurements_to_qiskit_source(
            qiskit_source
        )
        # qiskit_time_start = perf_counter_ns()
        # qiskit_res, qiskit_unitary = execute_single_py_program(
        #     instrumented_qiskit_source
        # )
        # qiskit_time_end = perf_counter_ns()
        print(colored(f"Executing QISKIT", "yellow", attrs=["bold"]))
        try:
            qiskit_res, qiskit_unitary, qiskit_time = timed_execute_single_py_program(
                instrumented_qiskit_source
            )
        except:
            write_file("qiskit_temp_" + filename, instrumented_qiskit_source)
            raise

        # cirq_time_start = perf_counter_ns()
        # cirq_res, cirq_unitary = execute_single_py_program(cirq_source)
        # cirq_time_end = perf_counter_ns()
        print(colored(f"Executing CIRQ", "yellow", attrs=["bold"]))
        try:
            cirq_res, cirq_unitary, cirq_time = timed_execute_single_py_program(
                cirq_source
            )
        except:
            write_file("cirq_temp_" + filename, cirq_source)
            raise

        print(colored(f"Executing CIRQ FOLLOWUP", "yellow", attrs=["bold"]))
        try:
            (
                cirq_res_followup,
                cirq_unitary_followup,
                cirq_time_followup,
            ) = timed_execute_single_py_program(cirq_source_follow_up)
        except:
            write_file("cirq_followup_temp_" + filename, cirq_source_follow_up)
            raise

        if not np.allclose(qiskit_unitary, cirq_unitary):
            if re.search(QasmUGate_Pattern, cirq_source) is None:
                print(colored(f"allclose = False and NO qasm gate found", "yellow", attrs=["bold"]))
                raise

            if not cirq.equal_up_to_global_phase(qiskit_unitary, cirq_unitary):
                print(colored(f"equal_up_to_global_phase = False", "red", attrs=["bold"]))
                raise
            else:
                print(colored("equal_up_to_global_phase = True", "green", attrs=["bold"]))
        else:
            print(colored("allclose = True", "green", attrs=["bold"]))

        ks_qiskit_cirq_followup = detect_divergence(
            {"res_A": qiskit_res, "res_B": cirq_res_followup}, KS_Detector()
        )
        ks_cirq_cirq_followup = detect_divergence(
            {"res_A": cirq_res, "res_B": cirq_res_followup}, KS_Detector()
        )

        divergence_metadata = {
            "ks_qiskit_cirq": detect_divergence(
                {"res_A": qiskit_res, "res_B": cirq_res}, KS_Detector()
            ),
            "ks_qiskit_cirq_followup": ks_qiskit_cirq_followup,
            "ks_cirq_cirq_followup": ks_cirq_cirq_followup,
        }
        subset_metadata = None
        if False and ks_qiskit_cirq_followup["p-value"] <= 1:
            print(f"START: {datetime.now()}")
            subset_metadata = execute_with_few_optimizations(
                filename, config, transpiler_obj, qiskit_res
            )
            print(f"END: {datetime.now()}")

        cirq_filepath = cirq_circuits_folder + filename
        with open(cirq_filepath, "w") as cirq_file:
            cirq_file.write(cirq_source)

        cirq_filepath = cirq_circuits_folder + "followup_" + filename
        with open(cirq_filepath, "w") as cirq_file:
            cirq_file.write(cirq_source_follow_up)

        write_metadata_file(
            filename,
            qiskit_res,
            cirq_res,
            {
                "qiskit": f"{(qiskit_time) / 10 ** 6} ms",
                "cirq": f"{(cirq_time) / 10 ** 6} ms",
                "cirq_followup": f"{(cirq_time_followup) / 10 ** 6} ms",
            },
            divergence_metadata,
            cirq_res_followup=cirq_res_followup,
            followup_metadata=followup_metadata,
            subset_metadata=subset_metadata,
        )
        count += 1

        for key in divergence_metadata:
            if divergence_metadata[key]["p-value"] < 0.05:
                print(colored(f"DIVERGENCE {filename}", "red", attrs=["bold"]))

    print(colored(f"Count = {count}", "red", attrs=["bold"]))


if __name__ == "__main__":
    files = os.listdir(qiskit_circuits_folder)
    execute(files)
