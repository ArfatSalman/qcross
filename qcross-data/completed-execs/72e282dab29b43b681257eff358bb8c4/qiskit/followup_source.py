# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_a3a14d = Parameter('p_a3a14d')
p_03a56d = Parameter('p_03a56d')
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(11, name='qr')
cr = ClassicalRegister(11, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_a3a14d), qargs=[qr[6]], cargs=[])
qc.append(CRZGate(p_03a56d), qargs=[qr[10], qr[9]], cargs=[])
qc.append(ZGate(), qargs=[qr[7]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_a3a14d: 6.163759533339787, p_03a56d: 4.2641612072511235})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=['rx', 'ry', 'rz', 'p', 'cx'], optimization_level=2, coupling_map=None)
# SECTION
# NAME: QASM_CONVERSION

qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_9daed048bfc34d26a91c480e6524c013 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_9daed048bfc34d26a91c480e6524c013, shots=7838).result().get_counts(qc)
RESULT = counts
