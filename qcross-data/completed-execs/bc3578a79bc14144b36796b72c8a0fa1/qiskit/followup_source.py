# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(3, name='qr')
cr = ClassicalRegister(3, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[1]], cargs=[])
qc.append(CHGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=[[0,
    1], [0, 3], [1, 0], [1, 2], [2, 1], [3, 0]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_d049d4e7d24f4c46a6e08d3bac85720b = Aer.get_backend('statevector_simulator')
counts = execute(qc, backend=backend_d049d4e7d24f4c46a6e08d3bac85720b, shots=489).result().get_counts(qc)
RESULT = counts
