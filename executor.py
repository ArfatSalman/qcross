import os


from time import perf_counter_ns
from pathlib import Path

from termcolor import colored
from json import dumps
from lib.detectors import JS_Detector, KS_Detector

import numpy as np

from transpiler import CirqCircuit

qiskit_circuits_folder = "data/qmt_v53/programs/source/"
cirq_circuits_folder = "data/qmt-cirq/cirq-src/"
exec_metadata_path = "data/qmt-cirq/exec-metadata/"

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


def write_metadata_file(filename, qiskit_res, cirq_res, exec_time, divergence):
    metadata = {
        "qiskit_res": qiskit_res,
        "cirq_result": cirq_res,
        "exec_time": exec_time,
        "divergence": divergence,
    }

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

def execute():
    count = 0
    files = os.listdir(qiskit_circuits_folder)
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
            cirq_source = CirqCircuit.from_qiskit_source(qiskit_source)

        qiskit_time_start = perf_counter_ns()
        instrumented_qiskit_source = add_unitary_measurements_to_qiskit_source(
            qiskit_source
        )
        qiskit_res, qiskit_unitary = execute_single_py_program(
            instrumented_qiskit_source
        )
        qiskit_time_end = perf_counter_ns()

        cirq_time_start = perf_counter_ns()
        cirq_res, cirq_unitary = execute_single_py_program(cirq_source)
        cirq_time_end = perf_counter_ns()

        if not np.allclose(qiskit_unitary, cirq_unitary):
            print(colored(f"allclose = False", "red", attrs=["bold"]))
            raise

        divergence_metadata = {
            "ks": detect_divergence(
                {"res_A": qiskit_res, "res_B": cirq_res}, KS_Detector()
            ),
            "js": detect_divergence(
                {"res_A": qiskit_res, "res_B": cirq_res}, JS_Detector()
            ),
        }

        cirq_filepath = cirq_circuits_folder + filename
        with open(cirq_filepath, "w") as cirq_file:
            cirq_file.write(cirq_source)

        write_metadata_file(
            filename,
            qiskit_res,
            cirq_res,
            {
                "qiskit": f"{(qiskit_time_end - qiskit_time_start) / 10 ** 6} ms",
                "cirq": f"{(cirq_time_end - cirq_time_start) / 10 ** 6} ms",
            },
            divergence_metadata,
        )
        count += 1

        if divergence_metadata["ks"]['p-value'] < 0.05:
            print(colored(f"DIVERGENCE {filename}", 'red', attrs=["bold"]))
            break
    print(colored(f"Count = {count}", "red", attrs=["bold"]))

if __name__ == "__main__":
    execute()
