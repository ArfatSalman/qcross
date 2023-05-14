# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(11, name='qr')
cr = ClassicalRegister(11, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[6], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(CCXGate(), qargs=[qr[5], qr[9], qr[7]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=3, coupling_map=[[0,
    1], [0, 4], [0, 5], [0, 7], [1, 0], [1, 6], [1, 11], [2, 4], [3, 7], [4,
    0], [4, 2], [4, 7], [4, 8], [5, 0], [6, 1], [7, 0], [7, 3], [7, 4], [7,
    12], [8, 4], [8, 11], [9, 11], [10, 12], [11, 1], [11, 8], [11, 9], [11,
    12], [12, 7], [12, 10], [12, 11]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_f86e878aa1134ed199cee86957def550 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_f86e878aa1134ed199cee86957def550, shots=7838).result().get_counts(qc)
RESULT = counts
