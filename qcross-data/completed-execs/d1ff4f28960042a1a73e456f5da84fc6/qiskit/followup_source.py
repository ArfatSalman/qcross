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
p_4b58f7 = Parameter('p_4b58f7')
p_b10c48 = Parameter('p_b10c48')
p_da461d = Parameter('p_da461d')
p_a1b5f5 = Parameter('p_a1b5f5')
p_69e8c5 = Parameter('p_69e8c5')
p_eb8e6b = Parameter('p_eb8e6b')
p_7fdc7e = Parameter('p_7fdc7e')
p_c0b116 = Parameter('p_c0b116')
p_669459 = Parameter('p_669459')
p_c6c4c2 = Parameter('p_c6c4c2')
p_eb23fe = Parameter('p_eb23fe')
p_33d287 = Parameter('p_33d287')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CRXGate(p_eb8e6b), qargs=[qr[4], qr[3]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(CRZGate(p_c6c4c2), qargs=[qr[3], qr[4]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[4]], cargs=[])
qc.append(RYYGate(1.6723037552953224), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[4]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[4]], cargs=[])
qc.append(CUGate(p_c0b116, p_eb23fe, p_a1b5f5, p_669459), qargs=[qr[1], qr[
    4]], cargs=[])
qc.append(RZGate(p_da461d), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(p_7fdc7e), qargs=[qr[0], qr[2]], cargs=[])
qc.append(CU1Gate(p_33d287), qargs=[qr[3], qr[0]], cargs=[])
qc.append(UGate(p_69e8c5, p_4b58f7, p_b10c48), qargs=[qr[4]], cargs=[])
qc.append(CHGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[4]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[1]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_09ecd4 = QuantumRegister(6, name='qr_09ecd4')
qc.add_register(qr_09ecd4)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_4b58f7: 0.07157463504881167,
    p_b10c48: 1.4112277317699358,
    p_da461d: 4.229610589867865,
    p_a1b5f5: 4.623446645668956,
    p_69e8c5: 5.887184334931191,
    p_eb8e6b: 2.0099472182748075,
    p_7fdc7e: 5.398622178940033,
    p_c0b116: 5.708725119517347,
    p_669459: 3.865496458458116,
    p_c6c4c2: 1.0296448789776642,
    p_eb23fe: 4.167661441102218,
    p_33d287: 3.2142159669963557,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_cc8da9542868443eab33e2890e137401 = Aer.get_backend('aer_simulator_matrix_product_state')
counts = execute(qc, backend=backend_cc8da9542868443eab33e2890e137401, shots=979).result().get_counts(qc)
RESULT = counts
