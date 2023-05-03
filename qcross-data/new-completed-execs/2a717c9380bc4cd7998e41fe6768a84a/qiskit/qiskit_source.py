# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter

# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(10, name="qr")
cr = ClassicalRegister(10, name="cr")
qc = QuantumCircuit(qr, cr, name="qc")
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[9], qr[2], qr[0], qr[6]], cargs=[])
qc.append(C4XGate(), qargs=[qr[5], qr[0], qr[9], qr[8], qr[6]], cargs=[])
qc.append(
    UGate(3.1560639900200687, 5.736507853795902, 5.182419857278261),
    qargs=[qr[3]],
    cargs=[],
)
qc.append(C3SXGate(), qargs=[qr[6], qr[3], qr[5], qr[9]], cargs=[])
qc.append(U1Gate(5.966509081754044), qargs=[qr[2]], cargs=[])
qc.append(SXGate(), qargs=[qr[6]], cargs=[])
qc.append(CU1Gate(4.213559936940442), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CCZGate(), qargs=[qr[6], qr[5], qr[1]], cargs=[])
qc.append(SdgGate(), qargs=[qr[6]], cargs=[])
qc.append(ZGate(), qargs=[qr[5]], cargs=[])
qc.append(SXGate(), qargs=[qr[9]], cargs=[])
qc.append(TdgGate(), qargs=[qr[6]], cargs=[])
qc.append(CRYGate(1.543339878695638), qargs=[qr[5], qr[1]], cargs=[])
qc.append(TdgGate(), qargs=[qr[9]], cargs=[])
qc.append(CYGate(), qargs=[qr[9], qr[3]], cargs=[])
qc.append(RXXGate(3.253117584460498), qargs=[qr[2], qr[4]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[4], qr[3], qr[1], qr[6]], cargs=[])
qc.append(U1Gate(4.922680836398291), qargs=[qr[1]], cargs=[])
qc.append(CU1Gate(4.44382187374409), qargs=[qr[7], qr[4]], cargs=[])
qc.append(CCXGate(), qargs=[qr[9], qr[2], qr[4]], cargs=[])
qc.append(U1Gate(6.275086588388869), qargs=[qr[9]], cargs=[])
qc.append(CCXGate(), qargs=[qr[7], qr[1], qr[3]], cargs=[])
qc.append(CSGate(), qargs=[qr[9], qr[5]], cargs=[])
qc.append(CYGate(), qargs=[qr[1], qr[8]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(RXXGate(4.826421202599676), qargs=[qr[5], qr[7]], cargs=[])
qc.append(CRYGate(0.6390825368890776), qargs=[qr[6], qr[3]], cargs=[])
qc.append(C4XGate(), qargs=[qr[9], qr[2], qr[4], qr[8], qr[7]], cargs=[])

# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)

print(qc.qasm())

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile

qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=None)

# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute

backend_0b81766f33524d50bbf320413693c6dd = Aer.get_backend("qasm_simulator")
counts = (
    execute(qc, backend=backend_0b81766f33524d50bbf320413693c6dd, shots=5542)
    .result()
    .get_counts(qc)
)
RESULT = counts
