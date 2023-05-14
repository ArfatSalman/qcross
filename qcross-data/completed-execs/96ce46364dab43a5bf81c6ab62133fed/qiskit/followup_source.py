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
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CPhaseGate(4.63837786161633), qargs=[qr[6], qr[2]], cargs=[])
subcircuit.append(SXGate(), qargs=[qr[4]], cargs=[])
subcircuit.append(C3XGate(5.94477504571567), qargs=[qr[6], qr[4], qr[7], qr[2]], cargs=[])
subcircuit.append(CU3Gate(5.1829934776392745, 2.7315239782495464, 3.9984051265341463), qargs=[qr[2], qr[0]], cargs=[])
subcircuit.append(SXGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(CRZGate(2.008796895454228), qargs=[qr[0], qr[5]], cargs=[])
subcircuit.append(CSXGate(), qargs=[qr[4], qr[0]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
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
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0,
    1], [0, 7], [0, 9], [0, 10], [1, 0], [1, 2], [2, 1], [2, 3], [3, 2], [4,
    5], [5, 4], [5, 9], [6, 8], [7, 0], [8, 6], [8, 9], [9, 0], [9, 5], [9,
    8], [9, 11], [10, 0], [11, 9]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_b94cfcea66734c66b3e51551c3972432 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_b94cfcea66734c66b3e51551c3972432, shots=2771).result().get_counts(qc)
RESULT = counts
