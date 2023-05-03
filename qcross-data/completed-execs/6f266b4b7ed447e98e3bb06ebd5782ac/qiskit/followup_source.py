# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_466c3c = Parameter('p_466c3c')
p_fb2b59 = Parameter('p_fb2b59')
p_f17856 = Parameter('p_f17856')
p_b0d476 = Parameter('p_b0d476')
p_c9d928 = Parameter('p_c9d928')
p_faf457 = Parameter('p_faf457')
p_cd9fd2 = Parameter('p_cd9fd2')
p_d9736e = Parameter('p_d9736e')
p_38ffe1 = Parameter('p_38ffe1')
p_305826 = Parameter('p_305826')
p_2e343f = Parameter('p_2e343f')
p_3eae93 = Parameter('p_3eae93')
p_499aed = Parameter('p_499aed')
p_40b220 = Parameter('p_40b220')
p_fbab31 = Parameter('p_fbab31')
p_6f4c81 = Parameter('p_6f4c81')
p_3681fa = Parameter('p_3681fa')
p_697593 = Parameter('p_697593')
p_e1e662 = Parameter('p_e1e662')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_d9736e), qargs=[qr[3]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CRXGate(p_499aed), qargs=[qr[4], qr[3]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(CRZGate(p_c9d928), qargs=[qr[3], qr[4]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[4]], cargs=[])
qc.append(RYYGate(p_e1e662), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[4]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[4]], cargs=[])
qc.append(CUGate(p_b0d476, p_40b220, 4.623446645668956, p_fb2b59), qargs=[qr[1], qr[4]], cargs=[])
qc.append(RZGate(p_466c3c), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(p_3681fa), qargs=[qr[0], qr[2]], cargs=[])
qc.append(CU1Gate(p_38ffe1), qargs=[qr[3], qr[0]], cargs=[])
qc.append(UGate(p_6f4c81, p_3eae93, p_f17856), qargs=[qr[4]], cargs=[])
qc.append(CHGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[4]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CU1Gate(p_fbab31), qargs=[qr[0], qr[3]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[0], qr[3], qr[1]], cargs=[])
qc.append(CUGate(p_2e343f, p_faf457, p_305826, p_697593), qargs=[qr[4], qr[3]], cargs=[])
qc.append(CRZGate(p_cd9fd2), qargs=[qr[2], qr[1]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_466c3c: 4.229610589867865, p_fb2b59: 3.865496458458116, p_f17856: 1.4112277317699358, p_b0d476: 5.708725119517347, p_c9d928: 1.0296448789776642, p_faf457: 5.0063780207098425, p_cd9fd2: 3.839241945509346, p_d9736e: 6.163759533339787, p_38ffe1: 3.2142159669963557, p_305826: 3.1562533916051736, p_2e343f: 5.03147076606842, p_3eae93: 0.07157463504881167, p_499aed: 2.0099472182748075, p_40b220: 4.167661441102218, p_fbab31: 4.028174522740928, p_6f4c81: 5.887184334931191, p_3681fa: 5.398622178940033, p_697593: 4.940217775579305, p_e1e662: 1.6723037552953224})
# SECTION
# NAME: QASM_CONVERSION
qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_0a3283ec40834512a68d0e5476ef04eb = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_0a3283ec40834512a68d0e5476ef04eb, shots=979).result().get_counts(qc)
RESULT = counts
