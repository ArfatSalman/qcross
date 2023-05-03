# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(7, name='qr')
cr = ClassicalRegister(7, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(IGate(), qargs=[qr[3]], cargs=[])
qc.append(XGate(), qargs=[qr[4]], cargs=[])
qc.append(TGate(), qargs=[qr[0]], cargs=[])
qc.append(C3XGate(), qargs=[qr[4], qr[6], qr[3], qr[2]], cargs=[])
qc.append(CU1Gate(3.9840757667715256), qargs=[qr[3], qr[6]], cargs=[])
qc.append(U2Gate(1.2445320670388027, 5.484541161403915), qargs=[qr[5]], cargs=[])
qc.append(TGate(), qargs=[qr[6]], cargs=[])
qc.append(DCXGate(), qargs=[qr[6], qr[3]], cargs=[])
qc.append(U3Gate(2.0075607189768796, 4.451648094855798, 0.9112643954181384), qargs=[qr[5]], cargs=[])
qc.append(CRXGate(2.3584860491406796), qargs=[qr[1], qr[6]], cargs=[])
qc.append(CU1Gate(0.1446301149031628), qargs=[qr[3], qr[1]], cargs=[])
qc.append(CUGate(0.5186416756754034, 0.37593935376934196, 5.5900874211259195, 1.3667758390177343), qargs=[qr[2], qr[3]], cargs=[])
qc.append(XGate(), qargs=[qr[3]], cargs=[])
qc.append(UGate(5.054317038195475, 0.7695110069701433, 1.2922416810957755), qargs=[qr[1]], cargs=[])
qc.append(U2Gate(0.1149636377110738, 4.386499201930481), qargs=[qr[2]], cargs=[])
qc.append(U3Gate(4.785990021070069, 3.3831192493434576, 3.322394937884733), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[1]], cargs=[])
qc.append(CRYGate(0.6395924521893505), qargs=[qr[1], qr[0]], cargs=[])
qc.append(SwapGate(), qargs=[qr[0], qr[5]], cargs=[])
qc.append(SwapGate(), qargs=[qr[5], qr[3]], cargs=[])
qc.append(CRYGate(1.3751732052958698), qargs=[qr[4], qr[5]], cargs=[])
qc.append(IGate(), qargs=[qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[6], qr[3]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[5], qr[2], qr[0], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=['rx', 'ry', 'rz', 'p', 'cx'], optimization_level=1, coupling_map=None)
# SECTION
# NAME: EXECUTION
from qiskit import Aer, transpile, execute
backend_085b027c9de348ec98c2df6ef22cc673 = Aer.get_backend('aer_simulator_statevector')
counts = execute(qc, backend=backend_085b027c9de348ec98c2df6ef22cc673, shots=1959).result().get_counts(qc)
RESULT = counts