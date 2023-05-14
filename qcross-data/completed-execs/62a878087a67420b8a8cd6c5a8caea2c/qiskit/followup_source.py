# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[1]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(XGate(), qargs=[qr[3]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[4], qr[3]], cargs=[])
qc.append(CRZGate(1.0296448789776642), qargs=[qr[0], qr[3]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[4], qr[2], qr[3], qr[7]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(RYYGate(1.740253089260498), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[0], qr[2]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[0]], cargs=[])
qc.append(SXGate(), qargs=[qr[4]], cargs=[])
qc.append(CU1Gate(3.2142159669963557), qargs=[qr[1], qr[4]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_db4291 = QuantumRegister(9, name='qr_db4291')
qc.add_register(qr_db4291)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_9d3694be51384353bc8af4684d36fa32 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_9d3694be51384353bc8af4684d36fa32, shots=2771).result().get_counts(qc)
RESULT = counts