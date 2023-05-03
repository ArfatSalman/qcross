# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[6], qr[3]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[1], qr[7]], cargs=[])
qc.append(CCXGate(), qargs=[qr[5], qr[9], qr[7]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[9]], cargs=[])
qc.append(XGate(), qargs=[qr[8]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0,
    1], [0, 6], [0, 7], [0, 10], [0, 12], [1, 0], [1, 2], [1, 14], [2, 1],
    [2, 5], [2, 8], [2, 10], [3, 5], [3, 8], [4, 5], [5, 2], [5, 3], [5, 4],
    [5, 7], [5, 11], [5, 13], [6, 0], [6, 7], [7, 0], [7, 5], [7, 6], [8, 2
    ], [8, 3], [9, 12], [10, 0], [10, 2], [11, 5], [12, 0], [12, 9], [12, 
    14], [13, 5], [14, 1], [14, 12]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_1a3c72d471c34fdd97e56164b6698656 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_1a3c72d471c34fdd97e56164b6698656, shots=5542).result().get_counts(qc)
RESULT = counts
