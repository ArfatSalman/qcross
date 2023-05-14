# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(11, name='qr')
cr = ClassicalRegister(11, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[6]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[5], qr[8]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(CCXGate(), qargs=[qr[7], qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[8]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[4], qr[5], qr[3]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[9]], cargs=[])
qc.append(CCXGate(), qargs=[qr[2], qr[4], qr[8]], cargs=[])
qc.append(SdgGate(), qargs=[qr[2]], cargs=[])
qc.append(U2Gate(4.214504315296764, 4.6235667602042065), qargs=[qr[4]],
    cargs=[])
qc.append(CSXGate(), qargs=[qr[6], qr[8]], cargs=[])
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
backend_9883f1ef959c4c40a4c9ac5b8539366e = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_9883f1ef959c4c40a4c9ac5b8539366e, shots=7838).result().get_counts(qc)
RESULT = counts
