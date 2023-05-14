# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(9, name='qr')
cr = ClassicalRegister(9, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[3], qr[7]], cargs=[])
qc.append(CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245,
    5.987304452123941), qargs=[qr[4], qr[6]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=3, coupling_map=[[0, 1], [0, 8], [1, 0], [1, 3], [2, 10], [2, 11], [3, 1], [3, 7], [3, 9], [4, 8], [5, 10], [6, 7], [7, 3], [7, 6], [7, 10], [8, 0], [8, 4], [9, 3], [10, 2], [10, 5], [10, 7], [11, 2]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_d5ffad46440c44c2b44e268be9059e08 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_d5ffad46440c44c2b44e268be9059e08, shots=3919).result().get_counts(qc)
RESULT = counts
