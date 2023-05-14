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
p_a0ca5d = Parameter('p_a0ca5d')
p_8b617c = Parameter('p_8b617c')
p_1fce1b = Parameter('p_1fce1b')
p_32ce54 = Parameter('p_32ce54')
p_6530e4 = Parameter('p_6530e4')
p_bcda17 = Parameter('p_bcda17')
p_45f58e = Parameter('p_45f58e')
p_3962ff = Parameter('p_3962ff')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(4, name='qr')
cr = ClassicalRegister(4, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_a0ca5d), qargs=[qr[1]], cargs=[])
qc.append(RZZGate(4.066449154047175), qargs=[qr[2], qr[3]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(CUGate(0.5112149185250571, p_32ce54, p_1fce1b, 5.987304452123941),
    qargs=[qr[0], qr[2]], cargs=[])
qc.append(CU1Gate(p_3962ff), qargs=[qr[3], qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[3], qr[0], qr[1], qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[3], qr[1], qr[0], qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[2]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[1], qr[0], qr[3]], cargs=[])
qc.append(RYYGate(1.740253089260498), qargs=[qr[2], qr[0]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[2], qr[3], qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(2.9790366726895714), qargs=[qr[0], qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[2], qr[0], qr[3]], cargs=[])
qc.append(RYYGate(5.398622178940033), qargs=[qr[2], qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(CU1Gate(p_bcda17), qargs=[qr[0], qr[3]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CRXGate(p_6530e4), qargs=[qr[2], qr[0]], cargs=[])
qc.append(U2Gate(p_8b617c, p_45f58e), qargs=[qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_937141 = QuantumRegister(6, name='qr_937141')
qc.add_register(qr_937141)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_a0ca5d: 6.163759533339787,
    p_8b617c: 4.214504315296764,
    p_1fce1b: 2.3864521352475245,
    p_32ce54: 5.897054719225356,
    p_6530e4: 5.94477504571567,
    p_bcda17: 3.2142159669963557,
    p_45f58e: 4.6235667602042065,
    p_3962ff: 5.154187354656876,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_0847b382fcaf4317ab3dceb475cb3ed5 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_0847b382fcaf4317ab3dceb475cb3ed5, shots=692).result().get_counts(qc)
RESULT = counts
