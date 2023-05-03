# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_dcc7c3 = Parameter('p_dcc7c3')
p_883ff5 = Parameter('p_883ff5')
p_cbd7c7 = Parameter('p_cbd7c7')
p_ac7c01 = Parameter('p_ac7c01')
p_a8d127 = Parameter('p_a8d127')
p_464996 = Parameter('p_464996')
p_cdc516 = Parameter('p_cdc516')
p_f56c05 = Parameter('p_f56c05')
p_93f2a9 = Parameter('p_93f2a9')
p_1c4575 = Parameter('p_1c4575')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_883ff5), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[6]], cargs=[])
qc.append(CRXGate(p_a8d127), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CRZGate(p_f56c05), qargs=[qr[1], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[7], qr[6], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(p_1c4575), qargs=[qr[6], qr[7]], cargs=[])
qc.append(CRZGate(p_cdc516), qargs=[qr[1], qr[7]], cargs=[])
qc.append(RZGate(p_93f2a9), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(CU1Gate(p_cbd7c7), qargs=[qr[4], qr[0]], cargs=[])
qc.append(CRXGate(p_464996), qargs=[qr[6], qr[4]], cargs=[])
qc.append(RZZGate(p_dcc7c3), qargs=[qr[7], qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(RZGate(p_ac7c01), qargs=[qr[4]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_96a3f9 = QuantumRegister(6, name='qr_96a3f9')
qc.add_register(qr_96a3f9)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_dcc7c3: 5.1829934776392745, p_883ff5: 6.163759533339787, p_cbd7c7: 3.2142159669963557, p_ac7c01: 3.775592041307464, p_a8d127: 5.987304452123941, p_464996: 5.94477504571567, p_cdc516: 4.167661441102218, p_f56c05: 1.0296448789776642, p_93f2a9: 4.229610589867865, p_1c4575: 1.740253089260498})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=['rx', 'ry', 'rz', 'p', 'cx'], optimization_level=2, coupling_map=None)
# SECTION
# NAME: QASM_CONVERSION

from qiskit.qasm3 import loads, dumps
qc = loads(dumps(qc))

# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_392e5bfc581048b2b85fd9658217f5cf = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_392e5bfc581048b2b85fd9658217f5cf, shots=2771).result().get_counts(qc)
RESULT = counts
