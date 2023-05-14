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
qc.append(RZGate(6.163759533339787), qargs=[qr[2]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[6], qr[1]], cargs=[])
qc.append(ZGate(), qargs=[qr[9]], cargs=[])
qc.append(CCXGate(), qargs=[qr[4], qr[0], qr[8]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 5], [0, 6], [0, 7], [1, 0], [1, 2], [1, 9], [2, 1], [2, 3], [3, 2], [4, 5], [5, 0], [5, 4], [5, 10], [6, 0], [7, 0], [8, 9], [9, 1], [9, 8], [10, 5]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_404dc37dae75428b9bd73e85412214c5 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_404dc37dae75428b9bd73e85412214c5, shots=7838).result().get_counts(qc)
RESULT = counts
