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
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(RZZGate(1.927446989780488), qargs=[qr[9], qr[4]], cargs=[])
subcircuit.append(CU3Gate(1.2827690425732097, 1.3283826543858017, 3.672121211148789), qargs=[qr[10], qr[6]], cargs=[])
subcircuit.append(CUGate(4.229610589867865, 2.696266694818697, 5.631160518436971, 2.9151388486514547), qargs=[qr[0], qr[10]], cargs=[])
subcircuit.append(RZXGate(4.563562108824195), qargs=[qr[4], qr[8]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CRZGate(4.2641612072511235), qargs=[qr[6], qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0,
    1], [0, 7], [0, 11], [1, 0], [1, 3], [1, 8], [2, 6], [3, 1], [4, 11], [
    5, 6], [5, 10], [6, 2], [6, 5], [6, 8], [7, 0], [8, 1], [8, 6], [9, 11],
    [10, 5], [11, 0], [11, 4], [11, 9]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_802e28bf731145cfa5a482a3b455e1c4 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_802e28bf731145cfa5a482a3b455e1c4, shots=7838).result().get_counts(qc)
RESULT = counts
