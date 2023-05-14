# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[6], qr[3]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[1], qr[7]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0,
    1], [0, 8], [0, 10], [0, 12], [1, 0], [1, 4], [1, 5], [2, 8], [3, 6], [
    3, 12], [4, 1], [4, 7], [4, 11], [5, 1], [6, 3], [6, 12], [7, 4], [8, 0
    ], [8, 2], [9, 12], [10, 0], [11, 4], [12, 0], [12, 3], [12, 6], [12, 9]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_8fc325ec7b914082a77200be5ecaa8d2 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_8fc325ec7b914082a77200be5ecaa8d2, shots=5542).result().get_counts(qc)
RESULT = counts
