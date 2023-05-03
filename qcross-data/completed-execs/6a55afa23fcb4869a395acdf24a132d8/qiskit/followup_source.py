# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(9, name='qr')
cr = ClassicalRegister(9, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[8]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[4]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: QASM_CONVERSION

qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=['ccx', 'h'], optimization_level=2,
    coupling_map=[[0, 1], [0, 3], [0, 6], [0, 8], [1, 0], [1, 9], [2, 5], [
    3, 0], [4, 5], [5, 2], [5, 4], [5, 8], [6, 0], [7, 9], [8, 0], [8, 5],
    [9, 1], [9, 7]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_8ff6772ac97c4c53a1d3f2e877ee6139 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_8ff6772ac97c4c53a1d3f2e877ee6139, shots=3919).result().get_counts(qc)
RESULT = counts
