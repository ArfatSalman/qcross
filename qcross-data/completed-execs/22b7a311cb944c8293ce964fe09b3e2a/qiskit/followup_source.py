# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_1b6af5 = Parameter('p_1b6af5')
p_224ae5 = Parameter('p_224ae5')
p_e5c76f = Parameter('p_e5c76f')
p_88b560 = Parameter('p_88b560')
p_772597 = Parameter('p_772597')
p_7edefd = Parameter('p_7edefd')
p_b289d6 = Parameter('p_b289d6')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_772597), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[6]], cargs=[])
qc.append(CRXGate(p_7edefd), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CRZGate(1.0296448789776642), qargs=[qr[1], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[7], qr[6], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(1.740253089260498), qargs=[qr[6], qr[7]], cargs=[])
qc.append(CRZGate(p_1b6af5), qargs=[qr[1], qr[7]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(CU1Gate(3.2142159669963557), qargs=[qr[4], qr[0]], cargs=[])
qc.append(CRXGate(p_e5c76f), qargs=[qr[6], qr[4]], cargs=[])
qc.append(RZZGate(p_88b560), qargs=[qr[7], qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(RZGate(p_b289d6), qargs=[qr[4]], cargs=[])
qc.append(CRXGate(p_224ae5), qargs=[qr[0], qr[3]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_1b6af5: 4.167661441102218, p_224ae5: 0.7279391018916035, p_e5c76f: 5.94477504571567, p_88b560: 5.1829934776392745, p_772597: 6.163759533339787, p_7edefd: 5.987304452123941, p_b289d6: 3.775592041307464})
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_c17a3dc79b524a98859ba708d992a884 = Aer.get_backend('aer_simulator_statevector')
counts = execute(qc, backend=backend_c17a3dc79b524a98859ba708d992a884, shots=2771).result().get_counts(qc)
RESULT = counts
