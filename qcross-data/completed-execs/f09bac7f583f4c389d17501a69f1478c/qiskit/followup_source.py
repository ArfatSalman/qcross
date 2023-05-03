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
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(XGate(), qargs=[qr[4]], cargs=[])
qc.append(CRXGate(2.0099472182748075), qargs=[qr[6], qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[3], qr[0], qr[5], qr[6]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[3]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[6], qr[5], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(ECRGate(), qargs=[qr[3], qr[4]], cargs=[])
qc.append(SdgGate(), qargs=[qr[3]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[6], qr[2], qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[5]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[5]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[6], qr[5], qr[4]], cargs=[])
qc.append(CU1Gate(3.2142159669963557), qargs=[qr[1], qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 5], [1, 0], [1, 2], [1, 3], [2, 1], [2, 4], [3, 1], [3, 6], [4, 2], [5, 0], [5, 7], [6, 3], [7, 5]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_fbf8d4c269174afcbe99f694d7908c6d = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_fbf8d4c269174afcbe99f694d7908c6d, shots=1959).result().get_counts(qc)
RESULT = counts
