# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(7, name='qr')
cr = ClassicalRegister(7, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=3, coupling_map=[[0,
    1], [0, 2], [0, 4], [0, 7], [1, 0], [1, 6], [2, 0], [2, 5], [3, 4], [4,
    0], [4, 3], [4, 8], [5, 2], [6, 1], [7, 0], [8, 4]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_69fd13e330344da28bb80aff3a7952db = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_69fd13e330344da28bb80aff3a7952db, shots=1959).result().get_counts(qc)
RESULT = counts
