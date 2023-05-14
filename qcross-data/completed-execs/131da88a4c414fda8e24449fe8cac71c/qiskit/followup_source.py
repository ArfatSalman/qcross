# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr_1 = QuantumRegister(9, name='qr_1')
cr_1 = ClassicalRegister(9, name='cr_1')
qc_1 = QuantumCircuit(qr_1, cr_1, name='qc_1')


qc_1.append(RZGate(6.163759533339787), qargs=[qr_1[0]], cargs=[])
qc_1.append(ZGate(), qargs=[qr_1[1]], cargs=[])
qc_1.append(CCXGate(), qargs=[qr_1[3], qr_1[2], qr_1[4]], cargs=[])


qr_2 = QuantumRegister(2, name='qr_2')
cr_2 = ClassicalRegister(2, name='cr_2')
qc_2 = QuantumCircuit(qr_2, cr_2, name='qc_2')


qc_2.append(CRZGate(4.2641612072511235), qargs=[qr_2[1], qr_2[0]], cargs=[])
qc_2.append(ZGate(), qargs=[qr_2[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc_1.measure(qr_1, cr_1)
qc_2.measure(qr_2, cr_2)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc_1 = transpile(qc_1, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 8], [1, 0], [1, 3], [2, 7], [3, 1], [3, 6], [3, 11], [4, 8], [5, 7], [5, 11], [6, 3], [7, 2], [7, 5], [7, 9], [8, 0], [8, 4], [8, 9], [9, 7], [9, 8], [9, 10], [10, 9], [11, 3], [11, 5], [11, 12], [12, 11]])
qc_2 = transpile(qc_2, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 8], [1, 0], [1, 3], [2, 7], [3, 1], [3, 6], [3, 11], [4, 8], [5, 7], [5, 11], [6, 3], [7, 2], [7, 5], [7, 9], [8, 0], [8, 4], [8, 9], [9, 7], [9, 8], [9, 10], [10, 9], [11, 3], [11, 5], [11, 12], [12, 11]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_72325406009a4e8da7d8fe5940e1dc4f = Aer.get_backend('aer_simulator')
counts_1 = execute(qc_1, backend=backend_72325406009a4e8da7d8fe5940e1dc4f, shots=7838).result().get_counts(qc_1)
counts_2 = execute(qc_2, backend=backend_72325406009a4e8da7d8fe5940e1dc4f, shots=7838).result().get_counts(qc_2)
RESULT = [counts_1, counts_2]
