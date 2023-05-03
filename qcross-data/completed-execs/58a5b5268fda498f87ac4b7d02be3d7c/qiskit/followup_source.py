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


qc_1.append(RZGate(6.163759533339787), qargs=[qr_1[1]], cargs=[])
qc_1.append(CRZGate(4.2641612072511235), qargs=[qr_1[3], qr_1[1]], cargs=[])
qc_1.append(CRXGate(5.987304452123941), qargs=[qr_1[0], qr_1[4]], cargs=[])
qc_1.append(CCXGate(), qargs=[qr_1[2], qr_1[5], qr_1[4]], cargs=[])
qc_1.append(TGate(), qargs=[qr_1[5]], cargs=[])
qc_1.append(CRZGate(4.167661441102218), qargs=[qr_1[0], qr_1[3]], cargs=[])
qc_1.append(RZGate(4.229610589867865), qargs=[qr_1[0]], cargs=[])


qr_2 = QuantumRegister(3, name='qr_2')
cr_2 = ClassicalRegister(3, name='cr_2')
qc_2 = QuantumCircuit(qr_2, cr_2, name='qc_2')


qc_2.append(ZGate(), qargs=[qr_2[2]], cargs=[])
qc_2.append(XGate(), qargs=[qr_2[0]], cargs=[])
qc_2.append(SXGate(), qargs=[qr_2[2]], cargs=[])
qc_2.append(CSXGate(), qargs=[qr_2[1], qr_2[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc_1.measure(qr_1, cr_1)
qc_2.measure(qr_2, cr_2)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc_1 = transpile(qc_1, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [1, 0], [1, 2], [1, 3], [1, 4], [1, 5], [1, 9], [2, 1], [2, 10], [3, 1], [3, 6], [3, 10], [4, 1], [5, 1], [6, 3], [7, 10], [8, 10], [9, 1], [10, 2], [10, 3], [10, 7], [10, 8]])
qc_2 = transpile(qc_2, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [1, 0], [1, 2], [1, 3], [1, 4], [1, 5], [1, 9], [2, 1], [2, 10], [3, 1], [3, 6], [3, 10], [4, 1], [5, 1], [6, 3], [7, 10], [8, 10], [9, 1], [10, 2], [10, 3], [10, 7], [10, 8]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_ea9f9962f47b41bcbc927956e52723e9 = Aer.get_backend('qasm_simulator')
counts_1 = execute(qc_1, backend=backend_ea9f9962f47b41bcbc927956e52723e9, shots=5542).result().get_counts(qc_1)
counts_2 = execute(qc_2, backend=backend_ea9f9962f47b41bcbc927956e52723e9, shots=5542).result().get_counts(qc_2)
RESULT = [counts_1, counts_2]
