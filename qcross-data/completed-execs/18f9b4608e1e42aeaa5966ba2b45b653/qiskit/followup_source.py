# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(7, name='qr')
cr = ClassicalRegister(7, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[1]], cargs=[])
qc.append(ZGate(), qargs=[qr[5]], cargs=[])
qc.append(XGate(), qargs=[qr[3]], cargs=[])
qc.append(CRXGate(2.0099472182748075), qargs=[qr[0], qr[4]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[5], qr[2], qr[6], qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[5]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[0], qr[6], qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[5], qr[3]], cargs=[])
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
backend_01b9f79188994689b585faebef09c032 = Aer.get_backend('aer_simulator')
counts = execute(qc, backend=backend_01b9f79188994689b585faebef09c032, shots=1959).result().get_counts(qc)
RESULT = counts
