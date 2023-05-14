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

qr_186bf7 = QuantumRegister(9, name='qr_186bf7')
qc.add_register(qr_186bf7)
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
backend_259f55111ed54f0e9690dc79c9570a30 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_259f55111ed54f0e9690dc79c9570a30, shots=489).result().get_counts(qc)
RESULT = counts
