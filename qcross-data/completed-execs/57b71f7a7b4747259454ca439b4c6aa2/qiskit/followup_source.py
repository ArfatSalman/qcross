# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(2, name='qr')
cr = ClassicalRegister(2, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(XGate(), qargs=[qr[1]], cargs=[])
subcircuit.append(CHGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(RZZGate(6.163759533339787), qargs=[qr[0], qr[1]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_e08032 = QuantumRegister(8, name='qr_e08032')
qc.add_register(qr_e08032)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=3, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_36ebec7e6a7d49ae85803b00d1441ece = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_36ebec7e6a7d49ae85803b00d1441ece, shots=346).result().get_counts(qc)
RESULT = counts
