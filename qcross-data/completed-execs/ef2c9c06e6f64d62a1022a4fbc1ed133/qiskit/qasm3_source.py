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
qc.append(RZGate(6.163759533339787), qargs=[qr[8]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[5], qr[8]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[4], qr[1]], cargs=[])
qc.append(CCXGate(), qargs=[qr[7], qr[6], qr[1]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(TGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[9]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[4], qr[5]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[4]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[3], qr[9]], cargs=[])
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
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_084d7960363e456ab8ad5aff0a6b4474 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_084d7960363e456ab8ad5aff0a6b4474, shots=5542).result().get_counts(qc)
RESULT = counts
