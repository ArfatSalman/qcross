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
qc.append(ECRGate(), qargs=[qr[9], qr[2]], cargs=[])
qc.append(TdgGate(), qargs=[qr[4]], cargs=[])
qc.append(CU1Gate(0.7405945593267375), qargs=[qr[9], qr[3]], cargs=[])
qc.append(CRYGate(4.601077991755651), qargs=[qr[7], qr[9]], cargs=[])
qc.append(CSwapGate(), qargs=[qr[6], qr[0], qr[9]], cargs=[])
qc.append(CPhaseGate(2.9147217589256114), qargs=[qr[6], qr[2]], cargs=[])
qc.append(PhaseGate(0.5021373390560734), qargs=[qr[9]], cargs=[])
qc.append(XGate(), qargs=[qr[9]], cargs=[])
qc.append(U1Gate(4.188067174285268), qargs=[qr[4]], cargs=[])
qc.append(CHGate(), qargs=[qr[7], qr[9]], cargs=[])
qc.append(TdgGate(), qargs=[qr[0]], cargs=[])
qc.append(CPhaseGate(2.629684885038655), qargs=[qr[5], qr[3]], cargs=[])
qc.append(CPhaseGate(5.383276207092515), qargs=[qr[2], qr[7]], cargs=[])
qc.append(HGate(), qargs=[qr[1]], cargs=[])
qc.append(ECRGate(), qargs=[qr[8], qr[6]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=['ccx', 'h'], optimization_level=0, coupling_map=None)
# SECTION
# NAME: EXECUTION
from qiskit import Aer, transpile, execute
backend_fdcb185d1cec4236953929c63cf5c3ac = Aer.get_backend('statevector_simulator')
counts = execute(qc, backend=backend_fdcb185d1cec4236953929c63cf5c3ac, shots=7838).result().get_counts(qc)
RESULT = counts