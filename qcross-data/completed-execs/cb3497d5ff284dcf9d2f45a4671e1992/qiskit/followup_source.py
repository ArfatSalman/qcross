# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(9, name='qr')
cr = ClassicalRegister(9, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[4]], cargs=[])
qc.append(CSXGate(), qargs=[qr[3], qr[7]], cargs=[])
qc.append(CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245,
    5.987304452123941), qargs=[qr[8], qr[5]], cargs=[])
qc.append(SdgGate(), qargs=[qr[0]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[8], qr[4], qr[1], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(SGate(), qargs=[qr[8]], cargs=[])
qc.append(SGate(), qargs=[qr[4]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[6], qr[3], qr[8]], cargs=[])
qc.append(SXGate(), qargs=[qr[8]], cargs=[])
qc.append(CU1Gate(3.2142159669963557), qargs=[qr[4], qr[6]], cargs=[])
qc.append(CRZGate(1.4112277317699358), qargs=[qr[2], qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(CSXGate(), qargs=[qr[8], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(CHGate(), qargs=[qr[5], qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[6], qr[8]], cargs=[])
qc.append(CRZGate(2.586208953975239), qargs=[qr[0], qr[3]], cargs=[])
qc.append(U2Gate(2.5163050709890156, 2.1276323672732023), qargs=[qr[3]],
    cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
qc.append(CCXGate(), qargs=[qr[8], qr[5], qr[0]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[7], qr[8], qr[0]], cargs=[])
qc.append(TGate(), qargs=[qr[8]], cargs=[])
qc.append(RZGate(5.014941143947427), qargs=[qr[0]], cargs=[])
qc.append(CRXGate(5.970852306777193), qargs=[qr[0], qr[4]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 4], [0, 5], [0, 9], [0, 10], [1, 0], [2, 6], [3, 10], [4, 0], [5, 0], [5, 7], [6, 2], [6, 7], [7, 5], [7, 6], [7, 8], [7, 11], [8, 7], [9, 0], [10, 0], [10, 3], [11, 7]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_63b890e71bd64f9bb7567a6d6facf6dc = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_63b890e71bd64f9bb7567a6d6facf6dc, shots=3919).result().get_counts(qc)
RESULT = counts
