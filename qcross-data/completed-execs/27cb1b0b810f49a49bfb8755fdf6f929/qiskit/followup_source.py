# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(9, name='qr')
cr = ClassicalRegister(9, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[8]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_1b824a = QuantumRegister(9, name='qr_1b824a')
qc.add_register(qr_1b824a)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=['ccx', 'h'], optimization_level=2,
    coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_7825afdcf47347ac8ca3fce750b1f7a5 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_7825afdcf47347ac8ca3fce750b1f7a5, shots=3919).result().get_counts(qc)
RESULT = counts
