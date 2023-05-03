# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(11, name='qr')
cr = ClassicalRegister(11, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[6], qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=['cx', 'h', 's', 't'], optimization_level=3,
    coupling_map=[[0, 1], [1, 0], [1, 6], [1, 7], [1, 10], [1, 11], [2, 3],
    [2, 6], [3, 2], [3, 6], [3, 9], [4, 7], [4, 8], [5, 7], [5, 12], [5, 13
    ], [6, 1], [6, 2], [6, 3], [7, 1], [7, 4], [7, 5], [7, 9], [8, 4], [8, 
    11], [9, 3], [9, 7], [9, 10], [10, 1], [10, 9], [11, 1], [11, 8], [12, 
    5], [13, 5]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_9b40b4c9f52444d68cd06c836447126f = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_9b40b4c9f52444d68cd06c836447126f, shots=7838).result().get_counts(qc)
RESULT = counts
