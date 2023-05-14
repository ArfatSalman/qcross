# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_f80351 = Parameter('p_f80351')
p_cb603f = Parameter('p_cb603f')
p_9a6428 = Parameter('p_9a6428')
p_14882b = Parameter('p_14882b')
p_229656 = Parameter('p_229656')
p_d83aa6 = Parameter('p_d83aa6')
p_1e7763 = Parameter('p_1e7763')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_1e7763), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_cb603f), qargs=[qr[6], qr[3]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(SXdgGate(), qargs=[qr[5]], cargs=[])
subcircuit.append(DCXGate(), qargs=[qr[4], qr[7]], cargs=[])
subcircuit.append(CU3Gate(4.2220417977098705, 1.672427069032094, 2.447994042088217), qargs=[qr[5], qr[3]], cargs=[])
subcircuit.append(CUGate(4.783709962939332, 4.509839071764646, 3.631024984774394, 2.3799139963609854), qargs=[qr[7], qr[3]], cargs=[])
subcircuit.append(PhaseGate(5.949169145894372), qargs=[qr[2]], cargs=[])
subcircuit.append(CSXGate(), qargs=[qr[1], qr[7]], cargs=[])
subcircuit.append(CXGate(), qargs=[qr[2], qr[5]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CRXGate(5.987304452123941), qargs=[qr[1], qr[7]], cargs=[])
qc.append(CCXGate(), qargs=[qr[5], qr[9], qr[7]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[9]], cargs=[])
qc.append(XGate(), qargs=[qr[8]], cargs=[])
qc.append(CRZGate(p_229656), qargs=[qr[1], qr[6]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[4], qr[8]], cargs=[])
qc.append(CCXGate(), qargs=[qr[4], qr[9], qr[5]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[4], qr[0], qr[9]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[7], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(CRZGate(p_9a6428), qargs=[qr[1], qr[2]], cargs=[])
qc.append(U2Gate(p_14882b, p_d83aa6), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[9]], cargs=[])
qc.append(TGate(), qargs=[qr[8]], cargs=[])
qc.append(RZGate(5.014941143947427), qargs=[qr[1]], cargs=[])
qc.append(CRXGate(p_f80351), qargs=[qr[7], qr[1]], cargs=[])
qc.append(UGate(5.080799300534071, 5.023617931957853, 2.271164628944128), qargs=[qr[2]], cargs=[])
qc.append(ECRGate(), qargs=[qr[4], qr[8]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[8]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_3f20d8 = QuantumRegister(7, name='qr_3f20d8')
subcircuit.add_register(qr_3f20d8)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_f80351: 5.970852306777193, p_cb603f: 4.2641612072511235, p_9a6428: 2.586208953975239, p_14882b: 2.5163050709890156, p_229656: 4.167661441102218, p_d83aa6: 2.1276323672732023, p_1e7763: 6.163759533339787})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION
from qiskit import Aer, transpile, execute
backend_fe5b80cdca6f4153abf919e4d7b0e00a = Aer.get_backend(
    'statevector_simulator')
counts = execute(qc, backend=backend_fe5b80cdca6f4153abf919e4d7b0e00a,
    shots=5542).result().get_counts(qc)
RESULT = counts
