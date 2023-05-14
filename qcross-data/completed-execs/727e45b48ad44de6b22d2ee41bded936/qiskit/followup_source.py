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
# NAME: USELESS_ENTITIES

qr_219140 = QuantumRegister(7, name='qr_219140')
qc.add_register(qr_219140)
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
backend_3334b9e5a98b4455829b11d126a4b101 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_3334b9e5a98b4455829b11d126a4b101, shots=489).result().get_counts(qc)
RESULT = counts
