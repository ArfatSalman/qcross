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
qc.append(RZGate(6.163759533339787), qargs=[qr[1]], cargs=[])
qc.append(ZGate(), qargs=[qr[5]], cargs=[])
qc.append(XGate(), qargs=[qr[4]], cargs=[])
qc.append(CRXGate(2.0099472182748075), qargs=[qr[0], qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[5], qr[6], qr[3], qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[5]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[6], qr[0], qr[3], qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=['rx', 'ry', 'rz', 'p', 'cx'], optimization_level=3, coupling_map=[[0, 1], [0, 3], [0, 6], [1, 0], [1, 2], [2, 1], [2, 4], [2, 5], [3, 0], [4, 2], [5, 2], [6, 0]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_75a7b616b048472b9689a8b1ad568a66 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_75a7b616b048472b9689a8b1ad568a66, shots=1959).result().get_counts(qc)
RESULT = counts

print(RESULT)