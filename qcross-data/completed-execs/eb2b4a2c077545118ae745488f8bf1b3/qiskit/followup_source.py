# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(7, name='qr')
cr = ClassicalRegister(7, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 3], [0, 6], [1, 0], [1, 2], [1, 8], [2, 1], [3, 0], [4, 5], [4, 8], [5, 4], [6, 0], [6, 9], [7, 8], [8, 1], [8, 4], [8, 7], [9, 6]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_cc7f670669364ec38c6168502b0a7f5f = Aer.get_backend('aer_simulator_density_matrix')
counts = execute(qc, backend=backend_cc7f670669364ec38c6168502b0a7f5f, shots=1959).result().get_counts(qc)
RESULT = counts
