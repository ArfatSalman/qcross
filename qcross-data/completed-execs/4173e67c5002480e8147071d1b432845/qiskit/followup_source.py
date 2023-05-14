# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_aab82c = Parameter('p_aab82c')
p_61e37c = Parameter('p_61e37c')
p_3f39bf = Parameter('p_3f39bf')
p_e66f86 = Parameter('p_e66f86')
p_d9b3b7 = Parameter('p_d9b3b7')
p_58380b = Parameter('p_58380b')
p_4bf6d4 = Parameter('p_4bf6d4')
p_457d2e = Parameter('p_457d2e')
p_dc6a99 = Parameter('p_dc6a99')
p_2fe099 = Parameter('p_2fe099')
p_b5cb9c = Parameter('p_b5cb9c')
p_251638 = Parameter('p_251638')
p_f86d7f = Parameter('p_f86d7f')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[6]], cargs=[])
qc.append(CRXGate(p_58380b), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CRZGate(p_f86d7f), qargs=[qr[1], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[7], qr[6], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(p_b5cb9c), qargs=[qr[6], qr[7]], cargs=[])
qc.append(CRZGate(p_3f39bf), qargs=[qr[1], qr[7]], cargs=[])
qc.append(RZGate(p_aab82c), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(CU1Gate(p_4bf6d4), qargs=[qr[4], qr[0]], cargs=[])
qc.append(CRXGate(5.94477504571567), qargs=[qr[6], qr[4]], cargs=[])
qc.append(RZZGate(p_251638), qargs=[qr[7], qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(RZGate(3.775592041307464), qargs=[qr[4]], cargs=[])
qc.append(CRXGate(p_dc6a99), qargs=[qr[0], qr[3]], cargs=[])
qc.append(CUGate(p_457d2e, p_d9b3b7, p_2fe099, p_e66f86), qargs=[qr[6], qr[2]], cargs=[])
qc.append(U2Gate(2.5163050709890156, p_61e37c), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[6]], cargs=[])
qc.append(SdgGate(), qargs=[qr[0]], cargs=[])
qc.append(RZZGate(3.950837470808744), qargs=[qr[3], qr[4]], cargs=[])
qc.append(TGate(), qargs=[qr[5]], cargs=[])
qc.append(RYYGate(1.9669252191306448), qargs=[qr[4], qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_aab82c: 4.229610589867865, p_61e37c: 2.1276323672732023, p_3f39bf: 4.167661441102218, p_e66f86: 4.940217775579305, p_d9b3b7: 5.0063780207098425, p_58380b: 5.987304452123941, p_4bf6d4: 3.2142159669963557, p_457d2e: 5.03147076606842, p_dc6a99: 0.7279391018916035, p_2fe099: 3.1562533916051736, p_b5cb9c: 1.740253089260498, p_251638: 5.1829934776392745, p_f86d7f: 1.0296448789776642})
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0,
    1], [0, 2], [0, 6], [1, 0], [1, 4], [2, 0], [2, 5], [2, 7], [3, 4], [4,
    1], [4, 3], [5, 2], [6, 0], [7, 2]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_af49a642fc434c40b3f1ca7122bf5bed = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_af49a642fc434c40b3f1ca7122bf5bed, shots=2771).result().get_counts(qc)
RESULT = counts
