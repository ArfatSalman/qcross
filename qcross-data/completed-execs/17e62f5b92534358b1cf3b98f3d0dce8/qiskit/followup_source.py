# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_efcc68 = Parameter('p_efcc68')
p_2061b2 = Parameter('p_2061b2')
p_536d06 = Parameter('p_536d06')
p_732b5a = Parameter('p_732b5a')
p_dbfaed = Parameter('p_dbfaed')
p_28ab37 = Parameter('p_28ab37')
p_c8704d = Parameter('p_c8704d')
p_77100f = Parameter('p_77100f')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_536d06), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_dbfaed), qargs=[qr[6], qr[3]], cargs=[])
qc.append(CRXGate(p_2061b2), qargs=[qr[1], qr[7]], cargs=[])
qc.append(CCXGate(), qargs=[qr[5], qr[9], qr[7]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[9]], cargs=[])
qc.append(XGate(), qargs=[qr[8]], cargs=[])
qc.append(CRZGate(p_28ab37), qargs=[qr[1], qr[6]], cargs=[])
qc.append(RZGate(p_efcc68), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[4], qr[8]], cargs=[])
qc.append(CCXGate(), qargs=[qr[4], qr[9], qr[5]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[4], qr[0], qr[9]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[7], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(CRZGate(p_77100f), qargs=[qr[1], qr[2]], cargs=[])
qc.append(U2Gate(p_c8704d, p_732b5a), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[0]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(SXdgGate(), qargs=[qr[9]], cargs=[])
qc.append(TGate(), qargs=[qr[8]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_78a91c = QuantumRegister(2, name='qr_78a91c')
qc.add_register(qr_78a91c)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_efcc68: 4.229610589867865, p_2061b2: 5.987304452123941, p_536d06: 6.163759533339787, p_732b5a: 2.1276323672732023, p_dbfaed: 4.2641612072511235, p_28ab37: 4.167661441102218, p_c8704d: 2.5163050709890156, p_77100f: 2.586208953975239})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_3430762fa9b4415492294df71d8608a8 = Aer.get_backend('aer_simulator')
counts = execute(qc, backend=backend_3430762fa9b4415492294df71d8608a8, shots=5542).result().get_counts(qc)
RESULT = counts
