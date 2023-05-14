# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_b55b30 = Parameter('p_b55b30')
p_5d3d3d = Parameter('p_5d3d3d')
p_48d37c = Parameter('p_48d37c')
p_5d4f5c = Parameter('p_5d4f5c')
p_c95cea = Parameter('p_c95cea')
p_806bcc = Parameter('p_806bcc')
p_e6233a = Parameter('p_e6233a')
p_c8910e = Parameter('p_c8910e')
p_78f4ca = Parameter('p_78f4ca')
p_f29331 = Parameter('p_f29331')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_806bcc), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[6]], cargs=[])
qc.append(CRXGate(p_b55b30), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CRZGate(1.0296448789776642), qargs=[qr[1], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[7], qr[6], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(1.740253089260498), qargs=[qr[6], qr[7]], cargs=[])
qc.append(CRZGate(p_e6233a), qargs=[qr[1], qr[7]], cargs=[])
qc.append(RZGate(p_c95cea), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(CU1Gate(3.2142159669963557), qargs=[qr[4], qr[0]], cargs=[])
qc.append(CRXGate(p_78f4ca), qargs=[qr[6], qr[4]], cargs=[])
qc.append(RZZGate(p_5d3d3d), qargs=[qr[7], qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(RZGate(p_f29331), qargs=[qr[4]], cargs=[])
qc.append(CRXGate(0.7279391018916035), qargs=[qr[0], qr[3]], cargs=[])
qc.append(CUGate(5.03147076606842, 5.0063780207098425, p_5d4f5c, 4.940217775579305), qargs=[qr[6], qr[2]], cargs=[])
qc.append(U2Gate(p_c8910e, 2.1276323672732023), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[6]], cargs=[])
qc.append(SdgGate(), qargs=[qr[0]], cargs=[])
qc.append(RZZGate(p_48d37c), qargs=[qr[3], qr[4]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_b55b30: 5.987304452123941, p_5d3d3d: 5.1829934776392745, p_48d37c: 3.950837470808744, p_5d4f5c: 3.1562533916051736, p_c95cea: 4.229610589867865, p_806bcc: 6.163759533339787, p_e6233a: 4.167661441102218, p_c8910e: 2.5163050709890156, p_78f4ca: 5.94477504571567, p_f29331: 3.775592041307464})
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=['rx', 'ry', 'rz', 'p', 'cx'],
    optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_c512c5b61df04c1594299da6a7d721f4 = Aer.get_backend('aer_simulator_density_matrix')
counts = execute(qc, backend=backend_c512c5b61df04c1594299da6a7d721f4, shots=2771).result().get_counts(qc)
RESULT = counts
