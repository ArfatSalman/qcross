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
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 2], [1, 0], [1, 4], [2, 0], [3, 4], [4, 1], [4, 3]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_9a4186c9db6548f0a0d11a23bf64000d = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_9a4186c9db6548f0a0d11a23bf64000d, shots=692).result().get_counts(qc)
RESULT = counts
