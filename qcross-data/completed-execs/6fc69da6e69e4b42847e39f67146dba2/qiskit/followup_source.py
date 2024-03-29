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
qc.append(CSXGate(), qargs=[qr[6], qr[7]], cargs=[])
qc.append(CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245,
    5.987304452123941), qargs=[qr[0], qr[2]], cargs=[])
qc.append(SdgGate(), qargs=[qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[8], qr[3], qr[5]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[5]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[8]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[4], qr[6], qr[0]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(CU1Gate(3.2142159669963557), qargs=[qr[8], qr[4]], cargs=[])
qc.append(CRZGate(1.4112277317699358), qargs=[qr[5], qr[8]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[6]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(CHGate(), qargs=[qr[2], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[4], qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=['rx', 'ry', 'rz', 'p', 'cx'], optimization_level=1, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_eb0f1c9a8e044601aaa9788c95271de9 = Aer.get_backend('aer_simulator_density_matrix')
counts = execute(qc, backend=backend_eb0f1c9a8e044601aaa9788c95271de9, shots=3919).result().get_counts(qc)
RESULT = counts
