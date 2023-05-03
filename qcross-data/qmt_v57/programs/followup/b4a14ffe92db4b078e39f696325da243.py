# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(8, name="qr")
cr = ClassicalRegister(8, name="cr")
qc = QuantumCircuit(qr, cr, name="qc")
qc.append(CCZGate(), qargs=[qr[4], qr[3], qr[1]], cargs=[])
qc.append(C3XGate(), qargs=[qr[4], qr[6], qr[1], qr[5]], cargs=[])
qc.append(RYGate(0.04159691202596985), qargs=[qr[3]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[0], qr[4], qr[5], qr[3]], cargs=[])
qc.append(CCZGate(), qargs=[qr[6], qr[4], qr[7]], cargs=[])
qc.append(CRXGate(1.1755890234683788), qargs=[qr[2], qr[6]], cargs=[])
qc.append(
    RVGate(5.773627487786608, 5.1094177788600685, 0.26978519489356295),
    qargs=[qr[1]],
    cargs=[],
)
qc.append(RYYGate(1.0497226185786626), qargs=[qr[1], qr[4]], cargs=[])
qc.append(XGate(), qargs=[qr[5]], cargs=[])
qc.append(U1Gate(5.170869847116428), qargs=[qr[3]], cargs=[])
qc.append(U2Gate(5.919352275167993, 4.281168093106029), qargs=[qr[1]], cargs=[])
qc.append(
    CU3Gate(0.978761097229285, 3.4272370634074725, 5.553744714963829),
    qargs=[qr[1], qr[4]],
    cargs=[],
)
qc.append(
    U2Gate(2.4243720779571793, 5.686593670183813), qargs=[qr[2]], cargs=[]
)  # SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile

qc = transpile(qc, basis_gates=None, optimization_level=3, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute

backend_164b2b3fc6c745d8b1f230f4ba57d524 = Aer.get_backend("qasm_simulator")
counts = (
    execute(qc, backend=backend_164b2b3fc6c745d8b1f230f4ba57d524, shots=2771)
    .result()
    .get_counts(qc)
)
RESULT = counts
