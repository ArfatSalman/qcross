# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(2, name='qr')
cr = ClassicalRegister(2, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZZGate(6.163759533339787), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(ECRGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(1.977559237989846), qargs=[qr[0], qr[1]], cargs=[])
qc.append(TGate(), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[1]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CRZGate(2.2498881927557752), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[1]], cargs=[])
qc.append(RZGate(5.320621737498446), qargs=[qr[1]], cargs=[])
qc.append(RZGate(5.512260524440591), qargs=[qr[1]], cargs=[])
qc.append(CU1Gate(1.6723037552953224), qargs=[qr[0], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RZZGate(6.086884486572108), qargs=[qr[0], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(RYYGate(3.3705408413231095), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[1]], cargs=[])
qc.append(RZGate(5.190931186022931), qargs=[qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(5.167261531657622), qargs=[qr[1], qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CRXGate(4.167661441102218), qargs=[qr[1], qr[0]], cargs=[])
subcircuit.append(HGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(RXGate(6.221353754875494), qargs=[qr[0]], cargs=[])
subcircuit.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
subcircuit.append(CYGate(), qargs=[qr[1], qr[0]], cargs=[])
subcircuit.append(HGate(), qargs=[qr[1]], cargs=[])
subcircuit.append(SXGate(), qargs=[qr[1]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_44b36c = QuantumRegister(6, name='qr_44b36c')
qc.add_register(qr_44b36c)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=['rx', 'ry', 'rz', 'p', 'cx'],
    optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_9c199b0540d945bcb9033c77e39c8cf4 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_9c199b0540d945bcb9033c77e39c8cf4, shots=346).result().get_counts(qc)
RESULT = counts
