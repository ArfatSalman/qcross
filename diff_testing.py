import os
from pathlib import Path
import json
from termcolor import colored
import numpy as np

from qcross.utils import execute_single_py_program, fix_cx3, display_results, detect_divergence
from qcross.transpiler_pyquil import PyQuilCircuit

SRC_FOLDER = "data/qmt_v55/programs/source/"

# FOLLOWUP_FOLDER = "data/qmt_v53/programs/followup/"
# METADATA_FOLDER = "data/qmt_v53/programs/metadata/"

EXEC_METADATA_FOLDER = "data/differential-testing/"

Path(EXEC_METADATA_FOLDER).mkdir(parents=True, exist_ok=True)

limit = 10

np.seterr(divide="ignore")
np.seterr(invalid="ignore")

DONE_FILE = open("DIFF_DONE.csv", "r+", encoding="utf-8")
completed = DONE_FILE.read().splitlines()

SUCCESS_COUNT = 0
TOTAL = 0
FAILURES = 0

def run_modified_qiskit(filepath):
    with open(filepath, encoding='utf-8') as f:



def execute_file(file):
    exception = False

    filename = file.split(".")[0]

    # if file in completed:
    #     return

    DONE_FILE.write(f"{file}\n")
    completed.append(file)

    src = SRC_FOLDER + file

    print(colored(f"\nOpening {file}", "green", attrs=["bold"]))

    metadata = {}

    try:
        with open(src, encoding="ascii") as f:
            qiskit_src = fix_cx3(f.read())

            try:
                print('RUNNING qiskit')
                src_res, _ = execute_single_py_program(qiskit_src)
                print('END RUNNING qiskit')
                metadata["src_res"] = src_res
            except Exception as error:
                exception = True
                metadata["src_Error"] = str(error)
                src_res = {}
                print(f"Error while executing SOURCE of {file}")
                print(colored(error, "red"))

            m, quil_src = PyQuilCircuit(qiskit_src).get_follow_up(
                {"add_unitary": False}
            )
            try:
                print('RUNNING pyquil')
                quil, _ = execute_single_py_program(quil_src)
                print('END RUNNING qiskit')
                metadata["quil"] = quil
            except Exception as error:
                exception = True
                metadata["src_Error"] = str(error)
                quil = {}
                print(f"Error while executing src of {file}")
                print(colored(error, "red"))

    except IOError:
        print(colored(f"cannot open {src}", "red"))
        return
    global TOTAL
    TOTAL += 1
    if True:
        if exception is False:
            metadata["divergence"] = detect_divergence(src_res, quil)
            print(colored(metadata["divergence"], "yellow"))
        display_results({"src": src_res, "quil": quil})

        Path(EXEC_METADATA_FOLDER + filename).mkdir(parents=True, exist_ok=True)
        with open(
            EXEC_METADATA_FOLDER + filename + "/" + filename + ".json",
            "w",
            encoding="utf-8",
        ) as w:
            w.write(json.dumps(metadata, sort_keys=True, indent=4))

        with open(
            EXEC_METADATA_FOLDER + filename + "/" + file, "w", encoding="utf-8"
        ) as w:
            w.write(qiskit_src)

        with open(
            EXEC_METADATA_FOLDER + filename + "/" + filename + ".followup.py",
            "w",
            encoding="utf-8",
        ) as w:
            w.write(quil_src)
    else:
        global SUCCESS_COUNT
        SUCCESS_COUNT += 1
        print(colored("SUCCESS", "green"))

    return


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        filename = sys.argv[1]
        execute_file(filename)
    else:
        count = 10
        for file in os.listdir(SRC_FOLDER):
            if file in completed:
                continue
            if count == 0:
                break
            count -= 1
            execute_file(file)
    print(
        colored(f"SUCCESS={SUCCESS_COUNT}, FAILURES={FAILURES}, TOTAL={TOTAL}", "green")
    )
    DONE_FILE.close()
