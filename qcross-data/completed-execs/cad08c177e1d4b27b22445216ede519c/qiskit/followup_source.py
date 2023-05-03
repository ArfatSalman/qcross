# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr_1 = QuantumRegister(8, name='qr_1')
cr_1 = ClassicalRegister(8, name='cr_1')
qc_1 = QuantumCircuit(qr_1, cr_1, name='qc_1')


qc_1.append(CRZGate(4.2641612072511235), qargs=[qr_1[2], qr_1[0]], cargs=[])
qc_1.append(CCXGate(), qargs=[qr_1[1], qr_1[5], qr_1[3]], cargs=[])
qc_1.append(ZGate(), qargs=[qr_1[0]], cargs=[])
qc_1.append(XGate(), qargs=[qr_1[3]], cargs=[])
qc_1.append(RCCXGate(), qargs=[qr_1[6], qr_1[2], qr_1[4]], cargs=[])
qc_1.append(CCXGate(), qargs=[qr_1[3], qr_1[6], qr_1[0]], cargs=[])


qr_2 = QuantumRegister(3, name='qr_2')
cr_2 = ClassicalRegister(3, name='cr_2')
qc_2 = QuantumCircuit(qr_2, cr_2, name='qc_2')


qc_2.append(RZGate(6.163759533339787), qargs=[qr_2[0]], cargs=[])
qc_2.append(ZGate(), qargs=[qr_2[1]], cargs=[])
qc_2.append(RZGate(4.229610589867865), qargs=[qr_2[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc_1.measure(qr_1, cr_1)
qc_2.measure(qr_2, cr_2)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc_1 = transpile(qc_1, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 4], [1, 0], [1, 3], [1, 6], [1, 8], [1, 10], [2, 6], [3, 1], [3, 7], [3, 9], [3, 11], [4, 0], [4, 12], [5, 7], [5, 10], [5, 11], [6, 1], [6, 2], [6, 12], [7, 3], [7, 5], [8, 1], [8, 11], [9, 3], [10, 1], [10, 5], [11, 3], [11, 5], [11, 8], [12, 4], [12, 6]])
qc_2 = transpile(qc_2, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 4], [1, 0], [1, 3], [1, 6], [1, 8], [1, 10], [2, 6], [3, 1], [3, 7], [3, 9], [3, 11], [4, 0], [4, 12], [5, 7], [5, 10], [5, 11], [6, 1], [6, 2], [6, 12], [7, 3], [7, 5], [8, 1], [8, 11], [9, 3], [10, 1], [10, 5], [11, 3], [11, 5], [11, 8], [12, 4], [12, 6]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_1c1c1829609c49859e01c8529eabdb4b = Aer.get_backend('qasm_simulator')
counts_1 = execute(qc_1, backend=backend_1c1c1829609c49859e01c8529eabdb4b, shots=7838).result().get_counts(qc_1)
counts_2 = execute(qc_2, backend=backend_1c1c1829609c49859e01c8529eabdb4b, shots=7838).result().get_counts(qc_2)
RESULT = [counts_1, counts_2]
