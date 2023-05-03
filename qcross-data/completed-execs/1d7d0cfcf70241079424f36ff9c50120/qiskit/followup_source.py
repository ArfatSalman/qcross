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
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])
qc.append(CSXGate(), qargs=[qr[5], qr[1]], cargs=[])
qc.append(CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245,
    5.987304452123941), qargs=[qr[2], qr[6]], cargs=[])
qc.append(SdgGate(), qargs=[qr[0]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[3], qr[7], qr[8]], cargs=[])
qc.append(ZGate(), qargs=[qr[5]], cargs=[])
qc.append(XGate(), qargs=[qr[8]], cargs=[])
qc.append(SGate(), qargs=[qr[2]], cargs=[])
qc.append(SGate(), qargs=[qr[3]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[4], qr[5], qr[2]], cargs=[])
qc.append(SXGate(), qargs=[qr[2]], cargs=[])
qc.append(CU1Gate(3.2142159669963557), qargs=[qr[3], qr[4]], cargs=[])
qc.append(CRZGate(1.4112277317699358), qargs=[qr[8], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[5]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[5]], cargs=[])
qc.append(ZGate(), qargs=[qr[7]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 6], [1, 0], [1, 5], [1, 7], [1, 10], [2, 8], [2, 9], [3, 7], [4, 8], [5, 1], [5, 8], [5, 11], [5, 12], [6, 0], [7, 1], [7, 3], [8, 2], [8, 4], [8, 5], [9, 2], [10, 1], [11, 5], [12, 5]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_5eb5f854d79a49f399eb052a2c65fef7 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_5eb5f854d79a49f399eb052a2c65fef7, shots=3919).result().get_counts(qc)
RESULT = counts
