# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_097544 = Parameter('p_097544')
p_6bf657 = Parameter('p_6bf657')
p_cda6ce = Parameter('p_cda6ce')
p_74776f = Parameter('p_74776f')
p_45ab98 = Parameter('p_45ab98')
p_814b0e = Parameter('p_814b0e')
p_2092b7 = Parameter('p_2092b7')
p_9cf47d = Parameter('p_9cf47d')
p_2a789a = Parameter('p_2a789a')
p_f9d44b = Parameter('p_f9d44b')
p_a08081 = Parameter('p_a08081')
p_6b1e96 = Parameter('p_6b1e96')
p_e59b9b = Parameter('p_e59b9b')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_6bf657), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[6]], cargs=[])
qc.append(CRXGate(p_cda6ce), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CRZGate(1.0296448789776642), qargs=[qr[1], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[7], qr[6], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(p_f9d44b), qargs=[qr[6], qr[7]], cargs=[])
qc.append(CRZGate(p_814b0e), qargs=[qr[1], qr[7]], cargs=[])
qc.append(RZGate(p_e59b9b), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(CU1Gate(p_2092b7), qargs=[qr[4], qr[0]], cargs=[])
qc.append(CRXGate(5.94477504571567), qargs=[qr[6], qr[4]], cargs=[])
qc.append(RZZGate(p_097544), qargs=[qr[7], qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(RZGate(p_6b1e96), qargs=[qr[4]], cargs=[])
qc.append(CRXGate(p_9cf47d), qargs=[qr[0], qr[3]], cargs=[])
qc.append(CUGate(p_2a789a, p_74776f, 3.1562533916051736, p_a08081), qargs=[qr[6], qr[2]], cargs=[])
qc.append(U2Gate(2.5163050709890156, p_45ab98), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[6]], cargs=[])
qc.append(SdgGate(), qargs=[qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_097544: 5.1829934776392745, p_6bf657: 6.163759533339787, p_cda6ce: 5.987304452123941, p_74776f: 5.0063780207098425, p_45ab98: 2.1276323672732023, p_814b0e: 4.167661441102218, p_2092b7: 3.2142159669963557, p_9cf47d: 0.7279391018916035, p_2a789a: 5.03147076606842, p_f9d44b: 1.740253089260498, p_a08081: 4.940217775579305, p_6b1e96: 3.775592041307464, p_e59b9b: 4.229610589867865})
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1, coupling_map=[[0,
    1], [0, 2], [0, 4], [1, 0], [1, 3], [2, 0], [3, 1], [3, 6], [4, 0], [4,
    5], [5, 4], [6, 3], [6, 7], [7, 6]])
# SECTION
# NAME: QASM_CONVERSION


from qiskit.qasm3 import loads, dumps
qc = loads(dumps(qc))

# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_c79a3d5d56714f52badf0cb5077047d9 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_c79a3d5d56714f52badf0cb5077047d9, shots=2771).result().get_counts(qc)
RESULT = counts
