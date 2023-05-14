# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(2, name='qr')
cr = ClassicalRegister(2, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
# SECTION
# NAME: USELESS_ENTITIES

qr_0d082f = QuantumRegister(8, name='qr_0d082f')
qc.add_register(qr_0d082f)
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
backend_098a32a8d0564b05963c9c08f963d723 = Aer.get_backend(
    'aer_simulator_matrix_product_state')
counts = execute(qc, backend=backend_098a32a8d0564b05963c9c08f963d723,
    shots=346).result().get_counts(qc)
RESULT = counts
