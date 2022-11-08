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

file_path = '48fe12d5150d4d0bbb6b82dedc39141c.py'
print(f'opening {file_path}')
py_content = open(path + file_path, "r").read()

cirq_content = CirqCircuit.from_qiskit_source(py_content)
with open('temp_cirq.py', 'w') as f:
    f.write(cirq_content)

py_content = py_content.replace('# NAME: MEASUREMENT', """
# NAME: MEASUREMENT
import qiskit.quantum_info as qi
UNITARY = qi.Operator(qc.reverse_bits()).data
""")

Q = execute_single_py_program_unitary(py_content)
C = execute_single_py_program_unitary(cirq_content)
if allclose(Q, C):
    print(f'allclose = {colored(True, "green", attrs=["bold"])}')
else:
    print(f'allclose = {colored(False, "red", attrs=["bold"])}')
    with printoptions(threshold=200):
        print(len(Q))
        print(len(C))
        print(Q == C)
        print('qiskit')
        print(colored(Q, 'red'))
        print('cirq')
        print(colored(C, 'yellow'))



