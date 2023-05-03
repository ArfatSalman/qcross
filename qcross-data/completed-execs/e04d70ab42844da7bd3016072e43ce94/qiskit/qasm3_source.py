# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_0e7163 = Parameter('p_0e7163')
p_44a409 = Parameter('p_44a409')
p_8270ff = Parameter('p_8270ff')
p_96c96a = Parameter('p_96c96a')
p_796fab = Parameter('p_796fab')
p_8d288b = Parameter('p_8d288b')
p_facb1d = Parameter('p_facb1d')
p_492eef = Parameter('p_492eef')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(6, name='qr')
cr = ClassicalRegister(6, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_44a409), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_8270ff), qargs=[qr[2], qr[4]], cargs=[])
qc.append(CUGate(0.5112149185250571, 5.897054719225356, p_8d288b, 5.987304452123941), qargs=[qr[2], qr[3]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[4], qr[0], qr[2]], cargs=[])
qc.append(CCXGate(), qargs=[qr[1], qr[5], qr[0]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[4], qr[3], qr[5], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[5], qr[3], qr[4]], cargs=[])
qc.append(SGate(), qargs=[qr[5]], cargs=[])
qc.append(CRZGate(p_facb1d), qargs=[qr[1], qr[5]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[2], qr[1], qr[3]], cargs=[])
qc.append(CU1Gate(p_0e7163), qargs=[qr[3], qr[0]], cargs=[])
qc.append(UGate(5.887184334931191, 0.07157463504881167, p_492eef), qargs=[qr[5]], cargs=[])
qc.append(RZZGate(5.1829934776392745), qargs=[qr[0], qr[5]], cargs=[])
qc.append(SGate(), qargs=[qr[4]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[4]], cargs=[])
qc.append(CRZGate(4.833923139882297), qargs=[qr[0], qr[5]], cargs=[])
qc.append(CU1Gate(p_96c96a), qargs=[qr[1], qr[4]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[3], qr[0], qr[4], qr[2]], cargs=[])
qc.append(CRZGate(p_796fab), qargs=[qr[2], qr[5]], cargs=[])
qc.append(CRXGate(2.6687018103754414), qargs=[qr[4], qr[5]], cargs=[])
qc.append(CRZGate(5.742126321682921), qargs=[qr[2], qr[0]], cargs=[])
qc.append(TGate(), qargs=[qr[5]], cargs=[])
qc.append(SdgGate(), qargs=[qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_0e7163: 3.2142159669963557, p_44a409: 6.163759533339787, p_8270ff: 4.2641612072511235, p_96c96a: 4.028174522740928, p_796fab: 2.586208953975239, p_8d288b: 2.3864521352475245, p_facb1d: 4.167661441102218, p_492eef: 1.4112277317699358})
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1, coupling_map=[[0,
    1], [1, 0], [1, 2], [1, 5], [2, 1], [3, 4], [3, 5], [4, 3], [5, 1], [5, 3]]
    )
# SECTION
# NAME: QASM_CONVERSION


from qiskit.qasm3 import loads, dumps
qc = loads(dumps(qc))

# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_22a8b4dc1c79479dadbf80f589cbde88 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_22a8b4dc1c79479dadbf80f589cbde88, shots=1385).result().get_counts(qc)
RESULT = counts
