# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(4, name='qr')
cr = ClassicalRegister(4, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
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
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [1, 0], [1, 3], [2, 3], [3, 1], [3, 2]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_9bb0300acf954d56adfaa0acb67ebf8c = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_9bb0300acf954d56adfaa0acb67ebf8c, shots=692).result().get_counts(qc)
RESULT = counts
