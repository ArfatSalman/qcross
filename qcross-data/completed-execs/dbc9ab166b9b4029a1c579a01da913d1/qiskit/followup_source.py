# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_c69e12 = Parameter('p_c69e12')
p_23fe7b = Parameter('p_23fe7b')
p_3b83fb = Parameter('p_3b83fb')
p_d5ab30 = Parameter('p_d5ab30')
p_9f1173 = Parameter('p_9f1173')
p_8cc75e = Parameter('p_8cc75e')
p_ed89c2 = Parameter('p_ed89c2')
p_f1fd0a = Parameter('p_f1fd0a')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(7, name='qr')
cr = ClassicalRegister(7, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_f1fd0a), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[3]], cargs=[])
qc.append(CRXGate(2.0099472182748075), qargs=[qr[2], qr[5]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(TGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(IGate(), qargs=[qr[3]], cargs=[])
subcircuit.append(PhaseGate(0.4827903095199283), qargs=[qr[6]], cargs=[])
subcircuit.append(RZGate(1.2484842640635918), qargs=[qr[0]], cargs=[])
subcircuit.append(CRZGate(4.747288222618085), qargs=[qr[1], qr[3]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(C3SXGate(), qargs=[qr[6], qr[0], qr[1], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[4], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[2], qr[1], qr[5]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(ECRGate(), qargs=[qr[6], qr[3]], cargs=[])
qc.append(SdgGate(), qargs=[qr[6]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[2], qr[5], qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[1]], cargs=[])
qc.append(RZGate(p_9f1173), qargs=[qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[2], qr[1], qr[3]], cargs=[])
qc.append(CU1Gate(3.2142159669963557), qargs=[qr[4], qr[0]], cargs=[])
qc.append(CRXGate(p_d5ab30), qargs=[qr[4], qr[6]], cargs=[])
qc.append(CHGate(), qargs=[qr[4], qr[0]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[0], qr[3], qr[4]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[5]], cargs=[])
qc.append(CRZGate(p_3b83fb), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CU1Gate(p_8cc75e), qargs=[qr[1], qr[4]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[0], qr[5], qr[4]], cargs=[])
qc.append(CRZGate(p_23fe7b), qargs=[qr[6], qr[2]], cargs=[])
qc.append(U2Gate(p_c69e12, p_ed89c2), qargs=[qr[2]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_ef5c94 = QuantumRegister(8, name='qr_ef5c94')
qc.add_register(qr_ef5c94)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_c69e12: 2.5163050709890156, p_23fe7b: 2.586208953975239, p_3b83fb: 4.833923139882297, p_d5ab30: 5.94477504571567, p_9f1173: 4.229610589867865, p_8cc75e: 4.028174522740928, p_ed89c2: 2.1276323672732023, p_f1fd0a: 6.163759533339787})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_b53c55c4ad6a4f209d60a41090fe6f34 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_b53c55c4ad6a4f209d60a41090fe6f34, shots=1959).result().get_counts(qc)
RESULT = counts
