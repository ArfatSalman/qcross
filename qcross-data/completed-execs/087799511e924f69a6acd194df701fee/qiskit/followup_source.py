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
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[3]], cargs=[])
qc.append(CRXGate(2.0099472182748075), qargs=[qr[2], qr[5]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[6], qr[0], qr[1], qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0,
    1], [0, 5], [1, 0], [1, 2], [1, 3], [2, 1], [2, 6], [3, 1], [4, 5], [5,
    0], [5, 4], [6, 2]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_2cbe7c1202da41a5b7445bd3e89fd6ab = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_2cbe7c1202da41a5b7445bd3e89fd6ab, shots=1959).result().get_counts(qc)
RESULT = counts
