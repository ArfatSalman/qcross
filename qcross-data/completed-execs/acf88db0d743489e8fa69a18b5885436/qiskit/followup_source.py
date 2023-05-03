# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[6]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0,
    1], [0, 5], [1, 0], [1, 2], [1, 8], [2, 1], [3, 9], [4, 9], [5, 0], [5,
    6], [6, 5], [7, 8], [7, 9], [8, 1], [8, 7], [8, 10], [9, 3], [9, 4], [9,
    7], [10, 8]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_19c1625ce7504b12b3b7437d03365cec = Aer.get_backend('aer_simulator')
counts = execute(qc, backend=backend_19c1625ce7504b12b3b7437d03365cec, shots=2771).result().get_counts(qc)
RESULT = counts
