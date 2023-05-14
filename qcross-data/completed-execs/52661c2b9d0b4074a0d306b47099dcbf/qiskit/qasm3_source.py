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


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: QASM_CONVERSION


from qiskit.qasm3 import loads, dumps
qc = loads(dumps(qc))

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=['rx', 'ry', 'rz', 'p', 'cx'], optimization_level=2, coupling_map=[[0, 1], [0, 7], [0, 10], [1, 0], [1, 3], [1, 5], [1, 9], [2, 5], [3, 1], [4, 5], [5, 1], [5, 2], [5, 4], [5, 8], [6, 8], [7, 0], [8, 5], [8, 6], [9, 1], [10, 0]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_5abc8e8eac194e1f9961499ba610f3a4 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_5abc8e8eac194e1f9961499ba610f3a4, shots=7838).result().get_counts(qc)
RESULT = counts
