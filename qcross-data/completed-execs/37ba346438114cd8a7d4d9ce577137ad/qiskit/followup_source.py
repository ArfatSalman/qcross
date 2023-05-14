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
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(RZZGate(5.017245588344839), qargs=[qr[0], qr[1]], cargs=[])
subcircuit.append(CYGate(), qargs=[qr[0], qr[2]], cargs=[])
subcircuit.append(CRZGate(2.008796895454228), qargs=[qr[0], qr[3]], cargs=[])
subcircuit.append(YGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(RCCXGate(), qargs=[qr[4], qr[1], qr[2]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CRXGate(2.0099472182748075), qargs=[qr[4], qr[3]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(CRZGate(1.0296448789776642), qargs=[qr[3], qr[4]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[4]], cargs=[])
qc.append(RYYGate(1.6723037552953224), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[4]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[4]], cargs=[])
qc.append(CUGate(5.708725119517347, 4.167661441102218, 4.623446645668956, 3.865496458458116), qargs=[qr[1], qr[4]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(5.398622178940033), qargs=[qr[0], qr[2]], cargs=[])
qc.append(CU1Gate(3.2142159669963557), qargs=[qr[3], qr[0]], cargs=[])
qc.append(UGate(5.887184334931191, 0.07157463504881167, 1.4112277317699358), qargs=[qr[4]], cargs=[])
qc.append(CHGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: QASM_CONVERSION

qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=['rx', 'ry', 'rz', 'p', 'cx'],
    optimization_level=2, coupling_map=[[0, 1], [0, 3], [1, 0], [1, 2], [1,
    5], [2, 1], [3, 0], [4, 5], [5, 1], [5, 4], [5, 6], [6, 5]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_aeff518eae9b47a2a79c8777a49b9b18 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_aeff518eae9b47a2a79c8777a49b9b18, shots=979).result().get_counts(qc)
RESULT = counts
