# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[6]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CRZGate(1.0296448789776642), qargs=[qr[1], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[7], qr[6], qr[3]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_7c915a = QuantumRegister(3, name='qr_7c915a')
qc.add_register(qr_7c915a)
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
backend_bcde0cabc12f40d5b56d5db89f6ef732 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_bcde0cabc12f40d5b56d5db89f6ef732, shots=2771).result().get_counts(qc)
RESULT = counts
