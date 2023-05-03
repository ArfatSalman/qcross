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
qc.append(U3Gate(4.655749679598676, 2.7381706999194857, 2.740795817289426), qargs=[qr[0]], cargs=[])
qc.append(RYYGate(5.171156764260811), qargs=[qr[2], qr[1]], cargs=[])
qc.append(DCXGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(U1Gate(4.660569462447812), qargs=[qr[1]], cargs=[])
qc.append(CPhaseGate(5.442036812415247), qargs=[qr[1], qr[0]], cargs=[])
qc.append(RYGate(3.1620892961233205), qargs=[qr[2]], cargs=[])
qc.append(RZGate(2.816396898940768), qargs=[qr[2]], cargs=[])
qc.append(HGate(), qargs=[qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=['ccx', 'h'], optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION
from qiskit import Aer, transpile, execute
backend_5f7f5b89d63a4e95a9265f6efd7d631e = Aer.get_backend('statevector_simulator')
counts = execute(qc, backend=backend_5f7f5b89d63a4e95a9265f6efd7d631e, shots=489).result().get_counts(qc)
RESULT = counts