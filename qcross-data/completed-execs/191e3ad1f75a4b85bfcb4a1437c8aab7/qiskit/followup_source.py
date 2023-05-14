# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[7]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[6], qr[7]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[0], qr[5]], cargs=[])
qc.append(CCXGate(), qargs=[qr[3], qr[9], qr[5]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(TGate(), qargs=[qr[9]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[0], qr[6]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[0]], cargs=[])
qc.append(SXGate(), qargs=[qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[8], qr[2]], cargs=[])
qc.append(CCXGate(), qargs=[qr[8], qr[9], qr[3]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[8], qr[4], qr[9]], cargs=[])
qc.append(CSXGate(), qargs=[qr[4], qr[1]], cargs=[])
qc.append(ZGate(), qargs=[qr[4]], cargs=[])
qc.append(CHGate(), qargs=[qr[5], qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[4]], cargs=[])
qc.append(CRZGate(2.586208953975239), qargs=[qr[0], qr[1]], cargs=[])
qc.append(U2Gate(2.5163050709890156, 2.1276323672732023), qargs=[qr[1]],
    cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_1f51171d3f0b43958b515a7ddaeea2c5 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_1f51171d3f0b43958b515a7ddaeea2c5, shots=5542).result().get_counts(qc)
RESULT = counts
