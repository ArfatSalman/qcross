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
p_897886 = Parameter('p_897886')
p_0477e2 = Parameter('p_0477e2')
p_343721 = Parameter('p_343721')
p_837a0a = Parameter('p_837a0a')
p_31e933 = Parameter('p_31e933')
p_b58743 = Parameter('p_b58743')
p_a36cb0 = Parameter('p_a36cb0')
p_966369 = Parameter('p_966369')
p_a7959d = Parameter('p_a7959d')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(9, name='qr')
cr = ClassicalRegister(9, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_343721), qargs=[qr[8]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[4]], cargs=[])
qc.append(CUGate(p_31e933, p_897886, p_a36cb0, p_a7959d), qargs=[qr[0], qr[
    6]], cargs=[])
qc.append(SdgGate(), qargs=[qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[8], qr[7], qr[5]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[5]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[8]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[3], qr[2], qr[0]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(CU1Gate(p_837a0a), qargs=[qr[8], qr[3]], cargs=[])
qc.append(CRZGate(p_b58743), qargs=[qr[5], qr[8]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[7]], cargs=[])
qc.append(CHGate(), qargs=[qr[6], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[3], qr[0]], cargs=[])
qc.append(CRZGate(p_0477e2), qargs=[qr[1], qr[2]], cargs=[])
qc.append(U2Gate(2.5163050709890156, p_966369), qargs=[qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_897886: 5.897054719225356,
    p_0477e2: 2.586208953975239,
    p_343721: 6.163759533339787,
    p_837a0a: 3.2142159669963557,
    p_31e933: 0.5112149185250571,
    p_b58743: 1.4112277317699358,
    p_a36cb0: 2.3864521352475245,
    p_966369: 2.1276323672732023,
    p_a7959d: 5.987304452123941,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 2], [0, 4], [0, 5], [1, 0], [2, 0], [2, 4], [2, 6], [3, 8], [3, 10], [4, 0], [4, 2], [4, 7], [4, 8], [5, 0], [6, 2], [7, 4], [8, 3], [8, 4], [8, 9], [9, 8], [10, 3]])
# SECTION
# NAME: QASM_CONVERSION

qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_ace3aba85f684a3596680c33a6280c71 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_ace3aba85f684a3596680c33a6280c71, shots=3919).result().get_counts(qc)
RESULT = counts
