# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[4]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(RXGate(6.033961191253911), qargs=[qr[0]], cargs=[])
subcircuit.append(CXGate(), qargs=[qr[2], qr[6]], cargs=[])
subcircuit.append(CZGate(), qargs=[qr[1], qr[0]], cargs=[])
subcircuit.append(CU3Gate(1.2827690425732097,1.3283826543858017,3.672121211148789), qargs=[qr[2], qr[5]], cargs=[])
subcircuit.append(CZGate(), qargs=[qr[0], qr[1]], cargs=[])
subcircuit.append(U1Gate(6.2047416485134805), qargs=[qr[0]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 2], [0, 5], [0, 7], [0, 8], [1, 0], [1, 6], [1, 10], [2, 0], [3, 10], [4, 8], [5, 0], [6, 1], [7, 0], [8, 0], [8, 4], [9, 10], [10, 1], [10, 3], [10, 9]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_0de4aeca93044ace956e798ff1df47d5 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_0de4aeca93044ace956e798ff1df47d5, shots=2771).result().get_counts(qc)
RESULT = counts
