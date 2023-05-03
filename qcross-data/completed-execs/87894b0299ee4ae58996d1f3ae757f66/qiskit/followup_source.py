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
qc.append(CUGate(1.4006987211512518, 5.87171748222823, 1.6118094341214977, 3.48470543480054), qargs=[qr[5], qr[3]], cargs=[])
qc.append(U2Gate(0.49960530614896387, 3.4965748481666385), qargs=[qr[0]], cargs=[])
qc.append(RYGate(1.6125723299807893), qargs=[qr[0]], cargs=[])
qc.append(C3XGate(), qargs=[qr[9], qr[1], qr[5], qr[2]], cargs=[])
qc.append(RYGate(5.620914585085149), qargs=[qr[9]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
qc.append(SGate(), qargs=[qr[7]], cargs=[])
qc.append(SGate(), qargs=[qr[7]], cargs=[])
qc.append(CSwapGate(), qargs=[qr[4], qr[2], qr[9]], cargs=[])
qc.append(CRYGate(1.9836175804480751), qargs=[qr[6], qr[9]], cargs=[])
qc.append(CU1Gate(4.388257530988808), qargs=[qr[3], qr[6]], cargs=[])
qc.append(CYGate(), qargs=[qr[5], qr[9]], cargs=[])
qc.append(RYGate(4.206888046259435), qargs=[qr[1]], cargs=[])
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
backend_189bf23ab86243548c8b59dc68cc2226 = Aer.get_backend(
    'aer_simulator_statevector')
counts = execute(qc, backend=backend_189bf23ab86243548c8b59dc68cc2226,
    shots=5542).result().get_counts(qc)
RESULT = counts
