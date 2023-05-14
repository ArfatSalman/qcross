# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_d25745 = Parameter('p_d25745')
p_7280db = Parameter('p_7280db')
p_66bc6f = Parameter('p_66bc6f')
p_7efb1a = Parameter('p_7efb1a')
p_9e0b52 = Parameter('p_9e0b52')
p_6a275f = Parameter('p_6a275f')
p_a8dc96 = Parameter('p_a8dc96')
p_6c61a4 = Parameter('p_6c61a4')
p_0f968c = Parameter('p_0f968c')
p_55502a = Parameter('p_55502a')
p_74ecdc = Parameter('p_74ecdc')
p_3ebfd3 = Parameter('p_3ebfd3')
p_eb0914 = Parameter('p_eb0914')
p_e304cd = Parameter('p_e304cd')
p_5dbd96 = Parameter('p_5dbd96')
p_0caccb = Parameter('p_0caccb')
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(6, name='qr')
cr = ClassicalRegister(6, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_0caccb), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_9e0b52), qargs=[qr[1], qr[4]], cargs=[])
qc.append(CUGate(p_55502a, p_74ecdc, p_5dbd96, p_66bc6f), qargs=[qr[1], qr[
    3]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[4], qr[0], qr[1]], cargs=[])
qc.append(CCXGate(), qargs=[qr[2], qr[5], qr[0]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[4], qr[3], qr[5], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[5], qr[3], qr[4]], cargs=[])
qc.append(SGate(), qargs=[qr[5]], cargs=[])
qc.append(CRZGate(p_a8dc96), qargs=[qr[2], qr[5]], cargs=[])
qc.append(RZGate(p_6c61a4), qargs=[qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[1], qr[2], qr[3]], cargs=[])
qc.append(CU1Gate(p_3ebfd3), qargs=[qr[3], qr[0]], cargs=[])
qc.append(UGate(p_e304cd, p_0f968c, p_6a275f), qargs=[qr[5]], cargs=[])
qc.append(RZZGate(p_d25745), qargs=[qr[0], qr[5]], cargs=[])
qc.append(SGate(), qargs=[qr[4]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[4]], cargs=[])
qc.append(CRZGate(p_eb0914), qargs=[qr[0], qr[5]], cargs=[])
qc.append(CU1Gate(p_7efb1a), qargs=[qr[2], qr[4]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[3], qr[0], qr[4], qr[1]], cargs=[])
qc.append(CRZGate(p_7280db), qargs=[qr[1], qr[5]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_d25745: 5.1829934776392745, p_7280db: 2.586208953975239, p_66bc6f: 5.987304452123941, p_7efb1a: 4.028174522740928, p_9e0b52: 4.2641612072511235, p_6a275f: 1.4112277317699358, p_a8dc96: 4.167661441102218, p_6c61a4: 4.229610589867865, p_0f968c: 0.07157463504881167, p_55502a: 0.5112149185250571, p_74ecdc: 5.897054719225356, p_3ebfd3: 3.2142159669963557, p_eb0914: 4.833923139882297, p_e304cd: 5.887184334931191, p_5dbd96: 2.3864521352475245, p_0caccb: 6.163759533339787})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_af7b169f2d0842488336f1d546cbf46a = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_af7b169f2d0842488336f1d546cbf46a, shots=1385).result().get_counts(qc)
RESULT = counts
