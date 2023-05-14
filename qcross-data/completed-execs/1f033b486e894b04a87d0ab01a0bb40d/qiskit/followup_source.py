# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_547429 = Parameter('p_547429')
p_d52445 = Parameter('p_d52445')
p_791f18 = Parameter('p_791f18')
p_344604 = Parameter('p_344604')
p_2747c6 = Parameter('p_2747c6')
p_e58f03 = Parameter('p_e58f03')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(2, name='qr')
cr = ClassicalRegister(2, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZZGate(p_2747c6), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(ECRGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(p_547429), qargs=[qr[0], qr[1]], cargs=[])
qc.append(TGate(), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[1]], cargs=[])
qc.append(CRXGate(p_344604), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CRZGate(2.2498881927557752), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[1]], cargs=[])
qc.append(RZGate(5.320621737498446), qargs=[qr[1]], cargs=[])
qc.append(RZGate(5.512260524440591), qargs=[qr[1]], cargs=[])
qc.append(CU1Gate(p_e58f03), qargs=[qr[0], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RZZGate(6.086884486572108), qargs=[qr[0], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(RYYGate(3.3705408413231095), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[1]], cargs=[])
qc.append(RZGate(p_791f18), qargs=[qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(p_d52445), qargs=[qr[1], qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_f52a64 = QuantumRegister(10, name='qr_f52a64')
qc.add_register(qr_f52a64)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_547429: 1.977559237989846, p_d52445: 5.167261531657622, p_791f18: 5.190931186022931, p_344604: 5.987304452123941, p_2747c6: 6.163759533339787, p_e58f03: 1.6723037552953224})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_ab0841badfbe43d19f6327899e036c6c = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_ab0841badfbe43d19f6327899e036c6c, shots=346).result().get_counts(qc)
RESULT = counts
