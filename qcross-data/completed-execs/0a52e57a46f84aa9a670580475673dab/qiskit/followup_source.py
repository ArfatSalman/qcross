# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(3, name='qr')
cr = ClassicalRegister(3, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1, coupling_map=[[0,
    1], [0, 2], [1, 0], [2, 0]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_bcb1049243fc47b0bda9fa780f660c43 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_bcb1049243fc47b0bda9fa780f660c43, shots=489).result().get_counts(qc)
RESULT = counts
