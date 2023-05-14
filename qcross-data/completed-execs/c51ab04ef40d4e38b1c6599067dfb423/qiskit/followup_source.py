# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_236385 = Parameter('p_236385')
p_500aa6 = Parameter('p_500aa6')
p_8f916e = Parameter('p_8f916e')
p_8aac37 = Parameter('p_8aac37')
p_9f7fb1 = Parameter('p_9f7fb1')
p_3176a0 = Parameter('p_3176a0')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CRXGate(p_3176a0), qargs=[qr[4], qr[3]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(CRZGate(1.0296448789776642), qargs=[qr[3], qr[4]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[4]], cargs=[])
qc.append(RYYGate(1.6723037552953224), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[4]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[4]], cargs=[])
qc.append(CUGate(5.708725119517347, 4.167661441102218, p_8aac37, 3.865496458458116), qargs=[qr[1], qr[4]], cargs=[])
qc.append(RZGate(p_8f916e), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(5.398622178940033), qargs=[qr[0], qr[2]], cargs=[])
qc.append(CU1Gate(3.2142159669963557), qargs=[qr[3], qr[0]], cargs=[])
qc.append(UGate(p_9f7fb1, p_236385, p_500aa6), qargs=[qr[4]], cargs=[])
qc.append(CHGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[4]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CHGate(), qargs=[qr[0], qr[1]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_236385: 0.07157463504881167, p_500aa6: 1.4112277317699358, p_8f916e: 4.229610589867865, p_8aac37: 4.623446645668956, p_9f7fb1: 5.887184334931191, p_3176a0: 2.0099472182748075})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=['rx', 'ry', 'rz', 'p', 'cx'], optimization_level=1, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_6e2d8bf1af55489a92d00168481c28fa = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_6e2d8bf1af55489a92d00168481c28fa, shots=979).result().get_counts(qc)
RESULT = counts
