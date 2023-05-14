# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(4, name='qr')
cr = ClassicalRegister(4, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(SdgGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(TdgGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(CCXGate(), qargs=[qr[2], qr[3], qr[1]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
# SECTION
# NAME: USELESS_ENTITIES

qr_e88545 = QuantumRegister(9, name='qr_e88545')
subcircuit.add_register(qr_e88545)
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
backend_4c698c169b9d49f8946d24ad06cbb819 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_4c698c169b9d49f8946d24ad06cbb819, shots=692).result().get_counts(qc)
RESULT = counts
