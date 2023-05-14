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
qc.append(ECRGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[1], qr[0]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_bc9ba6 = QuantumRegister(8, name='qr_bc9ba6')
qc.add_register(qr_bc9ba6)
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
backend_aa7718e5c36241d6be82c18e2377069c = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_aa7718e5c36241d6be82c18e2377069c, shots=346).result().get_counts(qc)
RESULT = counts
