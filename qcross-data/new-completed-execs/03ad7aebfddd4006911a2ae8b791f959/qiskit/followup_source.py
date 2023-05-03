# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_9a487a = Parameter('p_9a487a')
p_958665 = Parameter('p_958665')
p_15dc74 = Parameter('p_15dc74')
p_ca2ee7 = Parameter('p_ca2ee7')
p_13526e = Parameter('p_13526e')
p_13b576 = Parameter('p_13b576')
p_74b502 = Parameter('p_74b502')
p_9d695e = Parameter('p_9d695e')
p_1c2d80 = Parameter('p_1c2d80')
p_fc122e = Parameter('p_fc122e')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(9, name='qr')
cr = ClassicalRegister(9, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(IGate(), qargs=[qr[1]], cargs=[])
qc.append(C4XGate(), qargs=[qr[4], qr[7], qr[8], qr[0], qr[6]], cargs=[])
qc.append(TdgGate(), qargs=[qr[4]], cargs=[])
qc.append(PhaseGate(p_13b576), qargs=[qr[5]], cargs=[])
qc.append(C4XGate(), qargs=[qr[3], qr[0], qr[5], qr[8], qr[2]], cargs=[])
qc.append(RYGate(p_13526e), qargs=[qr[0]], cargs=[])
qc.append(TdgGate(), qargs=[qr[3]], cargs=[])
qc.append(U2Gate(p_1c2d80, p_ca2ee7), qargs=[qr[6]], cargs=[])
qc.append(CU3Gate(p_9a487a, 6.100759745363555, p_958665), qargs=[qr[0], qr[4]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[7], qr[0], qr[1], qr[8]], cargs=[])
qc.append(RYGate(p_fc122e), qargs=[qr[0]], cargs=[])
qc.append(PhaseGate(p_74b502), qargs=[qr[3]], cargs=[])
qc.append(RZZGate(p_15dc74), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CYGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(CYGate(), qargs=[qr[4], qr[2]], cargs=[])
qc.append(SGate(), qargs=[qr[3]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[8], qr[5], qr[7]], cargs=[])
qc.append(C4XGate(), qargs=[qr[0], qr[4], qr[5], qr[2], qr[6]], cargs=[])
qc.append(U1Gate(0.1283649697684065), qargs=[qr[8]], cargs=[])
qc.append(U1Gate(p_9d695e), qargs=[qr[2]], cargs=[])# SECTION
# NAME: USELESS_ENTITIES

qr_a58c70 = QuantumRegister(10, name='qr_a58c70')
qc.add_register(qr_a58c70)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_9a487a: 1.0200536425931515, p_958665: 3.891803045839442, p_15dc74: 5.548043373759139, p_ca2ee7: 4.861997899593006, p_13526e: 5.6536210846521495, p_13b576: 3.583928898313607, p_74b502: 0.6916556361503159, p_9d695e: 5.195347791320497, p_1c2d80: 5.070978145808224,
    p_fc122e: 3.345954529034082,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_5ecb0c47d957454cb3c183178e4ddced = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_5ecb0c47d957454cb3c183178e4ddced, shots=3919).result().get_counts(qc)
RESULT = counts
