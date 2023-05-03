# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_7d7ce5 = Parameter('p_7d7ce5')
p_7291d9 = Parameter('p_7291d9')
p_f3c89a = Parameter('p_f3c89a')
p_8a1a82 = Parameter('p_8a1a82')
p_922074 = Parameter('p_922074')
p_6c1345 = Parameter('p_6c1345')
p_4bcda6 = Parameter('p_4bcda6')
p_45c2b7 = Parameter('p_45c2b7')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(3, name='qr')
cr = ClassicalRegister(3, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_7291d9), qargs=[qr[1]], cargs=[])
qc.append(CHGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[2], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(SGate(), qargs=[qr[2]], cargs=[])
qc.append(SdgGate(), qargs=[qr[1]], cargs=[])
qc.append(CRXGate(p_922074), qargs=[qr[0], qr[2]], cargs=[])
qc.append(SGate(), qargs=[qr[2]], cargs=[])
qc.append(CCXGate(), qargs=[qr[1], qr[0], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(RYYGate(p_4bcda6), qargs=[qr[1], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(SGate(), qargs=[qr[2]], cargs=[])
qc.append(ECRGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(RYYGate(p_7d7ce5), qargs=[qr[2], qr[0]], cargs=[])
subcircuit.append(U1Gate(p_45c2b7), qargs=[qr[0]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(RCCXGate(), qargs=[qr[1], qr[0], qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(SdgGate(), qargs=[qr[2]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[0], qr[2], qr[1]], cargs=[])
qc.append(CRZGate(p_6c1345), qargs=[qr[2], qr[1]], cargs=[])
qc.append(SGate(), qargs=[qr[2]], cargs=[])
qc.append(CRZGate(p_f3c89a), qargs=[qr[2], qr[1]], cargs=[])
qc.append(RYYGate(p_8a1a82), qargs=[qr[1], qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_7d7ce5: 0.2906326206587185, p_7291d9: 6.163759533339787, p_f3c89a: 0.05525155902669336, p_8a1a82: 3.2287759437031154, p_922074: 5.987304452123941, p_6c1345: 4.167661441102218, p_4bcda6: 1.6723037552953224, p_45c2b7: 1.4447770477048325})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION
from qiskit import Aer, transpile, execute
backend_6f28bf29d7b442e9844be570c6e07685 = Aer.get_backend('aer_simulator')
counts = execute(qc, backend=backend_6f28bf29d7b442e9844be570c6e07685,
    shots=489).result().get_counts(qc)
RESULT = counts
