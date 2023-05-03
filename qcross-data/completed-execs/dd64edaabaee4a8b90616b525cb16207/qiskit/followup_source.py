# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_31eb9a = Parameter('p_31eb9a')
p_2f614c = Parameter('p_2f614c')
p_0aa758 = Parameter('p_0aa758')
p_98af8b = Parameter('p_98af8b')
p_296b91 = Parameter('p_296b91')
p_704f8c = Parameter('p_704f8c')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_31eb9a), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[6]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CRZGate(p_704f8c), qargs=[qr[1], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[7], qr[6], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(RYGate(2.936349225876477), qargs=[qr[0]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(RYYGate(p_98af8b), qargs=[qr[6], qr[7]], cargs=[])
qc.append(CRZGate(p_0aa758), qargs=[qr[1], qr[7]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(CU1Gate(p_296b91), qargs=[qr[4], qr[0]], cargs=[])
qc.append(CRXGate(p_2f614c), qargs=[qr[6], qr[4]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_31eb9a: 6.163759533339787, p_2f614c: 5.94477504571567, p_0aa758: 4.167661441102218, p_98af8b: 1.740253089260498, p_296b91: 3.2142159669963557, p_704f8c: 1.0296448789776642})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1, coupling_map=None)
# SECTION
# NAME: QASM_CONVERSION

qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_4c74e0b2e8e64b19922929edca0f1574 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_4c74e0b2e8e64b19922929edca0f1574, shots=2771).result().get_counts(qc)
RESULT = counts
