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
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CRXGate(2.0099472182748075), qargs=[qr[4], qr[3]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(CRZGate(1.0296448789776642), qargs=[qr[3], qr[4]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[4]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=3, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_2e23eeb1613a4f9ab22c8e63619e6bb0 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_2e23eeb1613a4f9ab22c8e63619e6bb0, shots=979).result().get_counts(qc)
RESULT = counts
