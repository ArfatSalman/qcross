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
qc.append(RZGate(6.163759533339787), qargs=[qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(CRXGate(2.0099472182748075), qargs=[qr[4], qr[0]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[6], qr[5], qr[3], qr[4]], cargs=[])
qc.append(CHGate(), qargs=[qr[2], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[5], qr[4], qr[3], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[4]], cargs=[])
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
backend_383ff38669e647c59ed11e644f25b431 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_383ff38669e647c59ed11e644f25b431, shots=1959).result().get_counts(qc)
RESULT = counts
