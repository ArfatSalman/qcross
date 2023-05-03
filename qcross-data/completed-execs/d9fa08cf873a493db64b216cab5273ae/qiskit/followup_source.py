# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_a95533 = Parameter('p_a95533')
p_ec403b = Parameter('p_ec403b')
p_4c0f0f = Parameter('p_4c0f0f')
p_6100f8 = Parameter('p_6100f8')
p_07e86a = Parameter('p_07e86a')
p_55c5f0 = Parameter('p_55c5f0')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_4c0f0f), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_6100f8), qargs=[qr[6], qr[3]], cargs=[])
qc.append(CRXGate(p_55c5f0), qargs=[qr[1], qr[7]], cargs=[])
qc.append(CCXGate(), qargs=[qr[5], qr[9], qr[7]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[9]], cargs=[])
qc.append(XGate(), qargs=[qr[8]], cargs=[])
qc.append(CRZGate(p_07e86a), qargs=[qr[1], qr[6]], cargs=[])
qc.append(RZGate(p_ec403b), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[4], qr[8]], cargs=[])
qc.append(CCXGate(), qargs=[qr[4], qr[9], qr[5]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[4], qr[0], qr[9]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[7], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(CRZGate(p_a95533), qargs=[qr[1], qr[2]], cargs=[])
qc.append(U2Gate(2.5163050709890156, 2.1276323672732023), qargs=[qr[2]],
    cargs=[])
qc.append(TGate(), qargs=[qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[9]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_a95533: 2.586208953975239, p_ec403b: 4.229610589867865, p_4c0f0f: 6.163759533339787,
    p_6100f8: 4.2641612072511235,
    p_07e86a: 4.167661441102218,
    p_55c5f0: 5.987304452123941,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=[[0, 1], [0, 2], [0, 3], [0, 4], [0, 9], [1, 0], [1, 6], [2, 0], [2, 5], [2, 7], [3, 0], [4, 0], [4, 8], [4, 10], [5, 2], [5, 11], [6, 1], [7, 2], [8, 4], [9, 0], [10, 4], [11, 5]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_def3bb70187c4addb5b46388fb7398ca = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_def3bb70187c4addb5b46388fb7398ca, shots=5542).result().get_counts(qc)
RESULT = counts
