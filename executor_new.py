import os
import cirq
import sys

from datetime import datetime
from multiprocessing import Pool
import itertools

import re

from pathlib import Path

from termcolor import colored
from json import dumps
from lib.detectors import JS_Detector, KS_Detector
from random import shuffle
from copy import deepcopy
from itertools import chain, combinations, permutations


import numpy as np

# np.seterr(divide="ignore")
# np.seterr(invalid="ignore")

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
cirq_circuits_folder = "data/qmt-cirq-permutations/cirq-src/"
exec_metadata_path = "data/qmt-cirq-permutations/exec-metadata/"

Path(cirq_circuits_folder).mkdir(parents=True, exist_ok=True)
Path(exec_metadata_path).mkdir(parents=True, exist_ok=True)


def detect_divergence(exec_metadata, detector=KS_Detector()):
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


def write_file(path, content):
    with open(path, "w", encoding="ascii") as f:
        f.write(content)


def pool_helper(chunk):
    (transpiler_obj, perm, i) = chunk

    subset_followup_metadata, subset_followup = transpiler_obj.get_follow_up(
        {"transformations": perm, "add_unitary": False}
    )
    metadata = {"perm": subset_followup_metadata["transformations_order"]}

    if i % 100 == 0:
        print(colored(f"STARTING {i}", "blue", attrs=["bold"]))
    try:
        (
            res_followup,
            _,  # unitary
            _,  # time
        ) = timed_execute_single_py_program(subset_followup)
    except Exception as e:
        metadata["exception"] = str(e)

    metadata.update(
        {
            "res_followup": res_followup,
        }
    )
    return metadata


def execute_with_few_optimizations(
    filename, config, transpiler_obj, cirq_res, qiskit_res
):
    subsets = permutations(config["transformations"])
    subset_metadata = []

    with Pool() as pool:
        res = pool.imap(
            pool_helper,
            (
                (transpiler_obj, perm, i)
                for i, perm in enumerate(subsets)
            ),
        )
        for i, metadata in enumerate(res):
            metadata.update(
                {
                    "divergence_from_cirq": detect_divergence(
                        {"res_A": cirq_res, "res_B": metadata["res_followup"]},
                        KS_Detector(),
                    ),
                    "divergence_from_qiskit": detect_divergence(
                        {"res_A": qiskit_res, "res_B": metadata["res_followup"]},
                        KS_Detector(),
                    ),
                }
            )
            subset_metadata.append({i: metadata})

    return subset_metadata


base_config = {
    "transformations": [
        "defer_measurements",
        "merge_k_qubit_unitaries",
        "drop_empty_moments",
        "eject_z",
        "eject_phased_paulis",
        "drop_negligible_operations",
        "stratified_circuit",
        "synchronize_terminal_measurements",
    ],
}


def execute(lb, ub):
    count = 0
    print('Executing ', lb, ub)
    with open("choices.txt", encoding="utf-8") as f:
        files = f.readlines()

    files = files[lb:ub]

    start_time = datetime.now()
    for i, filedata in enumerate(files):
        folder, program_id = filedata.split(", ")
        program_id = program_id.strip()
        folder = folder.strip()
        filename = f'{program_id.strip()}.py'
        qiskit_circuit_fullpath = (
            f"data/{folder.strip()}/programs/source/{program_id.strip()}.py"
        )

        if os.path.exists(exec_metadata_path + f"{program_id}.json"):
            print(colored(f" {i+lb}: already done {filename}", "red"))
            count += 1
            continue

        with open(qiskit_circuit_fullpath, encoding="utf-8") as file:
            print(colored(f" {i+lb}: Opening QISKIT {filename}", "green"))
            qiskit_source = file.read()

        instrumented_qiskit_source = add_unitary_measurements_to_qiskit_source(
            qiskit_source
        )

        instrumented_qiskit_source = re.sub(
            r"qc.append\(C3XGate\(.*\)", "\n", instrumented_qiskit_source
        )
        transpiler_obj = CirqCircuit(instrumented_qiskit_source)
        try:
            cirq_source = transpiler_obj.get_equivalent()
        except Exception:
            print(colored(f"Skipping {filename}", "yellow", attrs=["bold"]))
            continue

        metadata = {}

        print(colored("Executing Instrumented QISKIT", "yellow", attrs=["bold"]))
        try:
            qiskit_res, qiskit_unitary, qiskit_time = timed_execute_single_py_program(
                instrumented_qiskit_source
            )
        except Exception as e:
            metadata["qiskit_exception"] = str(e)

        print(colored("Executing CIRQ", "yellow", attrs=["bold"]))
        try:
            cirq_res, cirq_unitary, cirq_time = timed_execute_single_py_program(
                cirq_source
            )
        except Exception as e:
            metadata["cirq_exception"] = str(e)

        if not np.allclose(qiskit_unitary, cirq_unitary):
            print(colored(f"allclose = False", "yellow", attrs=["bold"]))
            metadata["all_close"] = False
            if not cirq.equal_up_to_global_phase(qiskit_unitary, cirq_unitary):
                print(
                    colored(f"equal_up_to_global_phase = False", "red", attrs=["bold"])
                )
                metadata["equal_up_to_global_phase"] = False

        divergence_metadata = {
            "ks_qiskit_cirq": detect_divergence(
                {"res_A": qiskit_res, "res_B": cirq_res}, KS_Detector()
            )
        }
        subset_metadata = {}
        if (
            "cirq_exception" not in metadata
            and "equal_up_to_global_phase" not in metadata
        ):
            subset_metadata = execute_with_few_optimizations(
                filename, base_config, transpiler_obj, cirq_res, qiskit_res
            )
        else:
            print(
                colored(
                    "CIRQ has exeptions or unitary not equal. Did not calculate all permutations.",
                    "red",
                    attrs=["bold"],
                )
            )

        cirq_filepath = cirq_circuits_folder + filename
        with open(cirq_filepath, "w", encoding="utf-8") as cirq_file:
            cirq_file.write(cirq_source)

        write_metadata_file(
            filename,
            qiskit_res,
            cirq_res,
            {
                "qiskit": f"{(qiskit_time) / 10 ** 6} ms",
                "cirq": f"{(cirq_time) / 10 ** 6} ms",
            },
            divergence_metadata,
            subset_metadata=subset_metadata,
            metadata=metadata,
            time={"total_time_taken": str(datetime.now() - start_time)},
        )
        count += 1

    print(colored(f"Count = {count}", "red", attrs=["bold"]))


# if __name__ == "__main__":
#     args = sys.argv[1]
#     lb, ub = args.split(':')
#     execute(int(lb), int(ub))
