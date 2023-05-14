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
qc.append(RZGate(6.163759533339787), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(XGate(), qargs=[qr[6]], cargs=[])
qc.append(CRXGate(2.0099472182748075), qargs=[qr[0], qr[3]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[2], qr[5], qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[4], qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[0], qr[5], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[1], qr[6]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_19069d = QuantumRegister(7, name='qr_19069d')
qc.add_register(qr_19069d)
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
backend_e6ca06527b16400da100654a2d6dc325 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_e6ca06527b16400da100654a2d6dc325, shots=1959).result().get_counts(qc)
RESULT = counts
