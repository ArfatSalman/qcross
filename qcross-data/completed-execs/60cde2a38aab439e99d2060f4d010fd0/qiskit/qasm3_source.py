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
qc.append(RZGate(6.163759533339787), qargs=[qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[5], qr[2]], cargs=[])
qc.append(CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245,
    5.987304452123941), qargs=[qr[5], qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[3], qr[2], qr[0], qr[5]], cargs=[])
qc.append(CCXGate(), qargs=[qr[3], qr[4], qr[0]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[1], qr[4], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[5]], cargs=[])
qc.append(TGate(), qargs=[qr[2]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[4], qr[1], qr[2]], cargs=[])
qc.append(SGate(), qargs=[qr[4]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[3], qr[4]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[3]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: QASM_CONVERSION


from qiskit.qasm3 import loads, dumps
qc = loads(dumps(qc))

# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_4d99dc1aafe443feb4e8a593d670a2e8 = Aer.get_backend('aer_simulator_matrix_product_state')
counts = execute(qc, backend=backend_4d99dc1aafe443feb4e8a593d670a2e8, shots=1385).result().get_counts(qc)
RESULT = counts
