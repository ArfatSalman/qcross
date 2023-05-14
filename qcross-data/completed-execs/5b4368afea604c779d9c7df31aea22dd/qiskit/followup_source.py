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
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(CCXGate(), qargs=[qr[5], qr[9], qr[7]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: QASM_CONVERSION

qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0,
    1], [1, 0], [1, 3], [1, 8], [2, 7], [3, 1], [3, 6], [3, 11], [4, 8], [5,
    7], [6, 3], [7, 2], [7, 5], [7, 9], [8, 1], [8, 4], [8, 9], [9, 7], [9,
    8], [9, 10], [10, 9], [11, 3], [11, 12], [12, 11]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_18ab9412daef4c039c96bfd17d9c349f = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_18ab9412daef4c039c96bfd17d9c349f, shots=7838).result().get_counts(qc)
RESULT = counts
