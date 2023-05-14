# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_a2b8a1 = Parameter('p_a2b8a1')
p_c71b89 = Parameter('p_c71b89')
p_109b12 = Parameter('p_109b12')
p_61c866 = Parameter('p_61c866')
p_55837c = Parameter('p_55837c')
p_bcdc65 = Parameter('p_bcdc65')
p_ad1c79 = Parameter('p_ad1c79')
p_0e4f1e = Parameter('p_0e4f1e')
p_708df6 = Parameter('p_708df6')
p_b373ee = Parameter('p_b373ee')
p_89d7ca = Parameter('p_89d7ca')
p_55cda5 = Parameter('p_55cda5')
p_1d0fad = Parameter('p_1d0fad')
p_a3b617 = Parameter('p_a3b617')
p_a0a530 = Parameter('p_a0a530')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_1d0fad), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_708df6), qargs=[qr[6], qr[3]], cargs=[])
qc.append(CRXGate(p_0e4f1e), qargs=[qr[1], qr[7]], cargs=[])
qc.append(CCXGate(), qargs=[qr[5], qr[9], qr[7]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(U2Gate(p_a0a530, p_a3b617), qargs=[qr[0]], cargs=[])
subcircuit.append(SXdgGate(), qargs=[qr[4]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[9]], cargs=[])
qc.append(XGate(), qargs=[qr[8]], cargs=[])
qc.append(CRZGate(p_61c866), qargs=[qr[1], qr[6]], cargs=[])
qc.append(RZGate(p_55cda5), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[4], qr[8]], cargs=[])
qc.append(CCXGate(), qargs=[qr[4], qr[9], qr[5]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[4], qr[0], qr[9]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[7], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(CRZGate(p_c71b89), qargs=[qr[1], qr[2]], cargs=[])
qc.append(U2Gate(p_b373ee, p_ad1c79), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[9]], cargs=[])
qc.append(TGate(), qargs=[qr[8]], cargs=[])
qc.append(RZGate(p_a2b8a1), qargs=[qr[1]], cargs=[])
qc.append(CRXGate(p_89d7ca), qargs=[qr[7], qr[1]], cargs=[])
qc.append(UGate(p_55837c, p_bcdc65, p_109b12), qargs=[qr[2]], cargs=[])
qc.append(ECRGate(), qargs=[qr[4], qr[8]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_a2b8a1: 5.014941143947427, p_c71b89: 2.586208953975239, p_109b12: 2.271164628944128, p_61c866: 4.167661441102218, p_55837c: 5.080799300534071, p_bcdc65: 5.023617931957853, p_ad1c79: 2.1276323672732023, p_0e4f1e: 5.987304452123941, p_708df6: 4.2641612072511235, p_b373ee: 2.5163050709890156, p_89d7ca: 5.970852306777193, p_55cda5: 4.229610589867865, p_1d0fad: 6.163759533339787,
    p_a3b617: 1.0052392769301404,
    p_a0a530: 0.25812405723927917,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_39259d6170b34542bef41ff28826bae9 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_39259d6170b34542bef41ff28826bae9, shots=5542).result().get_counts(qc)
RESULT = counts
