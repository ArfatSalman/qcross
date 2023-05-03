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
qc.append(CUGate(4.8953107059252625, 2.6758072220615388, 3.2748083473946528, 6.236176216437301), qargs=[qr[4], qr[3]], cargs=[])
qc.append(SdgGate(), qargs=[qr[4]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[4], qr[2], qr[1], qr[3]], cargs=[])
qc.append(CUGate(3.8548770506419117, 4.254344154816252, 1.4586583527810086, 0.6558022908747309), qargs=[qr[1], qr[4]], cargs=[])
qc.append(U2Gate(4.508908477229367, 4.339644176014044), qargs=[qr[5]], cargs=[])
qc.append(C4XGate(), qargs=[qr[5], qr[2], qr[4], qr[1], qr[0]], cargs=[])
qc.append(CUGate(2.0612495225167686, 0.9108049053481971, 1.7408688031064241, 2.2294210493888307), qargs=[qr[2], qr[4]], cargs=[])
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
backend_a84fa236d4514ebb8518a814ff34053a = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_a84fa236d4514ebb8518a814ff34053a, shots=1385).result().get_counts(qc)
RESULT = counts
