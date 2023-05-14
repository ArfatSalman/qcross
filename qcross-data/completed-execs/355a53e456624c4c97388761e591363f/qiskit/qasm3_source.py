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
qc.append(RZGate(6.163759533339787), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[7]], cargs=[])
qc.append(XGate(), qargs=[qr[7]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[6], qr[7]], cargs=[])
qc.append(CRZGate(1.0296448789776642), qargs=[qr[3], qr[7]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[6], qr[1], qr[7], qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[5]], cargs=[])
qc.append(XGate(), qargs=[qr[3]], cargs=[])
qc.append(RYYGate(1.740253089260498), qargs=[qr[7], qr[1]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [1, 0], [1, 2], [1, 7], [1, 8], [2, 1], [2, 9], [2, 10], [3, 9], [4, 5], [4, 9], [5, 4], [6, 8], [6, 11], [7, 1], [8, 1], [8, 6], [9, 2], [9, 3], [9, 4], [10, 2], [11, 6]])
# SECTION
# NAME: QASM_CONVERSION


from qiskit.qasm3 import loads, dumps
qc = loads(dumps(qc))

# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_a10b9759e5264f01a030c33e7bd714cf = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_a10b9759e5264f01a030c33e7bd714cf, shots=2771).result().get_counts(qc)
RESULT = counts
