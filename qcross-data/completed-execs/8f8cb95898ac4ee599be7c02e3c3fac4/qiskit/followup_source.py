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
qc.append(RZGate(6.163759533339787), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[6]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CRZGate(1.0296448789776642), qargs=[qr[1], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[7], qr[6], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(1.740253089260498), qargs=[qr[6], qr[7]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[1], qr[7]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(CU1Gate(3.2142159669963557), qargs=[qr[4], qr[0]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(ZGate(), qargs=[qr[7]], cargs=[])
subcircuit.append(ECRGate(), qargs=[qr[5], qr[2]], cargs=[])
subcircuit.append(SwapGate(), qargs=[qr[1], qr[3]], cargs=[])
subcircuit.append(TGate(), qargs=[qr[7]], cargs=[])
subcircuit.append(RZGate(5.116009661150895), qargs=[qr[2]], cargs=[])
subcircuit.append(RCCXGate(), qargs=[qr[2], qr[5], qr[0]], cargs=[])
subcircuit.append(SXdgGate(), qargs=[qr[6]], cargs=[])
subcircuit.append(CCXGate(), qargs=[qr[5], qr[3], qr[4]], cargs=[])
subcircuit.append(RCCXGate(), qargs=[qr[1], qr[6], qr[7]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CRXGate(5.94477504571567), qargs=[qr[6], qr[4]], cargs=[])
qc.append(RZZGate(5.1829934776392745), qargs=[qr[7], qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(RZGate(3.775592041307464), qargs=[qr[4]], cargs=[])
qc.append(CRXGate(0.7279391018916035), qargs=[qr[0], qr[3]], cargs=[])
qc.append(CUGate(5.03147076606842, 5.0063780207098425, 3.1562533916051736, 4.940217775579305), qargs=[qr[6], qr[2]], cargs=[])
qc.append(U2Gate(2.5163050709890156, 2.1276323672732023), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[6]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 7], [1, 0], [1, 2], [1, 3], [1, 5], [2, 1], [3, 1], [4, 6], [4, 7], [5, 1], [6, 4], [7, 0], [7, 4]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_d412039631c742a8a11a2b67e3a20ae7 = Aer.get_backend('aer_simulator_density_matrix')
counts = execute(qc, backend=backend_d412039631c742a8a11a2b67e3a20ae7, shots=2771).result().get_counts(qc)
RESULT = counts
