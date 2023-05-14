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
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0,
    1], [0, 7], [0, 10], [1, 0], [1, 3], [1, 5], [1, 9], [2, 5], [3, 1], [4,
    5], [5, 1], [5, 2], [5, 4], [5, 8], [6, 8], [7, 0], [8, 5], [8, 6], [9,
    1], [10, 0]])
# SECTION
# NAME: QASM_CONVERSION


from qiskit.qasm3 import loads, dumps
qc = loads(dumps(qc))

# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_a7d00e5ee8404c9e870cfafc811c8a06 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_a7d00e5ee8404c9e870cfafc811c8a06, shots=3919).result().get_counts(qc)
RESULT = counts
