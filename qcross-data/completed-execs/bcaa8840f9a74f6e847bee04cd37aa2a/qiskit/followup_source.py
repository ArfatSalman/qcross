# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_42891c = Parameter('p_42891c')
p_92144e = Parameter('p_92144e')
p_cbf8a5 = Parameter('p_cbf8a5')
p_9f3b29 = Parameter('p_9f3b29')
p_914ffd = Parameter('p_914ffd')
p_155411 = Parameter('p_155411')
p_4ab831 = Parameter('p_4ab831')
p_e5e350 = Parameter('p_e5e350')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(2, name='qr')
cr = ClassicalRegister(2, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(SXGate(), qargs=[qr[1]], cargs=[])
subcircuit.append(SXGate(), qargs=[qr[1]], cargs=[])
subcircuit.append(RYGate(5.398622178940033), qargs=[qr[0]], cargs=[])
subcircuit.append(XGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(CU3Gate(1.3471739101750193, 3.2142159669963557, 2.852678572380205), qargs=[qr[0], qr[1]], cargs=[])
subcircuit.append(U1Gate(2.3568871696687452), qargs=[qr[1]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(RZZGate(6.163759533339787), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(ECRGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(p_92144e), qargs=[qr[0], qr[1]], cargs=[])
qc.append(TGate(), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[1]], cargs=[])
qc.append(CRXGate(p_e5e350), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CRZGate(p_4ab831), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[1]], cargs=[])
qc.append(RZGate(p_914ffd), qargs=[qr[1]], cargs=[])
qc.append(RZGate(5.512260524440591), qargs=[qr[1]], cargs=[])
qc.append(CU1Gate(p_155411), qargs=[qr[0], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RZZGate(6.086884486572108), qargs=[qr[0], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(RYYGate(p_42891c), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[1]], cargs=[])
qc.append(RZGate(p_9f3b29), qargs=[qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(p_cbf8a5), qargs=[qr[1], qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[1], qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_42891c: 3.3705408413231095, p_92144e: 1.977559237989846, p_cbf8a5: 5.167261531657622, p_9f3b29: 5.190931186022931, p_914ffd: 5.320621737498446, p_155411: 1.6723037552953224, p_4ab831: 2.2498881927557752, p_e5e350: 5.987304452123941})
# SECTION
# NAME: QASM_CONVERSION

qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=['ccx', 'h'], optimization_level=2,
    coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_bae7ef5edd8a4828a2ec3ef0ff3041bd = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_bae7ef5edd8a4828a2ec3ef0ff3041bd, shots=346).result().get_counts(qc)
RESULT = counts
