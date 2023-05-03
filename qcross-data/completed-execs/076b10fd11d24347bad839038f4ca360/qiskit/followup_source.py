# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_925c46 = Parameter('p_925c46')
p_b15ae8 = Parameter('p_b15ae8')
p_a28ef6 = Parameter('p_a28ef6')
p_40ca7b = Parameter('p_40ca7b')
p_26612a = Parameter('p_26612a')
p_0b1992 = Parameter('p_0b1992')
p_e50c6e = Parameter('p_e50c6e')
p_01d286 = Parameter('p_01d286')
p_635d83 = Parameter('p_635d83')
p_8885ef = Parameter('p_8885ef')
p_60901c = Parameter('p_60901c')
p_2c0ff7 = Parameter('p_2c0ff7')
p_97cf30 = Parameter('p_97cf30')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(11, name='qr')
cr = ClassicalRegister(11, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(ECRGate(), qargs=[qr[2], qr[5]], cargs=[])
subcircuit.append(RZGate(p_0b1992), qargs=[qr[1]], cargs=[])
subcircuit.append(DCXGate(), qargs=[qr[0], qr[5]], cargs=[])
subcircuit.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(RZGate(p_e50c6e), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_635d83), qargs=[qr[6], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(CCXGate(), qargs=[qr[5], qr[9], qr[7]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[7]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[10], qr[6], qr[8]], cargs=[])
qc.append(RZGate(p_60901c), qargs=[qr[0]], cargs=[])
qc.append(CCXGate(), qargs=[qr[7], qr[10], qr[2]], cargs=[])
qc.append(SdgGate(), qargs=[qr[7]], cargs=[])
qc.append(U2Gate(p_01d286, p_2c0ff7), qargs=[qr[10]], cargs=[])
qc.append(CSXGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[7]], cargs=[])
qc.append(CU1Gate(p_a28ef6), qargs=[qr[9], qr[0]], cargs=[])
qc.append(RZGate(p_26612a), qargs=[qr[6]], cargs=[])
qc.append(U2Gate(p_97cf30, p_925c46), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[0]], cargs=[])
qc.append(RZZGate(p_b15ae8), qargs=[qr[4], qr[0]], cargs=[])
qc.append(TGate(), qargs=[qr[0]], cargs=[])
qc.append(TGate(), qargs=[qr[1]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[5]], cargs=[])
qc.append(RZGate(p_8885ef), qargs=[qr[2]], cargs=[])
qc.append(CRZGate(p_40ca7b), qargs=[qr[5], qr[3]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_925c46: 2.1276323672732023, p_b15ae8: 3.950837470808744, p_a28ef6: 4.028174522740928, p_40ca7b: 0.6393443962862078, p_26612a: 5.0063780207098425, p_0b1992: 3.3407994338317226, p_e50c6e: 6.163759533339787, p_01d286: 4.214504315296764, p_635d83: 4.2641612072511235, p_8885ef: 4.722103101046168, p_60901c: 4.229610589867865, p_2c0ff7: 4.6235667602042065, p_97cf30: 2.5163050709890156})
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=['rx', 'ry', 'rz', 'p', 'cx'],
    optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_d3c9324b7370418fb5f96367319b8c48 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_d3c9324b7370418fb5f96367319b8c48, shots=7838).result().get_counts(qc)
RESULT = counts
