import os
import sys
from termcolor import colored
import numpy
from numpy import allclose, printoptions

from transpiler import CirqCircuit

def execute_single_py_program(filepath: str):
    """Execute a single python program."""
    py_content = open(filepath, "r").read()
    GLOBALS = {"RESULT": 0}
    exec(py_content, GLOBALS)
    return GLOBALS["RESULT"]

def execute_single_py_program_unitary(py_content: str):
    """Execute a single python program."""
    GLOBALS = {"UNITARY": None}
    exec(py_content, GLOBALS)
    return GLOBALS["UNITARY"]


path = "data/qmt_v55/programs/source/"
cirq_folder_path = "data/qmt_v55/programs/cirq/"

files = os.listdir(path)

file_path = '/Users/arfat/Desktop/qc-test/data/qmt_v53/programs/followup/0a3d48f93dbc418baf938627300020e8.py'
print(f'opening {file_path}')
py_content = open(file_path, "r").read()

m, cirq_content = CirqCircuit(py_content).get_follow_up({})

with open('temp_cirq.py', 'w') as f:
    f.write(cirq_content)

py_content = py_content.replace('# NAME: MEASUREMENT', """
# NAME: MEASUREMENT
import qiskit.quantum_info as qi
UNITARY = qi.Operator(qc.reverse_bits()).data
""")

# print(py_content)

Q = execute_single_py_program_unitary(py_content)
# C = execute_single_py_program_unitary(cirq_content)

# if allclose(Q, C):
#     print(f'allclose = {colored(True, "green", attrs=["bold"])}')
# else:
#     print(f'allclose = {colored(False, "red", attrs=["bold"])}')




