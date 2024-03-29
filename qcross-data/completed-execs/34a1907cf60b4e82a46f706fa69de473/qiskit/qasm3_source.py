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
qc.append(RZGate(6.163759533339787), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[2], qr[4]], cargs=[])
qc.append(CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245, 5.987304452123941), qargs=[qr[2], qr[3]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[4], qr[0], qr[2]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(IGate(), qargs=[qr[5]], cargs=[])
subcircuit.append(ZGate(), qargs=[qr[2]], cargs=[])
subcircuit.append(RYGate(4.658325508156331), qargs=[qr[2]], cargs=[])
subcircuit.append(CZGate(), qargs=[qr[1], qr[4]], cargs=[])
subcircuit.append(CRXGate(4.736752714049485), qargs=[qr[0], qr[4]], cargs=[])
subcircuit.append(CU1Gate(4.501598818751339), qargs=[qr[2], qr[5]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CCXGate(), qargs=[qr[1], qr[5], qr[0]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_88aa42 = QuantumRegister(2, name='qr_88aa42')
qc.add_register(qr_88aa42)
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
backend_54ca72b9c5bd42cbbb8a67e6522e45c4 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_54ca72b9c5bd42cbbb8a67e6522e45c4, shots=1385).result().get_counts(qc)
RESULT = counts
