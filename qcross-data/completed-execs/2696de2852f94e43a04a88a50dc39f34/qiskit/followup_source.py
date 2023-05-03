# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_c17d7a = Parameter('p_c17d7a')
p_b8f691 = Parameter('p_b8f691')
p_abc7bc = Parameter('p_abc7bc')
p_61eb28 = Parameter('p_61eb28')
p_efb1d9 = Parameter('p_efb1d9')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_abc7bc), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_c17d7a), qargs=[qr[6], qr[3]], cargs=[])
qc.append(CRXGate(p_efb1d9), qargs=[qr[1], qr[7]], cargs=[])
qc.append(CCXGate(), qargs=[qr[5], qr[9], qr[7]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[9]], cargs=[])
qc.append(XGate(), qargs=[qr[8]], cargs=[])
qc.append(CRZGate(p_61eb28), qargs=[qr[1], qr[6]], cargs=[])
qc.append(RZGate(p_b8f691), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[4], qr[8]], cargs=[])
qc.append(CCXGate(), qargs=[qr[4], qr[9], qr[5]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[4], qr[0], qr[9]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[7], qr[1]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_02ac22 = QuantumRegister(9, name='qr_02ac22')
qc.add_register(qr_02ac22)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_c17d7a: 4.2641612072511235, p_b8f691: 4.229610589867865, p_abc7bc: 6.163759533339787, p_61eb28: 4.167661441102218,
    p_efb1d9: 5.987304452123941,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_be54763dd3a1424c8ad4f57199c910de = Aer.get_backend('aer_simulator_statevector')
counts = execute(qc, backend=backend_be54763dd3a1424c8ad4f57199c910de, shots=5542).result().get_counts(qc)
RESULT = counts
