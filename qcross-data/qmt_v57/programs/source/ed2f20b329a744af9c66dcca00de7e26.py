
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
qc.append(RYGate(5.853149976778032), qargs=[qr[2]], cargs=[])
qc.append(CYGate(), qargs=[qr[5], qr[3]], cargs=[])
qc.append(RXXGate(1.8979725965318897), qargs=[qr[3], qr[4]], cargs=[])
qc.append(CRZGate(3.22390260798828), qargs=[qr[2], qr[1]], cargs=[])
qc.append(TdgGate(), qargs=[qr[6]], cargs=[])
qc.append(CPhaseGate(3.33138781671686), qargs=[qr[2], qr[10]], cargs=[])
qc.append(IGate(), qargs=[qr[5]], cargs=[])
qc.append(RXXGate(2.2223228953034386), qargs=[qr[6], qr[0]], cargs=[])
qc.append(CRZGate(1.958567966627553), qargs=[qr[10], qr[1]], cargs=[])
qc.append(CU1Gate(1.8658223544806745), qargs=[qr[8], qr[6]], cargs=[])
qc.append(CSGate(), qargs=[qr[6], qr[8]], cargs=[])
qc.append(C3XGate(), qargs=[qr[8], qr[3], qr[9], qr[1]], cargs=[])
qc.append(CPhaseGate(5.365920148103449), qargs=[qr[10], qr[3]], cargs=[])
qc.append(CU3Gate(3.4342195380212717,3.1911711278969404,5.406016201758407), qargs=[qr[7], qr[1]], cargs=[])
qc.append(RXXGate(0.19515517791513165), qargs=[qr[2], qr[9]], cargs=[])
qc.append(SGate(), qargs=[qr[6]], cargs=[])
qc.append(CPhaseGate(5.001328040447821), qargs=[qr[5], qr[8]], cargs=[])
qc.append(CPhaseGate(1.958603888434658), qargs=[qr[3], qr[2]], cargs=[])
qc.append(RXGate(0.723150500264737), qargs=[qr[6]], cargs=[])
qc.append(RYYGate(6.086914963294705), qargs=[qr[2], qr[0]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[6], qr[9], qr[1], qr[8]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[6], qr[4], qr[5], qr[1]], cargs=[])

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
backend_7ef9545be9d14d97b51a13527c7cd940 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_7ef9545be9d14d97b51a13527c7cd940, shots=7838).result().get_counts(qc)
RESULT = counts