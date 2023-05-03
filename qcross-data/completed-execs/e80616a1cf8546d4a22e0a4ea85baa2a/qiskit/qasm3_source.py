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
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0,
    1], [0, 2], [0, 8], [1, 0], [1, 4], [2, 0], [3, 7], [3, 8], [4, 1], [4,
    6], [5, 8], [6, 4], [6, 9], [7, 3], [7, 10], [8, 0], [8, 3], [8, 5], [9,
    6], [10, 7]])
# SECTION
# NAME: QASM_CONVERSION


from qiskit.qasm3 import loads, dumps
qc = loads(dumps(qc))

# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_53953120ee6b473ea2dd213ed6aca884 = Aer.get_backend('aer_simulator_density_matrix')
counts = execute(qc, backend=backend_53953120ee6b473ea2dd213ed6aca884, shots=7838).result().get_counts(qc)
RESULT = counts
