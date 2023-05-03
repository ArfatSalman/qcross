
# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter

# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(9, name='qr')
cr = ClassicalRegister(9, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(IGate(), qargs=[qr[1]], cargs=[])
qc.append(C4XGate(), qargs=[qr[4], qr[7], qr[8], qr[0], qr[6]], cargs=[])
qc.append(TdgGate(), qargs=[qr[4]], cargs=[])
qc.append(PhaseGate(3.583928898313607), qargs=[qr[5]], cargs=[])
qc.append(C4XGate(), qargs=[qr[3], qr[0], qr[5], qr[8], qr[2]], cargs=[])
qc.append(RYGate(5.6536210846521495), qargs=[qr[0]], cargs=[])
qc.append(TdgGate(), qargs=[qr[3]], cargs=[])
qc.append(U2Gate(5.070978145808224,4.861997899593006), qargs=[qr[6]], cargs=[])
qc.append(CU3Gate(1.0200536425931515,6.100759745363555,3.891803045839442), qargs=[qr[0], qr[4]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[7], qr[0], qr[1], qr[8]], cargs=[])
qc.append(RYGate(3.345954529034082), qargs=[qr[0]], cargs=[])
qc.append(PhaseGate(0.6916556361503159), qargs=[qr[3]], cargs=[])
qc.append(RZZGate(5.548043373759139), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CYGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(CYGate(), qargs=[qr[4], qr[2]], cargs=[])
qc.append(SGate(), qargs=[qr[3]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[8], qr[5], qr[7]], cargs=[])
qc.append(C4XGate(), qargs=[qr[0], qr[4], qr[5], qr[2], qr[6]], cargs=[])
qc.append(U1Gate(0.1283649697684065), qargs=[qr[8]], cargs=[])
qc.append(U1Gate(5.195347791320497), qargs=[qr[2]], cargs=[])

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
backend_5ecb0c47d957454cb3c183178e4ddced = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_5ecb0c47d957454cb3c183178e4ddced, shots=3919).result().get_counts(qc)
RESULT = counts