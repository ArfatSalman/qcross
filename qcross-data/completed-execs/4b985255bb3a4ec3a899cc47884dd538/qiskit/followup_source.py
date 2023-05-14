# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_bef792 = Parameter('p_bef792')
p_16c66f = Parameter('p_16c66f')
p_72801a = Parameter('p_72801a')
p_adfdc7 = Parameter('p_adfdc7')
p_a3b68b = Parameter('p_a3b68b')
p_35f264 = Parameter('p_35f264')
p_477e3c = Parameter('p_477e3c')
p_e721ac = Parameter('p_e721ac')
p_70b332 = Parameter('p_70b332')
p_8ead38 = Parameter('p_8ead38')
p_dc333a = Parameter('p_dc333a')
p_f7eb17 = Parameter('p_f7eb17')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_adfdc7), qargs=[qr[6], qr[3]], cargs=[])
qc.append(CRXGate(p_e721ac), qargs=[qr[1], qr[7]], cargs=[])
qc.append(CCXGate(), qargs=[qr[5], qr[9], qr[7]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[9]], cargs=[])
qc.append(XGate(), qargs=[qr[8]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[1], qr[6]], cargs=[])
qc.append(RZGate(p_70b332), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[4], qr[8]], cargs=[])
qc.append(CCXGate(), qargs=[qr[4], qr[9], qr[5]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[4], qr[0], qr[9]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[7], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(CRZGate(p_35f264), qargs=[qr[1], qr[2]], cargs=[])
qc.append(U2Gate(p_a3b68b, p_72801a), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[9]], cargs=[])
qc.append(TGate(), qargs=[qr[8]], cargs=[])
qc.append(RZGate(p_bef792), qargs=[qr[1]], cargs=[])
qc.append(CRXGate(p_8ead38), qargs=[qr[7], qr[1]], cargs=[])
qc.append(UGate(p_16c66f, p_477e3c, p_f7eb17), qargs=[qr[2]], cargs=[])
qc.append(ECRGate(), qargs=[qr[4], qr[8]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[8]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[7]], cargs=[])
qc.append(RZGate(p_dc333a), qargs=[qr[5]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_bef792: 5.014941143947427, p_16c66f: 5.080799300534071, p_72801a: 2.1276323672732023, p_adfdc7: 4.2641612072511235, p_a3b68b: 2.5163050709890156, p_35f264: 2.586208953975239, p_477e3c: 5.023617931957853, p_e721ac: 5.987304452123941, p_70b332: 4.229610589867865, p_8ead38: 5.970852306777193, p_dc333a: 3.6614081973587154, p_f7eb17: 2.271164628944128})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION
from qiskit import Aer, transpile, execute
backend_67d021ee0afb4011b293c27140d81fb4 = Aer.get_backend(
    'statevector_simulator')
counts = execute(qc, backend=backend_67d021ee0afb4011b293c27140d81fb4,
    shots=5542).result().get_counts(qc)
RESULT = counts
