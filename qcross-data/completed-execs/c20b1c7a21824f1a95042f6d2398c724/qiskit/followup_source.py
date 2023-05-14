# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr_1 = QuantumRegister(7, name='qr_1')
cr_1 = ClassicalRegister(7, name='cr_1')
qc_1 = QuantumCircuit(qr_1, cr_1, name='qc_1')


qc_1.append(ZGate(), qargs=[qr_1[1]], cargs=[])
qc_1.append(XGate(), qargs=[qr_1[1]], cargs=[])
qc_1.append(CRXGate(5.987304452123941), qargs=[qr_1[0], qr_1[1]], cargs=[])


qr_2 = QuantumRegister(1, name='qr_2')
cr_2 = ClassicalRegister(1, name='cr_2')
qc_2 = QuantumCircuit(qr_2, cr_2, name='qc_2')


qc_2.append(RZGate(6.163759533339787), qargs=[qr_2[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc_1.measure(qr_1, cr_1)
qc_2.measure(qr_2, cr_2)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc_1 = transpile(qc_1, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 6], [0, 9], [1, 0], [1, 2], [1, 3], [1, 4], [2, 1], [3, 1], [3, 7], [4, 1], [5, 6], [5, 8], [5, 11], [6, 0], [6, 5], [7, 3], [8, 5], [9, 0], [10, 11], [11, 5], [11, 10]])
qc_2 = transpile(qc_2, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 6], [0, 9], [1, 0], [1, 2], [1, 3], [1, 4], [2, 1], [3, 1], [3, 7], [4, 1], [5, 6], [5, 8], [5, 11], [6, 0], [6, 5], [7, 3], [8, 5], [9, 0], [10, 11], [11, 5], [11, 10]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_fb02f68eaec645ba85ca80b918e559cb = Aer.get_backend('qasm_simulator')
counts_1 = execute(qc_1, backend=backend_fb02f68eaec645ba85ca80b918e559cb, shots=2771).result().get_counts(qc_1)
counts_2 = execute(qc_2, backend=backend_fb02f68eaec645ba85ca80b918e559cb, shots=2771).result().get_counts(qc_2)
RESULT = [counts_1, counts_2]
