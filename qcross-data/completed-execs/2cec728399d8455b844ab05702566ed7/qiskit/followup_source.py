# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_595a74 = Parameter('p_595a74')
p_a57db2 = Parameter('p_a57db2')
p_2ae583 = Parameter('p_2ae583')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(9, name='qr')
cr = ClassicalRegister(9, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[8]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[4]], cargs=[])
qc.append(CUGate(p_a57db2, p_2ae583, p_595a74, 5.987304452123941), qargs=[qr[0], qr[6]], cargs=[])
qc.append(SdgGate(), qargs=[qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[8], qr[7], qr[5]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[5]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[8]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[3], qr[2], qr[0]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_595a74: 2.3864521352475245, p_a57db2: 0.5112149185250571, p_2ae583: 5.897054719225356})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 5], [1, 0], [1, 3], [1, 6], [2, 3], [3, 1], [3, 2], [3, 8], [3, 10], [4, 8], [4, 9], [5, 0], [6, 1], [7, 8], [8, 3], [8, 4], [8, 7], [9, 4], [10, 3]])
# SECTION
# NAME: EXECUTION
from qiskit import Aer, transpile, execute
backend_ae942b66b2504f63b04412c870dbb1d4 = Aer.get_backend(
    'aer_simulator_density_matrix')
counts = execute(qc, backend=backend_ae942b66b2504f63b04412c870dbb1d4,
    shots=3919).result().get_counts(qc)
RESULT = counts
