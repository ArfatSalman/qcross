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
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(CCXGate(), qargs=[qr[5], qr[9], qr[7]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[7]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[10], qr[6], qr[8]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[0]], cargs=[])
qc.append(CCXGate(), qargs=[qr[7], qr[10], qr[2]], cargs=[])
qc.append(SdgGate(), qargs=[qr[7]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0,
    1], [0, 9], [1, 0], [1, 2], [1, 5], [1, 8], [2, 1], [3, 8], [4, 9], [5,
    1], [6, 7], [6, 9], [7, 6], [8, 1], [8, 3], [9, 0], [9, 4], [9, 6], [9,
    10], [10, 9]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_a4aa59f7692d4d7eb6b9d3291660af81 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_a4aa59f7692d4d7eb6b9d3291660af81, shots=7838).result().get_counts(qc)
RESULT = counts
