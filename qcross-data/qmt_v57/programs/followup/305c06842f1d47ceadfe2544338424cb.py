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
qc.append(CU1Gate(4.335679443154954), qargs=[qr[0], qr[1]], cargs=[])
qc.append(RGate(1.1553086314970271, 5.667151402550979), qargs=[qr[0]], cargs=[])
qc.append(CSdgGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(YGate(), qargs=[qr[1]], cargs=[])
qc.append(U3Gate(1.3724528769143325, 0.44345184772069407, 4.121804766388379), qargs=[qr[1]], cargs=[])
qc.append(CRXGate(3.979943771912046), qargs=[qr[0], qr[1]], cargs=[])
qc.append(RYYGate(2.940100953861933), qargs=[qr[0], qr[1]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[0], qr[1]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CSdgGate(), qargs=[qr[1], qr[0]], cargs=[])
subcircuit.append(ECRGate(), qargs=[qr[0], qr[1]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(iSwapGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CRXGate(0.9996777376735287), qargs=[qr[1], qr[0]], cargs=[])
qc.append(RYYGate(5.385125621828923), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CSGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CSGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CSdgGate(), qargs=[qr[0], qr[1]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_2b8246 = QuantumRegister(9, name='qr_2b8246')
qc.add_register(qr_2b8246)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_fa4b6ff060964c3296266c737b5030c7 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_fa4b6ff060964c3296266c737b5030c7, shots=346).result().get_counts(qc)
RESULT = counts
