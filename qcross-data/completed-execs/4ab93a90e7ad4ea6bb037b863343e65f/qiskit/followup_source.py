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
qc.append(RZZGate(6.163759533339787), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_2f5ffc = QuantumRegister(10, name='qr_2f5ffc')
qc.add_register(qr_2f5ffc)
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
backend_c40336a0d08d45c2bad6af1e2d4a859b = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_c40336a0d08d45c2bad6af1e2d4a859b, shots=346).result().get_counts(qc)
RESULT = counts