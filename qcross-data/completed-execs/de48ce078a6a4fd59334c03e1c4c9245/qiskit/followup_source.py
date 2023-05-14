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
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_7d34e5 = QuantumRegister(6, name='qr_7d34e5')
qc.add_register(qr_7d34e5)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: QASM_CONVERSION

qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_35f429d8efdb4a4a859d677f8dc8c20b = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_35f429d8efdb4a4a859d677f8dc8c20b, shots=5542).result().get_counts(qc)
RESULT = counts
