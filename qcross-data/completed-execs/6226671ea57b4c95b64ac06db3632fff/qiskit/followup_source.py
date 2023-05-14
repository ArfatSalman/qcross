# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_7f87cd = Parameter('p_7f87cd')
p_6e3856 = Parameter('p_6e3856')
p_cb84fc = Parameter('p_cb84fc')
p_85980f = Parameter('p_85980f')
p_d1f1d7 = Parameter('p_d1f1d7')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(6, name='qr')
cr = ClassicalRegister(6, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_7f87cd), qargs=[qr[2], qr[4]], cargs=[])
qc.append(CUGate(p_cb84fc, 5.897054719225356, 2.3864521352475245, p_85980f), qargs=[qr[2], qr[3]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[4], qr[0], qr[2]], cargs=[])
qc.append(CCXGate(), qargs=[qr[1], qr[5], qr[0]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[4], qr[3], qr[5], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[5], qr[3], qr[4]], cargs=[])
qc.append(SGate(), qargs=[qr[5]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[1], qr[5]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[2], qr[1], qr[3]], cargs=[])
qc.append(CU1Gate(3.2142159669963557), qargs=[qr[3], qr[0]], cargs=[])
qc.append(UGate(5.887184334931191, 0.07157463504881167, 1.4112277317699358), qargs=[qr[5]], cargs=[])
qc.append(RZZGate(5.1829934776392745), qargs=[qr[0], qr[5]], cargs=[])
qc.append(SGate(), qargs=[qr[4]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[4]], cargs=[])
qc.append(CRZGate(4.833923139882297), qargs=[qr[0], qr[5]], cargs=[])
qc.append(CU1Gate(4.028174522740928), qargs=[qr[1], qr[4]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[3], qr[0], qr[4], qr[2]], cargs=[])
qc.append(CRZGate(p_6e3856), qargs=[qr[2], qr[5]], cargs=[])
qc.append(CRXGate(2.6687018103754414), qargs=[qr[4], qr[5]], cargs=[])
qc.append(CRZGate(p_d1f1d7), qargs=[qr[2], qr[0]], cargs=[])
qc.append(TGate(), qargs=[qr[5]], cargs=[])
qc.append(SdgGate(), qargs=[qr[0]], cargs=[])
qc.append(RZZGate(3.950837470808744), qargs=[qr[3], qr[4]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_b40f69 = QuantumRegister(10, name='qr_b40f69')
qc.add_register(qr_b40f69)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_7f87cd: 4.2641612072511235, p_6e3856: 2.586208953975239, p_cb84fc: 0.5112149185250571, p_85980f: 5.987304452123941, p_d1f1d7: 5.742126321682921})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_c0d06a1de20c456cb7fe0b622507be59 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_c0d06a1de20c456cb7fe0b622507be59, shots=1385).result().get_counts(qc)
RESULT = counts
