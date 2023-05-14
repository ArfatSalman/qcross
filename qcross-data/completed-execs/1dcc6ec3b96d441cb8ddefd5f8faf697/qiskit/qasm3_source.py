# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS
# SECTION
# NAME: PARAMETERS
p_ea6b64 = Parameter('p_ea6b64')
p_2e72b1 = Parameter('p_2e72b1')
p_ee580c = Parameter('p_ee580c')
p_6eeda0 = Parameter('p_6eeda0')
p_f65747 = Parameter('p_f65747')
p_18bd1c = Parameter('p_18bd1c')
p_ba0550 = Parameter('p_ba0550')
p_d56d65 = Parameter('p_d56d65')
p_01353d = Parameter('p_01353d')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_ea6b64), qargs=[qr[3]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CRXGate(p_18bd1c), qargs=[qr[4], qr[3]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(CRZGate(p_f65747), qargs=[qr[3], qr[4]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[4]], cargs=[])
qc.append(RYYGate(p_01353d), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[4]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[4]], cargs=[])
qc.append(CUGate(p_ee580c, p_2e72b1, p_ba0550, 3.865496458458116), qargs=[
    qr[1], qr[4]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(5.398622178940033), qargs=[qr[0], qr[2]], cargs=[])
qc.append(CU1Gate(3.2142159669963557), qargs=[qr[3], qr[0]], cargs=[])
qc.append(UGate(p_6eeda0, 0.07157463504881167, p_d56d65), qargs=[qr[4]],
    cargs=[])
qc.append(CHGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_ea6b64: 6.163759533339787,
    p_2e72b1: 4.167661441102218,
    p_ee580c: 5.708725119517347,
    p_6eeda0: 5.887184334931191,
    p_f65747: 1.0296448789776642,
    p_18bd1c: 2.0099472182748075,
    p_ba0550: 4.623446645668956,
    p_d56d65: 1.4112277317699358,
    p_01353d: 1.6723037552953224,
})

# SECTION
# NAME: QASM_CONVERSION


from qiskit.qasm3 import loads, dumps
qc = loads(dumps(qc))

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 2], [0, 5], [1, 0], [1, 3], [2, 0], [3, 1], [4, 5], [5, 0], [5, 4]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_cf1398bce19541fb94264b7d94e8e068 = Aer.get_backend('aer_simulator_density_matrix')
counts = execute(qc, backend=backend_cf1398bce19541fb94264b7d94e8e068, shots=979).result().get_counts(qc)
RESULT = counts
