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
qc.append(RZGate(6.163759533339787), qargs=[qr[1]], cargs=[])
qc.append(CHGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[2], qr[1]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [1, 0], [1, 2], [2, 1]])
# SECTION
# NAME: QASM_CONVERSION


from qiskit.qasm3 import loads, dumps
qc = loads(dumps(qc))

# SECTION
# NAME: EXECUTION
from qiskit import Aer, transpile, execute
backend_b7d08243c74d4c0d94060042cd52d6e1 = Aer.get_backend('aer_simulator')
counts = execute(qc, backend=backend_b7d08243c74d4c0d94060042cd52d6e1,
    shots=489).result().get_counts(qc)
RESULT = counts
