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
qc.append(ECRGate(), qargs=[qr[3], qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=['rx', 'ry', 'rz', 'p', 'cx'],
    optimization_level=3, coupling_map=[[0, 1], [0, 2], [1, 0], [1, 3], [2,
    0], [2, 4], [3, 1], [4, 2], [4, 5], [5, 4]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_f683f0fcdb48447bb24de411bb8a53f4 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_f683f0fcdb48447bb24de411bb8a53f4, shots=979).result().get_counts(qc)
RESULT = counts
