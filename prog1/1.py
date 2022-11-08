
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
qc.append(YGate(), qargs=[qr[3]], cargs=[])
qc.append(CYGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(CCXGate(), qargs=[qr[0], qr[1], qr[2]], cargs=[])
qc.append(SwapGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(CRXGate(4.082791881243139), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SwapGate(), qargs=[qr[1], qr[3]], cargs=[])
qc.append(CYGate(), qargs=[qr[2], qr[1]], cargs=[])
qc.append(U1Gate(3.481387546019227), qargs=[qr[0]], cargs=[])
qc.append(U1Gate(0.35618939893147905), qargs=[qr[1]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[3], qr[1], qr[2]], cargs=[])
qc.append(RXGate(3.4021354438782296), qargs=[qr[2]], cargs=[])

# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)

qc.qasm(formatted=True)

# SECTION
# NAME: OPTIMIZATION_LEVEL

# from qiskit import transpile
# qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)

# # SECTION
# # NAME: EXECUTION

# from qiskit import Aer, transpile, execute
# backend_0aeb997d610641108c5db249af0a7269 = Aer.get_backend('qasm_simulator')
# counts = execute(qc, backend=backend_0aeb997d610641108c5db249af0a7269, shots=692).result().get_counts(qc)
# RESULT = counts
# print(counts)