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
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0,
    1], [0, 4], [0, 6], [1, 0], [1, 3], [1, 8], [1, 12], [2, 5], [3, 1], [4,
    0], [5, 2], [5, 11], [6, 0], [6, 14], [7, 13], [7, 14], [8, 1], [9, 14],
    [10, 11], [11, 5], [11, 10], [11, 14], [12, 1], [13, 7], [14, 6], [14, 
    7], [14, 9], [14, 11]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_ef4dea72ab3443958515c94bb009ac6d = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_ef4dea72ab3443958515c94bb009ac6d, shots=5542).result().get_counts(qc)
RESULT = counts
