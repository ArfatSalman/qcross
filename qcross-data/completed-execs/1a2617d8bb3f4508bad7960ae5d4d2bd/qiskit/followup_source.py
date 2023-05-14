# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_c44195 = Parameter('p_c44195')
p_79c15b = Parameter('p_79c15b')
p_d72302 = Parameter('p_d72302')
p_f05a11 = Parameter('p_f05a11')
p_381d88 = Parameter('p_381d88')
p_3f6521 = Parameter('p_3f6521')
p_24e500 = Parameter('p_24e500')
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
qc.append(RYYGate(p_79c15b), qargs=[qr[0], qr[1]], cargs=[])
qc.append(TGate(), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[1]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CRZGate(p_24e500), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[1]], cargs=[])
qc.append(RZGate(p_381d88), qargs=[qr[1]], cargs=[])
qc.append(RZGate(5.512260524440591), qargs=[qr[1]], cargs=[])
qc.append(CU1Gate(p_3f6521), qargs=[qr[0], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RZZGate(6.086884486572108), qargs=[qr[0], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(RYYGate(p_c44195), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[1]], cargs=[])
qc.append(RZGate(p_f05a11), qargs=[qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(p_d72302), qargs=[qr[1], qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[1], qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_c44195: 3.3705408413231095, p_79c15b: 1.977559237989846, p_d72302: 5.167261531657622, p_f05a11: 5.190931186022931, p_381d88: 5.320621737498446, p_3f6521: 1.6723037552953224, p_24e500: 2.2498881927557752})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=3, coupling_map=None)
# SECTION
# NAME: EXECUTION
from qiskit import Aer, transpile, execute
backend_35c2e8dabe334d85ac9a25e0e9b3f317 = Aer.get_backend(
    'aer_simulator_matrix_product_state')
counts = execute(qc, backend=backend_35c2e8dabe334d85ac9a25e0e9b3f317,
    shots=346).result().get_counts(qc)
RESULT = counts
