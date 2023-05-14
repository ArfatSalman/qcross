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
qc.append(RZGate(6.163759533339787), qargs=[qr[8]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[7]], cargs=[])
qc.append(CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245,
    5.987304452123941), qargs=[qr[4], qr[6]], cargs=[])
qc.append(SdgGate(), qargs=[qr[5]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[4], qr[8], qr[0], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[3]], cargs=[])
qc.append(SGate(), qargs=[qr[4]], cargs=[])
qc.append(SGate(), qargs=[qr[8]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[5], qr[1], qr[2], qr[4]], cargs=[])
qc.append(SXGate(), qargs=[qr[4]], cargs=[])
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
backend_89930c5c008f46b2bb258f0fae556311 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_89930c5c008f46b2bb258f0fae556311, shots=3919).result().get_counts(qc)
RESULT = counts
