# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=['rx', 'ry', 'rz', 'p', 'cx'],
    optimization_level=2, coupling_map=[[0, 1], [0, 2], [0, 3], [1, 0], [1,
    5], [2, 0], [2, 4], [3, 0], [4, 2], [5, 1], [5, 6], [6, 5]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_042e39bee4934830ab8f2ece6142f83f = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_042e39bee4934830ab8f2ece6142f83f, shots=979).result().get_counts(qc)
RESULT = counts
