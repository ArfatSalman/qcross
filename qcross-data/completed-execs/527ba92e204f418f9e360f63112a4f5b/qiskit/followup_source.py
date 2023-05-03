# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_07b864 = Parameter('p_07b864')
p_12832b = Parameter('p_12832b')
p_aa27f8 = Parameter('p_aa27f8')
p_5f4a74 = Parameter('p_5f4a74')
p_d0f83e = Parameter('p_d0f83e')
p_6afe18 = Parameter('p_6afe18')
p_6d8eba = Parameter('p_6d8eba')
p_c41e19 = Parameter('p_c41e19')
p_431464 = Parameter('p_431464')
p_96609c = Parameter('p_96609c')
p_990bb6 = Parameter('p_990bb6')
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(7, name='qr')
cr = ClassicalRegister(7, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_990bb6), qargs=[qr[5]], cargs=[])
qc.append(ZGate(), qargs=[qr[4]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(CRXGate(p_12832b), qargs=[qr[0], qr[3]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[4], qr[2], qr[6], qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[5], qr[4]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[0], qr[6], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[4], qr[1]], cargs=[])
qc.append(SdgGate(), qargs=[qr[4]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[0], qr[3], qr[2]], cargs=[])
qc.append(SGate(), qargs=[qr[6]], cargs=[])
qc.append(RZGate(p_6afe18), qargs=[qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[0], qr[6], qr[1]], cargs=[])
qc.append(CU1Gate(p_07b864), qargs=[qr[5], qr[2]], cargs=[])
qc.append(CRXGate(p_431464), qargs=[qr[5], qr[4]], cargs=[])
qc.append(CHGate(), qargs=[qr[5], qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[2], qr[1], qr[5]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_d0f83e), qargs=[qr[2], qr[4]], cargs=[])
qc.append(CU1Gate(4.028174522740928), qargs=[qr[6], qr[5]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[2], qr[3], qr[5]], cargs=[])
qc.append(CRZGate(p_5f4a74), qargs=[qr[4], qr[0]], cargs=[])
qc.append(U2Gate(p_6d8eba, p_c41e19), qargs=[qr[0]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
qc.append(SdgGate(), qargs=[qr[2]], cargs=[])
qc.append(RZZGate(p_96609c), qargs=[qr[1], qr[5]], cargs=[])
qc.append(TGate(), qargs=[qr[5]], cargs=[])
qc.append(RYYGate(p_aa27f8), qargs=[qr[5], qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_07b864: 3.2142159669963557, p_12832b: 2.0099472182748075, p_aa27f8: 1.9669252191306448, p_5f4a74: 2.586208953975239, p_d0f83e: 4.833923139882297, p_6afe18: 4.229610589867865, p_6d8eba: 2.5163050709890156, p_c41e19: 2.1276323672732023, p_431464: 5.94477504571567, p_96609c: 3.950837470808744, p_990bb6: 6.163759533339787})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_85511d9e541a422b82ff406873bc0e8a = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_85511d9e541a422b82ff406873bc0e8a, shots=1959).result().get_counts(qc)
RESULT = counts
