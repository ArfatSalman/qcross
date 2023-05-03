# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 9], [1, 0], [1, 3], [1, 5], [2, 5], [2, 8], [3, 1], [4, 5], [5, 1], [5, 2], [5, 4], [5, 6], [6, 5], [6, 7], [7, 6], [8, 2], [9, 0]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_b96a0e35a7904992824b6dcf0997a5c8 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_b96a0e35a7904992824b6dcf0997a5c8, shots=2771).result().get_counts(qc)
RESULT = counts
