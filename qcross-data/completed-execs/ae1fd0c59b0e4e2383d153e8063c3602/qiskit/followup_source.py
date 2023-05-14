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
qc.append(RZGate(6.163759533339787), qargs=[qr[6]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(CRXGate(2.0099472182748075), qargs=[qr[2], qr[3]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[4], qr[5], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[6], qr[0]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[4], qr[2], qr[5], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(ECRGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SdgGate(), qargs=[qr[0]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[2], qr[3], qr[4]], cargs=[])
qc.append(SGate(), qargs=[qr[5]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 4], [0, 6], [0, 7], [1, 0], [2, 3], [3, 2], [3, 4], [4, 0], [4, 3], [5, 7], [6, 0], [7, 0], [7, 5]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_35eadbcaaf4e4c7a80bc70cc63eb4c3f = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_35eadbcaaf4e4c7a80bc70cc63eb4c3f, shots=1959).result().get_counts(qc)
RESULT = counts
