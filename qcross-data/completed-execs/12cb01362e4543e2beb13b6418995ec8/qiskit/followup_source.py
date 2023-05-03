# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS
# SECTION
# NAME: PARAMETERS
p_7ebac6 = Parameter('p_7ebac6')
p_02fa5f = Parameter('p_02fa5f')
p_68bc2a = Parameter('p_68bc2a')
p_b1a917 = Parameter('p_b1a917')
p_d2b847 = Parameter('p_d2b847')
p_98866e = Parameter('p_98866e')
p_896a7d = Parameter('p_896a7d')
p_583e59 = Parameter('p_583e59')
p_eef840 = Parameter('p_eef840')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(6, name='qr')
cr = ClassicalRegister(6, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(RZGate(p_896a7d), qargs=[qr[2]], cargs=[])
subcircuit.append(TGate(), qargs=[qr[1]], cargs=[])
subcircuit.append(CUGate(p_98866e, p_d2b847, 5.631160518436971, p_02fa5f),
    qargs=[qr[0], qr[3]], cargs=[])
subcircuit.append(TGate(), qargs=[qr[2]], cargs=[])
subcircuit.append(RZXGate(p_583e59), qargs=[qr[4], qr[0]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(RZGate(6.163759533339787), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_eef840), qargs=[qr[2], qr[4]], cargs=[])
qc.append(CUGate(p_68bc2a, p_b1a917, p_7ebac6, 5.987304452123941), qargs=[
    qr[2], qr[3]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[4], qr[0], qr[2]], cargs=[])
qc.append(CCXGate(), qargs=[qr[1], qr[5], qr[0]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[4], qr[3], qr[5], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[5], qr[3], qr[4]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_7ebac6: 2.3864521352475245,
    p_02fa5f: 2.9151388486514547,
    p_68bc2a: 0.5112149185250571,
    p_b1a917: 5.897054719225356,
    p_d2b847: 2.696266694818697,
    p_98866e: 4.229610589867865,
    p_896a7d: 3.672121211148789,
    p_583e59: 4.563562108824195,
    p_eef840: 4.2641612072511235,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_f43d67378d1d49b4ae3f343320ccf759 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_f43d67378d1d49b4ae3f343320ccf759, shots=1385).result().get_counts(qc)
RESULT = counts
