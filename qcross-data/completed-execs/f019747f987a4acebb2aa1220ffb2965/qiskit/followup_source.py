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
qc.append(CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245, 5.987304452123941), qargs=[qr[0], qr[6]], cargs=[])
qc.append(SdgGate(), qargs=[qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[8], qr[7], qr[5]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[5]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[8]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[3], qr[2], qr[0]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(UGate(2.438459595578943,3.326780904591333,3.4232119351142516), qargs=[qr[3]], cargs=[])
subcircuit.append(PhaseGate(0.4827903095199283), qargs=[qr[8]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CU1Gate(3.2142159669963557), qargs=[qr[8], qr[3]], cargs=[])
qc.append(CRZGate(1.4112277317699358), qargs=[qr[5], qr[8]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[7]], cargs=[])
qc.append(CHGate(), qargs=[qr[6], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[3], qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 7], [1, 0], [1, 2], [1, 3], [1, 5], [1, 9], [2, 1], [2, 10], [2, 11], [3, 1], [4, 7], [5, 1], [6, 10], [7, 0], [7, 4], [8, 11], [9, 1], [10, 2], [10, 6], [10, 12], [11, 2], [11, 8], [12, 10]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_d9cde1eac2e64ef095d6316d0bda8358 = Aer.get_backend('statevector_simulator')
counts = execute(qc, backend=backend_d9cde1eac2e64ef095d6316d0bda8358, shots=3919).result().get_counts(qc)
RESULT = counts
