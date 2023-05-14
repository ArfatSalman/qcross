# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_660fb5 = Parameter('p_660fb5')
p_773c06 = Parameter('p_773c06')
p_bfa20f = Parameter('p_bfa20f')
p_77ac42 = Parameter('p_77ac42')
p_a65f95 = Parameter('p_a65f95')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[6]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[0], qr[6]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(RXGate(0.7631154445516055), qargs=[qr[3]], cargs=[])
subcircuit.append(CXGate(), qargs=[qr[3], qr[7]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CRZGate(1.0296448789776642), qargs=[qr[1], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[7], qr[6], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(p_bfa20f), qargs=[qr[6], qr[7]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[1], qr[7]], cargs=[])
qc.append(RZGate(p_77ac42), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(CU1Gate(3.2142159669963557), qargs=[qr[4], qr[0]], cargs=[])
qc.append(CRXGate(5.94477504571567), qargs=[qr[6], qr[4]], cargs=[])
qc.append(RZZGate(p_660fb5), qargs=[qr[7], qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(RZGate(3.775592041307464), qargs=[qr[4]], cargs=[])
qc.append(CRXGate(0.7279391018916035), qargs=[qr[0], qr[3]], cargs=[])
qc.append(CUGate(p_773c06, 5.0063780207098425, 3.1562533916051736, 4.940217775579305), qargs=[qr[6], qr[2]], cargs=[])
qc.append(U2Gate(2.5163050709890156, 2.1276323672732023), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[6]], cargs=[])
qc.append(SdgGate(), qargs=[qr[0]], cargs=[])
qc.append(RZZGate(p_a65f95), qargs=[qr[3], qr[4]], cargs=[])
qc.append(TGate(), qargs=[qr[5]], cargs=[])
qc.append(RYYGate(1.9669252191306448), qargs=[qr[4], qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[3], qr[2], qr[5]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[7]], cargs=[])
qc.append(UGate(5.080799300534071, 5.023617931957853, 2.271164628944128), qargs=[qr[2]], cargs=[])
qc.append(ECRGate(), qargs=[qr[6], qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_660fb5: 5.1829934776392745, p_773c06: 5.03147076606842, p_bfa20f: 1.740253089260498, p_77ac42: 4.229610589867865, p_a65f95: 3.950837470808744})
# SECTION
# NAME: QASM_CONVERSION

qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0,
    1], [0, 8], [0, 9], [1, 0], [1, 3], [1, 4], [1, 6], [1, 11], [2, 11], [
    3, 1], [4, 1], [5, 9], [6, 1], [6, 10], [7, 11], [8, 0], [9, 0], [9, 5],
    [10, 6], [11, 1], [11, 2], [11, 7]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_2e2a0ced73404813811826dd5d59b42f = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_2e2a0ced73404813811826dd5d59b42f, shots=2771).result().get_counts(qc)
RESULT = counts
