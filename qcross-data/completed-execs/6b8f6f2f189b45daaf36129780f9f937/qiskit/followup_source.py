# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[2]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[4], qr[3]], cargs=[])
qc.append(ECRGate(), qargs=[qr[2], qr[1]], cargs=[])
qc.append(CRXGate(2.0099472182748075), qargs=[qr[0], qr[2]], cargs=[])
qc.append(SGate(), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(1.0296448789776642), qargs=[qr[2], qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[4], qr[0]], cargs=[])
qc.append(RYYGate(1.6723037552953224), qargs=[qr[3], qr[1]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(TGate(), qargs=[qr[0]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_cc4672 = QuantumRegister(8, name='qr_cc4672')
qc.add_register(qr_cc4672)
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
backend_9c5859ae1c0a4bb9a624798406e74c9f = Aer.get_backend('statevector_simulator')
counts = execute(qc, backend=backend_9c5859ae1c0a4bb9a624798406e74c9f, shots=979).result().get_counts(qc)
RESULT = counts
