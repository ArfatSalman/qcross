# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_a97204 = Parameter('p_a97204')
p_c78fcf = Parameter('p_c78fcf')
p_209b89 = Parameter('p_209b89')
p_f92e12 = Parameter('p_f92e12')
p_0564dd = Parameter('p_0564dd')
p_e4c2ac = Parameter('p_e4c2ac')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(9, name='qr')
cr = ClassicalRegister(9, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_a97204), qargs=[qr[8]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[4]], cargs=[])
qc.append(CUGate(p_209b89, p_0564dd, 2.3864521352475245, 5.987304452123941), qargs=[qr[0], qr[6]], cargs=[])
qc.append(SdgGate(), qargs=[qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[8], qr[7], qr[5]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[5]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[8]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[3], qr[2], qr[0]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(CU1Gate(3.2142159669963557), qargs=[qr[8], qr[3]], cargs=[])
qc.append(CRZGate(p_c78fcf), qargs=[qr[5], qr[8]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[7]], cargs=[])
qc.append(CHGate(), qargs=[qr[6], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[3], qr[0]], cargs=[])
qc.append(CRZGate(p_e4c2ac), qargs=[qr[1], qr[2]], cargs=[])
qc.append(U2Gate(p_f92e12, 2.1276323672732023), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[8]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_173848 = QuantumRegister(3, name='qr_173848')
qc.add_register(qr_173848)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_a97204: 6.163759533339787, p_c78fcf: 1.4112277317699358, p_209b89: 0.5112149185250571, p_f92e12: 2.5163050709890156, p_0564dd: 5.897054719225356, p_e4c2ac: 2.586208953975239})
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_c501a2035c0e4b8d8a3ddc85db8ad4b7 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_c501a2035c0e4b8d8a3ddc85db8ad4b7, shots=3919).result().get_counts(qc)
RESULT = counts
