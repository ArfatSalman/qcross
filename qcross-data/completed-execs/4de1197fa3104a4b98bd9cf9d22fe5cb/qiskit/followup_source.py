# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_4d1002 = Parameter('p_4d1002')
p_95d4c5 = Parameter('p_95d4c5')
p_c4621c = Parameter('p_c4621c')
p_7c06d6 = Parameter('p_7c06d6')
p_1cef4d = Parameter('p_1cef4d')
p_643384 = Parameter('p_643384')
p_0fdd04 = Parameter('p_0fdd04')
p_27af66 = Parameter('p_27af66')
p_c93870 = Parameter('p_c93870')
p_acd0b1 = Parameter('p_acd0b1')
p_d935d2 = Parameter('p_d935d2')
p_56ef16 = Parameter('p_56ef16')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(4, name='qr')
cr = ClassicalRegister(4, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_95d4c5), qargs=[qr[1]], cargs=[])
qc.append(RZZGate(p_c93870), qargs=[qr[2], qr[3]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(CUGate(p_0fdd04, p_c4621c, p_7c06d6, p_1cef4d), qargs=[qr[0], qr[2]], cargs=[])
qc.append(CU1Gate(p_d935d2), qargs=[qr[3], qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[3], qr[2]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(U1Gate(4.8767543643948805), qargs=[qr[0]], cargs=[])
subcircuit.append(SwapGate(), qargs=[qr[2], qr[0]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CHGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[3], qr[0], qr[1], qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[3], qr[1], qr[0], qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[2]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[1], qr[0], qr[3]], cargs=[])
qc.append(RYYGate(p_acd0b1), qargs=[qr[2], qr[0]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[2], qr[3], qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_643384), qargs=[qr[0], qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[2], qr[0], qr[3]], cargs=[])
qc.append(RYYGate(p_56ef16), qargs=[qr[2], qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(CU1Gate(p_27af66), qargs=[qr[0], qr[3]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CRXGate(p_4d1002), qargs=[qr[2], qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_4d1002: 5.94477504571567, p_95d4c5: 6.163759533339787, p_c4621c: 5.897054719225356, p_7c06d6: 2.3864521352475245, p_1cef4d: 5.987304452123941, p_643384: 2.9790366726895714, p_0fdd04: 0.5112149185250571, p_27af66: 3.2142159669963557, p_c93870: 4.066449154047175, p_acd0b1: 1.740253089260498, p_d935d2: 5.154187354656876, p_56ef16: 5.398622178940033})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_e2f0f29e9a064e508e4b350702b5bb29 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_e2f0f29e9a064e508e4b350702b5bb29, shots=692).result().get_counts(qc)
RESULT = counts
