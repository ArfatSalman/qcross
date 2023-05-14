# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_3603f7 = Parameter('p_3603f7')
p_fd786b = Parameter('p_fd786b')
p_b354cf = Parameter('p_b354cf')
p_a0ebfc = Parameter('p_a0ebfc')
p_27de98 = Parameter('p_27de98')
p_95a7b3 = Parameter('p_95a7b3')
p_91f56a = Parameter('p_91f56a')
p_317aec = Parameter('p_317aec')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(11, name='qr')
cr = ClassicalRegister(11, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_95a7b3), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[6], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(CCXGate(), qargs=[qr[5], qr[9], qr[7]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[7]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[10], qr[6], qr[8]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[0]], cargs=[])
qc.append(CCXGate(), qargs=[qr[7], qr[10], qr[2]], cargs=[])
qc.append(SdgGate(), qargs=[qr[7]], cargs=[])
qc.append(U2Gate(4.214504315296764, p_fd786b), qargs=[qr[10]], cargs=[])
qc.append(CSXGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[7]], cargs=[])
qc.append(CU1Gate(4.028174522740928), qargs=[qr[9], qr[0]], cargs=[])
qc.append(RZGate(p_3603f7), qargs=[qr[6]], cargs=[])
qc.append(U2Gate(p_27de98, p_317aec), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[0]], cargs=[])
qc.append(RZZGate(3.950837470808744), qargs=[qr[4], qr[0]], cargs=[])
qc.append(TGate(), qargs=[qr[0]], cargs=[])
qc.append(TGate(), qargs=[qr[1]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[5]], cargs=[])
qc.append(RZGate(4.722103101046168), qargs=[qr[2]], cargs=[])
qc.append(CRZGate(p_91f56a), qargs=[qr[5], qr[3]], cargs=[])
qc.append(CU1Gate(p_a0ebfc), qargs=[qr[3], qr[8]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[1]], cargs=[])
qc.append(RZGate(p_b354cf), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[8]], cargs=[])
qc.append(CSXGate(), qargs=[qr[7], qr[0]], cargs=[])
qc.append(CU1Gate(3.631024984774394), qargs=[qr[10], qr[7]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_3603f7: 5.0063780207098425, p_fd786b: 4.6235667602042065, p_b354cf: 3.6614081973587154, p_a0ebfc: 2.5476776328466872, p_27de98: 2.5163050709890156, p_95a7b3: 6.163759533339787, p_91f56a: 0.6393443962862078, p_317aec: 2.1276323672732023})
# SECTION
# NAME: QASM_CONVERSION

qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_981264f180354f57b61e610138ffd8b7 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_981264f180354f57b61e610138ffd8b7, shots=7838).result().get_counts(qc)
RESULT = counts
