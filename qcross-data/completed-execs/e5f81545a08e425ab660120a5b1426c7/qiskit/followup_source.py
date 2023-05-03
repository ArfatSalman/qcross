# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_566c5c = Parameter('p_566c5c')
p_d15eb0 = Parameter('p_d15eb0')
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_566c5c), qargs=[qr[1]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[3]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[1], qr[3]], cargs=[])
qc.append(CRXGate(2.0099472182748075), qargs=[qr[4], qr[1]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(CRZGate(1.0296448789776642), qargs=[qr[1], qr[4]], cargs=[])
qc.append(CHGate(), qargs=[qr[2], qr[4]], cargs=[])
qc.append(RYYGate(p_d15eb0), qargs=[qr[0], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[4]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_566c5c: 6.163759533339787, p_d15eb0: 1.6723037552953224})
# SECTION
# NAME: QASM_CONVERSION

qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_36a013b596b44a2293d72db9eaacd069 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_36a013b596b44a2293d72db9eaacd069, shots=979).result().get_counts(qc)
RESULT = counts
