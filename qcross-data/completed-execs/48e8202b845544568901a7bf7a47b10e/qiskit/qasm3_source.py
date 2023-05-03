# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(6, name='qr')
cr = ClassicalRegister(6, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(CRXGate(5.2771665030277894), qargs=[qr[2], qr[5]], cargs=[])
qc.append(RYGate(2.7769187719860096), qargs=[qr[5]], cargs=[])
qc.append(CRYGate(2.1848751379170706), qargs=[qr[0], qr[2]], cargs=[])
qc.append(C3XGate(), qargs=[qr[0], qr[1], qr[5], qr[4]], cargs=[])
qc.append(RYGate(0.43166458716598444), qargs=[qr[0]], cargs=[])
qc.append(DCXGate(), qargs=[qr[1], qr[3]], cargs=[])
qc.append(RXGate(4.785958015357605), qargs=[qr[0]], cargs=[])
qc.append(CRXGate(5.271022058006445), qargs=[qr[3], qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: QASM_CONVERSION


from qiskit.qasm3 import loads, dumps
qc = loads(dumps(qc))

# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1, coupling_map=[[0, 1], [0, 2], [1, 0], [1, 3], [1, 5], [1, 8], [2, 0], [2, 7], [3, 1], [4, 5], [4, 6], [5, 1], [5, 4], [6, 4], [7, 2], [8, 1]])# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_074eb075bcd946bf8157ba01d83613eb = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_074eb075bcd946bf8157ba01d83613eb, shots=1385).result().get_counts(qc)
RESULT = counts
