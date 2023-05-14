# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_b6dd52 = Parameter('p_b6dd52')
p_02ac66 = Parameter('p_02ac66')
p_f623a3 = Parameter('p_f623a3')
p_57e546 = Parameter('p_57e546')
p_e01555 = Parameter('p_e01555')
p_3851a3 = Parameter('p_3851a3')
p_736182 = Parameter('p_736182')
p_8b193d = Parameter('p_8b193d')
p_0d1cd9 = Parameter('p_0d1cd9')
p_5da4d4 = Parameter('p_5da4d4')
p_414184 = Parameter('p_414184')
p_2096e5 = Parameter('p_2096e5')
p_b24006 = Parameter('p_b24006')
p_304e0e = Parameter('p_304e0e')
p_d9a218 = Parameter('p_d9a218')
p_8522da = Parameter('p_8522da')
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(6, name='qr')
cr = ClassicalRegister(6, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_3851a3), qargs=[qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[4]], cargs=[])
qc.append(CRZGate(p_2096e5), qargs=[qr[1], qr[2]], cargs=[])
qc.append(CUGate(p_f623a3, 5.897054719225356, p_57e546, p_b24006), qargs=[
    qr[1], qr[4]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[3], qr[2], qr[0], qr[1]], cargs=[])
qc.append(CCXGate(), qargs=[qr[3], qr[5], qr[0]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[4], qr[5], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(TGate(), qargs=[qr[2]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[5], qr[4], qr[2]], cargs=[])
qc.append(SGate(), qargs=[qr[5]], cargs=[])
qc.append(CRZGate(p_d9a218), qargs=[qr[3], qr[5]], cargs=[])
qc.append(RZGate(p_8b193d), qargs=[qr[3]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[1], qr[3], qr[4]], cargs=[])
qc.append(CU1Gate(p_e01555), qargs=[qr[4], qr[0]], cargs=[])
qc.append(UGate(p_736182, p_5da4d4, p_304e0e), qargs=[qr[5]], cargs=[])
qc.append(RZZGate(p_02ac66), qargs=[qr[0], qr[5]], cargs=[])
qc.append(SGate(), qargs=[qr[2]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(CRZGate(p_414184), qargs=[qr[0], qr[5]], cargs=[])
qc.append(CU1Gate(p_b6dd52), qargs=[qr[3], qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[4], qr[0], qr[2], qr[1]], cargs=[])
qc.append(CRZGate(p_8522da), qargs=[qr[1], qr[5]], cargs=[])
qc.append(CRXGate(p_0d1cd9), qargs=[qr[2], qr[5]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_b6dd52: 4.028174522740928, p_02ac66: 5.1829934776392745, p_f623a3: 0.5112149185250571, p_57e546: 2.3864521352475245, p_e01555: 3.2142159669963557, p_3851a3: 6.163759533339787, p_736182: 5.887184334931191, p_8b193d: 4.229610589867865, p_0d1cd9: 2.6687018103754414, p_5da4d4: 0.07157463504881167, p_414184: 4.833923139882297, p_2096e5: 4.2641612072511235, p_b24006: 5.987304452123941, p_304e0e: 1.4112277317699358, p_d9a218: 4.167661441102218, p_8522da: 2.586208953975239})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_94dd4be6d7824e769761509b4151305a = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_94dd4be6d7824e769761509b4151305a, shots=1385).result().get_counts(qc)
RESULT = counts
