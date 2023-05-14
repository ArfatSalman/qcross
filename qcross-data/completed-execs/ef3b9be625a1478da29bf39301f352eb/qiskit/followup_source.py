# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_86f185 = Parameter('p_86f185')
p_6b43a3 = Parameter('p_6b43a3')
p_7d2faf = Parameter('p_7d2faf')
p_85477f = Parameter('p_85477f')
p_f407a3 = Parameter('p_f407a3')
p_eb055e = Parameter('p_eb055e')
p_e75067 = Parameter('p_e75067')
p_93dcc8 = Parameter('p_93dcc8')
p_0d2e3c = Parameter('p_0d2e3c')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_86f185), qargs=[qr[3]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CRXGate(p_7d2faf), qargs=[qr[4], qr[3]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(CRZGate(p_0d2e3c), qargs=[qr[3], qr[4]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[4]], cargs=[])
qc.append(RYYGate(p_85477f), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[4]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[4]], cargs=[])
qc.append(CUGate(p_f407a3, p_e75067, p_93dcc8, p_eb055e), qargs=[qr[1], qr[4]], cargs=[])
qc.append(RZGate(p_6b43a3), qargs=[qr[1]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_86f185: 6.163759533339787, p_6b43a3: 4.229610589867865, p_7d2faf: 2.0099472182748075, p_85477f: 1.6723037552953224, p_f407a3: 5.708725119517347, p_eb055e: 3.865496458458116, p_e75067: 4.167661441102218, p_93dcc8: 4.623446645668956, p_0d2e3c: 1.0296448789776642})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: QASM_CONVERSION
qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_572795f6ed634914ad0a842fd75d91fb = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_572795f6ed634914ad0a842fd75d91fb, shots=979).result().get_counts(qc)
RESULT = counts
