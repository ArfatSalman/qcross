# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(7, name='qr')
cr = ClassicalRegister(7, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
# SECTION
# NAME: USELESS_ENTITIES

qr_6e64db = QuantumRegister(10, name='qr_6e64db')
qc.add_register(qr_6e64db)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_55a2d512dc8e424288acf56761b019d7 = Aer.get_backend('aer_simulator_density_matrix')
counts = execute(qc, backend=backend_55a2d512dc8e424288acf56761b019d7, shots=1959).result().get_counts(qc)
RESULT = counts