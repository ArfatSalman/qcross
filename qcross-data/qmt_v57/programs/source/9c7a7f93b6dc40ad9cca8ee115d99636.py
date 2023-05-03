
# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter

# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(C4XGate(), qargs=[qr[4], qr[2], qr[0], qr[1], qr[3]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[2], qr[4], qr[3]], cargs=[])
qc.append(C4XGate(), qargs=[qr[4], qr[2], qr[0], qr[1], qr[3]], cargs=[])
qc.append(C3XGate(), qargs=[qr[4], qr[0], qr[1], qr[3]], cargs=[])
qc.append(SdgGate(), qargs=[qr[4]], cargs=[])

# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=None)

# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_78388998e7274756b5aac9198c4d6dfd = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_78388998e7274756b5aac9198c4d6dfd, shots=979).result().get_counts(qc)
RESULT = counts