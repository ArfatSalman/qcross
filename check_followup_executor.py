import os
from pathlib import Path
import json
from termcolor import colored
import numpy as np

from qcross.utils import execute_single_py_program, fix_cx3, display_results
from transpiler import CirqCircuit

SRC_FOLDER = "data/qmt_v53/programs/source/"
FOLLOWUP_FOLDER = "data/qmt_v53/programs/followup/"
METADATA_FOLDER = "data/qmt_v53/programs/metadata/"

EXEC_METADATA_FOLDER = "data/cirq-src-followup-check/"

Path(EXEC_METADATA_FOLDER).mkdir(parents=True, exist_ok=True)

limit = 10

np.seterr(divide="ignore")
np.seterr(invalid="ignore")

DONE_FILE = open("DONE.csv", "r+", encoding="utf-8")
completed = DONE_FILE.read().splitlines()

def execute_for_cirq(qiskit_src):
    try:
        pass
    except:
        pass


def execute_file(file):
    exception = False
    filename = file.split(".")[0]

    # if f"{filename}.json" in os.listdir(EXEC_METADATA_FOLDER + filename):
    #     return
    if file in completed:
        return

    DONE_FILE.write(f"{file}\n")
    completed.append(file)

    metadata_file = METADATA_FOLDER + filename + ".json"
    src = SRC_FOLDER + file
    follow_up = FOLLOWUP_FOLDER + file

    print(colored(f"\nOpening {file}", "green", attrs=["bold"]))

    metadata = {}

    try:
        with open(metadata_file, encoding="ascii") as f:
            data = json.loads(f.read())
            relations = data["followup"]["metamorphic_transformations"]
            metadata["relations"] = relations
            print(relations)
    except IOError:
        print(colored(f"cannot open metadata {metadata_file}", "red"))
        return

    try:
        with open(src, encoding="ascii") as f:
            qiskit_src = fix_cx3(f.read())
            m, src = CirqCircuit(qiskit_src).get_follow_up(
                {"add_unitary": False, "seed": 1223}
            )
            m, src = CirqCircuit(qiskit_src).get_follow_up(
                {"add_unitary": False, "seed": 1223}
            )

            try:
                src_res, _ = execute_single_py_program(src)
                metadata["src_res"] = src_res
            except Exception as error:
                exception = True
                metadata['src_Error'] = str(error)
                src_res = {}
                print(f"Error while executing SOURCE of {file}")
                print(colored(error, "red"))

    except IOError:
        print(colored(f"cannot open {metadata_file}", "red"))
        return

    return
    try:
        with open(follow_up, encoding="ascii") as f:
            followup_src = f.read()
            config = {"add_unitary": False, "seed": 1223}

            if "ToQasmAndBack" in relations:
                config["qasm_roundtrip"] = True

            if "ChangeBackend" in relations:
                config["backend"] = "DensityMatrixSimulator"

            if "InjectParameters" in relations:
                params = {}
                for k in data["followup"]["metamorphic_info"]:
                    if (
                        "replacement_dictionary"
                        in data["followup"]["metamorphic_info"][k]
                    ):
                        params.update(
                            data["followup"]["metamorphic_info"][k][
                                "replacement_dictionary"
                            ]
                        )
                if not params:
                    raise ValueError("params not found")

                config["inject_params"] = params

            if "ChangeQubitOrder" in relations:
                for k in data["followup"]["metamorphic_info"]:
                    if "mapping" in data["followup"]["metamorphic_info"][k]:
                        order = data["followup"]["metamorphic_info"][k]["mapping"]

                        config["qubit_order"] = eval(order)
                        break
                else:
                    raise ValueError("params not found")

            if "ChangeOptLevel" in relations:
                config["transformations"] = [
                    "defer_measurements",
                    "merge_k_qubit_unitaries",
                    "drop_empty_moments",
                    "eject_z",
                    "eject_phased_paulis",
                    "drop_negligible_operations",
                    "stratified_circuit",
                    "synchronize_terminal_measurements",
                ]

            if "InjectNullEffect" in relations:
                """implicit support for sub-circuits"""

            if "RunIndependentPartitions" in relations:
                mapping = None
                for k in data["followup"]["metamorphic_info"]:
                    if "mapping" in data["followup"]["metamorphic_info"][k]:
                        mapping = (
                            data["followup"]["metamorphic_info"][k][
                                "partition_0_mapping"
                            ],
                            data["followup"]["metamorphic_info"][k][
                                "partition_1_mapping"
                            ],
                        )

                config["independent_circuits"] = mapping

            m, followup_src = CirqCircuit(fix_cx3(followup_src)).get_follow_up(config)

            try:
                followup_res, _ = execute_single_py_program(src)
                metadata["followup_res"] = followup_res
            except Exception as error:
                exception = True
                followup_res = {}
                metadata['follow_up_Error'] = str(error)
                print(f"Error while executing FOLLOWUP of {file}")
                print(colored(error, "red"))

    except IOError:
        print(
            colored(
                f"cannot find followup {file}",
                "red",
                attrs=["bold"],
            )
        )
        return

    if exception or src_res != followup_res:
        print(colored("incorrect result", "red"))
        display_results({"src": src_res, "follow": followup_res})

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
            w.write(src)

        with open(
            EXEC_METADATA_FOLDER + filename + "/" + filename + ".followup.py",
            "w",
            encoding="utf-8",
        ) as w:
            w.write(followup_src)


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        filename = sys.argv[1]
        execute_file(filename)
    else:
        for file in os.listdir(SRC_FOLDER):
            execute_file(file)

    DONE_FILE.close()
