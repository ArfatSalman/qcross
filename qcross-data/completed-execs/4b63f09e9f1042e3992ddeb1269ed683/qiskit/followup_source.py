# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=[[0,
    1], [1, 0], [1, 3], [1, 5], [2, 5], [3, 1], [4, 5], [5, 1], [5, 2], [5, 4]]
    )
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_a689cb4bd240458983d97087607855c1 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_a689cb4bd240458983d97087607855c1, shots=979).result().get_counts(qc)
RESULT = counts
