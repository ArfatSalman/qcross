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
qc.append(RZGate(6.163759533339787), qargs=[qr[9]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[6], qr[9]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[5], qr[8]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_e1770c = QuantumRegister(7, name='qr_e1770c')
qc.add_register(qr_e1770c)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_5296c4258bcf4d3c8dac9e6eef06daab = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_5296c4258bcf4d3c8dac9e6eef06daab, shots=5542).result().get_counts(qc)
RESULT = counts
