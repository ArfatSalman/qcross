# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr_1 = QuantumRegister(6, name='qr_1')
cr_1 = ClassicalRegister(6, name='cr_1')
qc_1 = QuantumCircuit(qr_1, cr_1, name='qc_1')


qc_1.append(RZGate(6.163759533339787), qargs=[qr_1[1]], cargs=[])
qc_1.append(XGate(), qargs=[qr_1[0]], cargs=[])


qr_2 = QuantumRegister(1, name='qr_2')
cr_2 = ClassicalRegister(1, name='cr_2')
qc_2 = QuantumCircuit(qr_2, cr_2, name='qc_2')


qc_2.append(ZGate(), qargs=[qr_2[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc_1.measure(qr_1, cr_1)
qc_2.measure(qr_2, cr_2)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc_1 = transpile(qc_1, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 6], [1, 0], [1, 9], [2, 3], [3, 2], [3, 9], [4, 9], [5, 6], [5, 7], [5, 8], [6, 0], [6, 5], [7, 5], [8, 5], [9, 1], [9, 3], [9, 4]])
qc_2 = transpile(qc_2, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 6], [1, 0], [1, 9], [2, 3], [3, 2], [3, 9], [4, 9], [5, 6], [5, 7], [5, 8], [6, 0], [6, 5], [7, 5], [8, 5], [9, 1], [9, 3], [9, 4]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_8984f04357364ee8b62ea4ba6e6eb14a = Aer.get_backend('qasm_simulator')
counts_1 = execute(qc_1, backend=backend_8984f04357364ee8b62ea4ba6e6eb14a, shots=1959).result().get_counts(qc_1)
counts_2 = execute(qc_2, backend=backend_8984f04357364ee8b62ea4ba6e6eb14a, shots=1959).result().get_counts(qc_2)
RESULT = [counts_1, counts_2]
