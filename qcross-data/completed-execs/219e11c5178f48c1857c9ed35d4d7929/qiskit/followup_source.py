# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_7a4196 = Parameter('p_7a4196')
p_6c0341 = Parameter('p_6c0341')
p_36ff61 = Parameter('p_36ff61')
p_0404e8 = Parameter('p_0404e8')
p_669081 = Parameter('p_669081')
p_92c9c5 = Parameter('p_92c9c5')
p_c06d9c = Parameter('p_c06d9c')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(2, name='qr')
cr = ClassicalRegister(2, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZZGate(p_c06d9c), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(ECRGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(p_0404e8), qargs=[qr[0], qr[1]], cargs=[])
qc.append(TGate(), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[1]], cargs=[])
qc.append(CRXGate(p_7a4196), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CRZGate(p_669081), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[1]], cargs=[])
qc.append(RZGate(p_92c9c5), qargs=[qr[1]], cargs=[])
qc.append(RZGate(p_6c0341), qargs=[qr[1]], cargs=[])
qc.append(CU1Gate(1.6723037552953224), qargs=[qr[0], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RZZGate(p_36ff61), qargs=[qr[0], qr[1]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_7a4196: 5.987304452123941, p_6c0341: 5.512260524440591, p_36ff61: 6.086884486572108, p_0404e8: 1.977559237989846, p_669081: 2.2498881927557752, p_92c9c5: 5.320621737498446, p_c06d9c: 6.163759533339787})
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=['rx', 'ry', 'rz', 'p', 'cx'],
    optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_19fe9244baf84c1e81fab7dec2653f0f = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_19fe9244baf84c1e81fab7dec2653f0f, shots=346).result().get_counts(qc)
RESULT = counts
