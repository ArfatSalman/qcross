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
qc.append(RZGate(6.163759533339787), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[6]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[0], qr[6]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0,
    1], [0, 5], [0, 6], [1, 0], [1, 9], [1, 10], [2, 5], [3, 8], [4, 5], [4,
    7], [4, 11], [5, 0], [5, 2], [5, 4], [6, 0], [6, 8], [7, 4], [8, 3], [8,
    6], [9, 1], [10, 1], [11, 4]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_fefea7d8c4744634adafc1c901aa6260 = Aer.get_backend('aer_simulator_matrix_product_state')
counts = execute(qc, backend=backend_fefea7d8c4744634adafc1c901aa6260, shots=2771).result().get_counts(qc)
RESULT = counts
