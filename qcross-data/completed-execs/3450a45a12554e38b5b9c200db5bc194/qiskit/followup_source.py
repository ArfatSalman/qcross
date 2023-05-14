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
qc.append(RZGate(6.163759533339787), qargs=[qr[1]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_911505 = QuantumRegister(8, name='qr_911505')
qc.add_register(qr_911505)
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
backend_80cc46f4b8d7403391dd0596ef9d2e72 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_80cc46f4b8d7403391dd0596ef9d2e72, shots=692).result().get_counts(qc)
RESULT = counts
