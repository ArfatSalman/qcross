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
qc.append(RZZGate(6.163759533339787), qargs=[qr[0], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(RYYGate(1.977559237989846), qargs=[qr[1], qr[0]], cargs=[])
qc.append(TGate(), qargs=[qr[0]], cargs=[])
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
backend_12388acdade64da6ae15e712c393d71d = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_12388acdade64da6ae15e712c393d71d, shots=346).result().get_counts(qc)
RESULT = counts
