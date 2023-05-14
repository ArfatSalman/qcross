# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_492844 = Parameter('p_492844')
p_730e02 = Parameter('p_730e02')
p_57eb86 = Parameter('p_57eb86')
p_66f8bd = Parameter('p_66f8bd')
p_413130 = Parameter('p_413130')
p_00b361 = Parameter('p_00b361')
p_37a10a = Parameter('p_37a10a')
p_8594a5 = Parameter('p_8594a5')
p_1a08ce = Parameter('p_1a08ce')
p_ec5eaf = Parameter('p_ec5eaf')
p_dd7bb0 = Parameter('p_dd7bb0')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(2, name='qr')
cr = ClassicalRegister(2, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZZGate(p_492844), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(ECRGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(p_1a08ce), qargs=[qr[0], qr[1]], cargs=[])
qc.append(TGate(), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[1]], cargs=[])
qc.append(CRXGate(p_730e02), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CRZGate(p_37a10a), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[1]], cargs=[])
qc.append(RZGate(p_00b361), qargs=[qr[1]], cargs=[])
qc.append(RZGate(p_413130), qargs=[qr[1]], cargs=[])
qc.append(CU1Gate(p_57eb86), qargs=[qr[0], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RZZGate(p_8594a5), qargs=[qr[0], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(RYYGate(p_66f8bd), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[1]], cargs=[])
qc.append(RZGate(p_ec5eaf), qargs=[qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(p_dd7bb0), qargs=[qr[1], qr[0]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_908ff6 = QuantumRegister(4, name='qr_908ff6')
qc.add_register(qr_908ff6)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_492844: 6.163759533339787, p_730e02: 5.987304452123941, p_57eb86: 1.6723037552953224, p_66f8bd: 3.3705408413231095, p_413130: 5.512260524440591, p_00b361: 5.320621737498446, p_37a10a: 2.2498881927557752, p_8594a5: 6.086884486572108, p_1a08ce: 1.977559237989846,
    p_ec5eaf: 5.190931186022931,
    p_dd7bb0: 5.167261531657622,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_b74dd76e1fdf4277820dfb99ab3c4d93 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_b74dd76e1fdf4277820dfb99ab3c4d93, shots=346).result().get_counts(qc)
RESULT = counts
