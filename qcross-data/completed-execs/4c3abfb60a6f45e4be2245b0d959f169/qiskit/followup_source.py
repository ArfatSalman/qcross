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
p_478f57 = Parameter('p_478f57')
p_be710f = Parameter('p_be710f')
p_fb13a2 = Parameter('p_fb13a2')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_fb13a2), qargs=[qr[6], qr[3]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[1], qr[7]], cargs=[])
qc.append(CCXGate(), qargs=[qr[5], qr[9], qr[7]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[9]], cargs=[])
qc.append(XGate(), qargs=[qr[8]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[1], qr[6]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[4], qr[8]], cargs=[])
qc.append(CCXGate(), qargs=[qr[4], qr[9], qr[5]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[4], qr[0], qr[9]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[7], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(CRZGate(2.586208953975239), qargs=[qr[1], qr[2]], cargs=[])
qc.append(U2Gate(p_be710f, 2.1276323672732023), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[9]], cargs=[])
qc.append(TGate(), qargs=[qr[8]], cargs=[])
qc.append(RZGate(5.014941143947427), qargs=[qr[1]], cargs=[])
qc.append(CRXGate(5.970852306777193), qargs=[qr[7], qr[1]], cargs=[])
qc.append(UGate(5.080799300534071, p_478f57, 2.271164628944128), qargs=[qr[
    2]], cargs=[])
qc.append(ECRGate(), qargs=[qr[4], qr[8]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[8]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[7]], cargs=[])
qc.append(RZGate(3.6614081973587154), qargs=[qr[5]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_478f57: 5.023617931957853,
    p_be710f: 2.5163050709890156,
    p_fb13a2: 4.2641612072511235,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=['rx', 'ry', 'rz', 'p', 'cx'], optimization_level=0, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_884734b152914aebb2d16095a829aab5 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_884734b152914aebb2d16095a829aab5, shots=5542).result().get_counts(qc)
RESULT = counts
