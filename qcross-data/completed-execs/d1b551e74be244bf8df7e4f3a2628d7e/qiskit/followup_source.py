# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(3, name='qr')
cr = ClassicalRegister(3, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(CU1Gate(1.4006987211512518), qargs=[qr[0], qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(RZGate(2.5786401929143787), qargs=[qr[1]], cargs=[])
qc.append(RYGate(3.1208310247400375), qargs=[qr[0]], cargs=[])
qc.append(CU3Gate(3.4965748481666385, 5.407902101595624, 0.6970696680696589), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CSwapGate(), qargs=[qr[0], qr[1], qr[2]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CU3Gate(3.3635160723245443, 2.227557670457083, 1.4424895697923088), qargs=[qr[0], qr[2]], cargs=[])
qc.append(RZXGate(0.4418060716084386), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CUGate(5.925227014563219, 0.21934961519025842, 2.906368483395291, 4.602208997736638), qargs=[qr[1], qr[2]], cargs=[])
qc.append(CYGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(HGate(), qargs=[qr[2]], cargs=[])
qc.append(CXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(TGate().inverse(), qargs=[qr[2]], cargs=[])
qc.append(CXGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[2]], cargs=[])
qc.append(CXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(TGate().inverse(), qargs=[qr[2]], cargs=[])
qc.append(CXGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[0]], cargs=[])
qc.append(HGate(), qargs=[qr[2]], cargs=[])
qc.append(CXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(TGate().inverse(), qargs=[qr[0]], cargs=[])
qc.append(TGate(), qargs=[qr[1]], cargs=[])
qc.append(CXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(U2Gate(2.3677386437434818, 4.094703991955255), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[1]], cargs=[])
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
backend_7f6cc26aadb944868e60c423e0ddb8e0 = Aer.get_backend(
    'statevector_simulator')
counts = execute(qc, backend=backend_7f6cc26aadb944868e60c423e0ddb8e0,
    shots=489).result().get_counts(qc)
RESULT = counts
