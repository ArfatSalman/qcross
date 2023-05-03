# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0,
    1], [0, 6], [0, 9], [0, 11], [1, 0], [1, 2], [1, 5], [1, 8], [2, 1], [3,
    7], [3, 10], [4, 5], [5, 1], [5, 4], [5, 7], [6, 0], [7, 3], [7, 5], [8,
    1], [9, 0], [10, 3], [11, 0]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_0f927efe954d4b47a4c7b87e4d66021f = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_0f927efe954d4b47a4c7b87e4d66021f, shots=5542).result().get_counts(qc)
RESULT = counts
