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
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0,
    1], [0, 2], [0, 3], [1, 0], [2, 0], [3, 0], [3, 7], [4, 7], [5, 7], [6,
    7], [7, 3], [7, 4], [7, 5], [7, 6]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_b011123155ab4af0b9b2ea8941957385 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_b011123155ab4af0b9b2ea8941957385, shots=2771).result().get_counts(qc)
RESULT = counts
