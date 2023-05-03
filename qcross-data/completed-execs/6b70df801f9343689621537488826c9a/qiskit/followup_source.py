# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[3]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[1]], cargs=[])
qc.append(ECRGate(), qargs=[qr[0], qr[3]], cargs=[])
qc.append(CRXGate(2.0099472182748075), qargs=[qr[4], qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[1]], cargs=[])
qc.append(CRZGate(1.0296448789776642), qargs=[qr[0], qr[4]], cargs=[])
qc.append(CHGate(), qargs=[qr[2], qr[4]], cargs=[])
qc.append(RYYGate(1.6723037552953224), qargs=[qr[1], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[4]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(SGate(), qargs=[qr[4]], cargs=[])
qc.append(CUGate(5.708725119517347, 4.167661441102218, 4.623446645668956, 
    3.865496458458116), qargs=[qr[2], qr[4]], cargs=[])
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
backend_3d5fd6b6ef8d49cdaf239d56b888a082 = Aer.get_backend('aer_simulator_density_matrix')
counts = execute(qc, backend=backend_3d5fd6b6ef8d49cdaf239d56b888a082, shots=979).result().get_counts(qc)
RESULT = counts
