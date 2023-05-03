# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_fa6b38 = Parameter('p_fa6b38')
p_b444cc = Parameter('p_b444cc')
p_6274c7 = Parameter('p_6274c7')
p_8b3e71 = Parameter('p_8b3e71')
p_5f6e00 = Parameter('p_5f6e00')
p_3f9d0c = Parameter('p_3f9d0c')
p_df034d = Parameter('p_df034d')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(9, name='qr')
cr = ClassicalRegister(9, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_fa6b38), qargs=[qr[8]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[4]], cargs=[])
qc.append(CUGate(p_6274c7, p_df034d, p_b444cc, p_3f9d0c), qargs=[qr[0], qr[6]], cargs=[])
qc.append(SdgGate(), qargs=[qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[8], qr[7], qr[5]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[5]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[8]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[3], qr[2], qr[0]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(CU1Gate(p_8b3e71), qargs=[qr[8], qr[3]], cargs=[])
qc.append(CRZGate(p_5f6e00), qargs=[qr[5], qr[8]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[7]], cargs=[])
qc.append(CHGate(), qargs=[qr[6], qr[1]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_f74fe2 = QuantumRegister(9, name='qr_f74fe2')
qc.add_register(qr_f74fe2)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_fa6b38: 6.163759533339787, p_b444cc: 2.3864521352475245, p_6274c7: 0.5112149185250571, p_8b3e71: 3.2142159669963557, p_5f6e00: 1.4112277317699358, p_3f9d0c: 5.987304452123941, p_df034d: 5.897054719225356})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_6e567078943e404c908db8c82a87a5b4 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_6e567078943e404c908db8c82a87a5b4, shots=3919).result().get_counts(qc)
RESULT = counts
