# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_5d06b8 = Parameter('p_5d06b8')
p_97a6da = Parameter('p_97a6da')
p_9bb2df = Parameter('p_9bb2df')
p_1f1cd8 = Parameter('p_1f1cd8')
p_38c5ce = Parameter('p_38c5ce')
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[7]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[8], qr[7]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[6], qr[4]], cargs=[])
qc.append(CCXGate(), qargs=[qr[3], qr[1], qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[5]], cargs=[])
qc.append(TGate(), qargs=[qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[6], qr[8]], cargs=[])
qc.append(RZGate(p_9bb2df), qargs=[qr[6]], cargs=[])
qc.append(SXGate(), qargs=[qr[5]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(CCXGate(), qargs=[qr[0], qr[1], qr[3]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[5], qr[0], qr[9], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[9], qr[5]], cargs=[])
qc.append(ZGate(), qargs=[qr[9]], cargs=[])
qc.append(CHGate(), qargs=[qr[4], qr[6]], cargs=[])
qc.append(CSXGate(), qargs=[qr[5], qr[9]], cargs=[])
qc.append(CRZGate(p_5d06b8), qargs=[qr[6], qr[5]], cargs=[])
qc.append(U2Gate(2.5163050709890156, 2.1276323672732023), qargs=[qr[5]],
    cargs=[])
qc.append(TGate(), qargs=[qr[9]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[1]], cargs=[])
qc.append(TGate(), qargs=[qr[2]], cargs=[])
qc.append(RZGate(5.014941143947427), qargs=[qr[6]], cargs=[])
qc.append(CRXGate(5.970852306777193), qargs=[qr[4], qr[6]], cargs=[])
qc.append(UGate(p_38c5ce, p_1f1cd8, p_97a6da), qargs=[qr[5]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_df4e3d = QuantumRegister(1, name='qr_df4e3d')
qc.add_register(qr_df4e3d)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_5d06b8: 2.586208953975239, p_97a6da: 2.271164628944128, p_9bb2df: 4.229610589867865, p_1f1cd8: 5.023617931957853, p_38c5ce: 5.080799300534071})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=['rx', 'ry', 'rz', 'p', 'cx'], optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_e66263693fb3474883c3541487e02935 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_e66263693fb3474883c3541487e02935, shots=5542).result().get_counts(qc)
RESULT = counts
