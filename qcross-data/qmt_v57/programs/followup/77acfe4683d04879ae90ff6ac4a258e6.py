# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr_1 = QuantumRegister(3, name='qr_1')
cr_1 = ClassicalRegister(3, name='cr_1')
qc_1 = QuantumCircuit(qr_1, cr_1, name='qc_1')


qc_1.append(PhaseGate(3.565985138018942), qargs=[qr_1[4]], cargs=[])

qr_2 = QuantumRegister(3, name='qr_2')
cr_2 = ClassicalRegister(3, name='cr_2')
qc_2 = QuantumCircuit(qr_2, cr_2, name='qc_2')


qc_2.append(RXXGate(2.061982306423713), qargs=[qr_2[0], qr_2[2]], cargs=[])
qc_2.append(RVGate(1.8242043393661458, 4.419776500558505, 0.43416461978491694), qargs=[qr_2[2]], cargs=[])
qc_2.append(SGate(), qargs=[qr_2[0]], cargs=[])
qc_2.append(RXXGate(0.020795531533047435), qargs=[qr_2[1], qr_2[0]], cargs=[])# SECTION
# NAME: MEASUREMENT

qc_1.measure(qr_1, cr_1)
qc_2.measure(qr_2, cr_2)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc_1 = transpile(qc_1, basis_gates=['rx', 'ry', 'rz', 'p', 'cx'], optimization_level=0, coupling_map=[[0, 1], [0, 8], [1, 0], [1, 3], [1, 4], [1, 7], [2, 4], [3, 1], [4, 1], [4, 2], [4, 6], [5, 8], [6, 4], [7, 1], [8, 0], [8, 5]])
qc_2 = transpile(qc_2, basis_gates=['rx', 'ry', 'rz', 'p', 'cx'], optimization_level=0, coupling_map=[[0, 1], [0, 8], [1, 0], [1, 3], [1, 4], [1, 7], [2, 4], [3, 1], [4, 1], [4, 2], [4, 6], [5, 8], [6, 4], [7, 1], [8, 0], [8, 5]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_4ee926a61bb64c599cab9507d39ca0b0 = Aer.get_backend('qasm_simulator')
counts_1 = execute(qc_1, backend=backend_4ee926a61bb64c599cab9507d39ca0b0, shots=1385).result().get_counts(qc_1)
counts_2 = execute(qc_2, backend=backend_4ee926a61bb64c599cab9507d39ca0b0, shots=1385).result().get_counts(qc_2)
RESULT = [counts_1, counts_2]
