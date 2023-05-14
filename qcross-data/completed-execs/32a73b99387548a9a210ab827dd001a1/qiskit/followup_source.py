# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_fc0ce7 = Parameter('p_fc0ce7')
p_532c13 = Parameter('p_532c13')
p_96cba0 = Parameter('p_96cba0')
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[0]], cargs=[])
qc.append(CRZGate(p_fc0ce7), qargs=[qr[7], qr[0]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[5], qr[9]], cargs=[])
qc.append(CCXGate(), qargs=[qr[3], qr[4], qr[9]], cargs=[])
qc.append(ZGate(), qargs=[qr[8]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
qc.append(XGate(), qargs=[qr[6]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[5], qr[7]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[5]], cargs=[])
qc.append(SXGate(), qargs=[qr[8]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[6]], cargs=[])
qc.append(CCXGate(), qargs=[qr[1], qr[4], qr[3]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[8], qr[1], qr[2], qr[4]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[8]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[9], qr[5]], cargs=[])
qc.append(CSXGate(), qargs=[qr[8], qr[2]], cargs=[])
qc.append(CRZGate(p_96cba0), qargs=[qr[5], qr[8]], cargs=[])
qc.append(U2Gate(p_532c13, 2.1276323672732023), qargs=[qr[8]], cargs=[])
qc.append(TGate(), qargs=[qr[2]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[4]], cargs=[])
qc.append(TGate(), qargs=[qr[6]], cargs=[])
qc.append(RZGate(5.014941143947427), qargs=[qr[5]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_0b8718 = QuantumRegister(8, name='qr_0b8718')
qc.add_register(qr_0b8718)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_fc0ce7: 4.2641612072511235, p_532c13: 2.5163050709890156, p_96cba0: 2.586208953975239})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_ce55759ea2004299966bded9fd088396 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_ce55759ea2004299966bded9fd088396, shots=5542).result().get_counts(qc)
RESULT = counts
