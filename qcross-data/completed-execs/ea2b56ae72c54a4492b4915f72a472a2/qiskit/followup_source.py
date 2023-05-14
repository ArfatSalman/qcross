# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0,
    1], [0, 2], [0, 4], [1, 0], [1, 6], [2, 0], [3, 5], [4, 0], [4, 5], [5,
    3], [5, 4], [6, 1]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_66d29dd0a3b74b14afe67941beaaa39e = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_66d29dd0a3b74b14afe67941beaaa39e, shots=979).result().get_counts(qc)
RESULT = counts
