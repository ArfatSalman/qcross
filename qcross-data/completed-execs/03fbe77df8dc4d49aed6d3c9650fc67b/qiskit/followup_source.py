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
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[2], qr[1]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(UGate(4.8767543643948805, 4.182786512570673, 
    4.614324844707754), qargs=[qr[3]], cargs=[])
subcircuit.append(RZGate(6.253452668458444), qargs=[qr[2]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CRZGate(1.0296448789776642), qargs=[qr[0], qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[6], qr[1], qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[5]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(RYYGate(1.740253089260498), qargs=[qr[1], qr[6]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[0], qr[6]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[0]], cargs=[])
qc.append(SXGate(), qargs=[qr[2]], cargs=[])
qc.append(CU1Gate(3.2142159669963557), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CRXGate(5.94477504571567), qargs=[qr[1], qr[3]], cargs=[])
qc.append(RZZGate(5.1829934776392745), qargs=[qr[6], qr[2]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_7f5736 = QuantumRegister(5, name='qr_7f5736')
subcircuit.add_register(qr_7f5736)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_eec01e6a11ec47ea9064bb59ee97d342 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_eec01e6a11ec47ea9064bb59ee97d342, shots=2771).result().get_counts(qc)
RESULT = counts