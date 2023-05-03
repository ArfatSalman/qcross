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
qc.append(ECRGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SwapGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CU3Gate(0.19530688895228782, 1.7508214741181105, 0.6509821962978967), qargs=[qr[1], qr[0]], cargs=[])
qc.append(RZGate(0.07613141147187574), qargs=[qr[0]], cargs=[])
qc.append(CYGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(RZXGate(2.3441041272871757), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CRZGate(0.11523003750909885), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CYGate(), qargs=[qr[0], qr[1]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1, coupling_map=None)
# SECTION
# NAME: QASM_CONVERSION

from qiskit.qasm3 import loads, dumps
qc = loads(dumps(qc))

# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_1a9fdf09bc4644988c7bcef961775758 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_1a9fdf09bc4644988c7bcef961775758, shots=346).result().get_counts(qc)
RESULT = counts
