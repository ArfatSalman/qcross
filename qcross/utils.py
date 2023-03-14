import os
import json
import re
from time import perf_counter_ns


from lib.detectors import JS_Detector, KS_Detector
from termcolor import colored

paths = [
    "data/qmt_v52/programs/source",
    "data/qmt_v53/programs/source",
    "data/qmt_v54/programs/source",
    "data/qmt_v55/programs/source",
    "data/qmt_v56/programs/source",
]


def get_file_data(path):
    with open(path, encoding="utf-8") as f:
        content = f.read()
        return content


def detect_divergence(a, b, detector=KS_Detector()):
    stat, pval = detector.check(result_A=a, result_B=b)
    return {"statistic": stat, "p-value": pval}


CX3_REGEX = r"^(qc\.append\(C3XGate\()[\d+.]+(\),.*\))$"

C3X_REGEX_param = r"^(qc\.append\(C3XGate\().+(\),.*\))\s?#\s*.*$"


def fix_cx3(src):
    if re.search(CX3_REGEX, src, flags=re.MULTILINE):
        return re.sub(CX3_REGEX, r"\1\2", src, flags=re.MULTILINE)
    return re.sub(C3X_REGEX_param, r"\1\2", src, flags=re.MULTILINE)


def add_unitary_to_qiskit(src):
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


def get_qiskit_content_by_program_id(prog_id, remove_cx3=False):
    for folder in paths:
        filename = prog_id + ".py"
        try:
            content = open(folder + "/" + filename, encoding="ascii").read()
            if remove_cx3:
                content = re.sub(r"qc.append\(C3XGate\(.*\)", "\n", content)
            return content
        except Exception:
            continue


from prettytable import PrettyTable


def display_results(obj):
    x = PrettyTable()
    x.field_names = ["bitstr"] + list(sorted(obj.keys()))

    keys = set()
    for k in obj:
        for k2 in obj[k]:
            keys.add(k2)

    for bitstr in sorted(keys):
        row = [bitstr]
        for k in sorted(obj):
            row.append(obj[k].get(bitstr, " "))
        x.add_row(row)

    print(x)
    return x


class Logger:
    def __init__(self):
        self.should_log = os.environ.get("QCROSS_LOG", True)

    def red(self, args):
        if self.should_log:
            print(colored(args, color="red"))

    def yellow(self, args):
        if self.should_log:
            print(colored(args, color="yellow"))

    def green(self, args):
        if self.should_log:
            print(colored(args, color="green", attrs=["bold"]))

    def blue(self, args):
        if self.should_log:
            print(colored(args, color="blue", attrs=["bold"]))


Log = Logger()


def convert_morphq_metadata(data):

    if isinstance(data, str):
        with open(data, encoding="utf-8") as f:
            data = json.load(f)

    result = {}
    relations = data["followup"]["metamorphic_transformations"]
    result["relations"] = relations

    if "ToQasmAndBack" in relations:
        result["qasm_roundtrip"] = True

    if "AddUnusedRegister" in relations:
        result["unused_registers"] = True

    if "ChangeBackend" in relations:
        result["backend"] = "DensityMatrixSimulator"

    if "InjectParameters" in relations:
        params = {}
        for k in data["followup"]["metamorphic_info"]:
            if "replacement_dictionary" in data["followup"]["metamorphic_info"][k]:
                params.update(
                    data["followup"]["metamorphic_info"][k]["replacement_dictionary"]
                )
        if not params:
            raise ValueError("params not found")

        result["inject_params"] = params

    if "ChangeQubitOrder" in relations:
        for k in data["followup"]["metamorphic_info"]:
            if "mapping" in data["followup"]["metamorphic_info"][k]:
                order = data["followup"]["metamorphic_info"][k]["mapping"]

                result["qubit_order"] = eval(order)
                break
        else:
            raise ValueError("params not found")

    if "ChangeOptLevel" in relations:
        for k in data["followup"]["metamorphic_info"]:
            if "initial_level" in data["followup"]["metamorphic_info"][k]:
                result["opt_level"] = data["followup"]["metamorphic_info"][k]

    if "InjectNullEffect" in relations:
        """implicit support for sub-circuits"""

    if "RunIndependentPartitions" in relations:
        mapping = None
        for k in data["followup"]["metamorphic_info"]:
            if "mapping" in data["followup"]["metamorphic_info"][k]:
                mapping = (
                    data["followup"]["metamorphic_info"][k]["partition_0_mapping"],
                    data["followup"]["metamorphic_info"][k]["partition_1_mapping"],
                )

        result["independent_circuits"] = mapping

    return result
