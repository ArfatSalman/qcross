# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(6, name='qr')
cr = ClassicalRegister(6, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0,
    1], [0, 2], [0, 4], [0, 6], [1, 0], [1, 3], [2, 0], [3, 1], [3, 5], [4,
    0], [5, 3], [6, 0]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_b13cb17801ca44bc8f24cc46da046cd3 = Aer.get_backend('aer_simulator_density_matrix')
counts = execute(qc, backend=backend_b13cb17801ca44bc8f24cc46da046cd3, shots=1385).result().get_counts(qc)
RESULT = counts
