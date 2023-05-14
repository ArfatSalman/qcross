# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
# SECTION
# NAME: USELESS_ENTITIES

qr_5e2429 = QuantumRegister(4, name='qr_5e2429')
qc.add_register(qr_5e2429)
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
qc = transpile(qc, basis_gates=['ccx', 'h'], optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_c4b488939691490fa536c73f103699dc = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_c4b488939691490fa536c73f103699dc, shots=5542).result().get_counts(qc)
RESULT = counts
