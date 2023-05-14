# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_830596 = Parameter('p_830596')
p_e2029e = Parameter('p_e2029e')
p_fa1a24 = Parameter('p_fa1a24')
p_a95f84 = Parameter('p_a95f84')
p_b2df8c = Parameter('p_b2df8c')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(6, name='qr')
cr = ClassicalRegister(6, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_fa1a24), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[2], qr[4]], cargs=[])
qc.append(CUGate(p_a95f84, p_b2df8c, p_830596, p_e2029e), qargs=[qr[2], qr[3]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[4], qr[0], qr[2]], cargs=[])
qc.append(CCXGate(), qargs=[qr[1], qr[5], qr[0]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[4], qr[3], qr[5], qr[0]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CU3Gate(1.2827690425732097,1.3283826543858017,3.672121211148789), qargs=[qr[2], qr[5]], cargs=[])
subcircuit.append(TGate(), qargs=[qr[1]], cargs=[])
subcircuit.append(CUGate(4.229610589867865,2.696266694818697,5.631160518436971,2.9151388486514547), qargs=[qr[0], qr[3]], cargs=[])
subcircuit.append(TGate(), qargs=[qr[2]], cargs=[])
subcircuit.append(RZXGate(4.563562108824195), qargs=[qr[4], qr[0]], cargs=[])
subcircuit.append(C3XGate(5.94477504571567), qargs=[qr[4], qr[5], qr[2], qr[1]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_830596: 2.3864521352475245, p_e2029e: 5.987304452123941, p_fa1a24: 6.163759533339787, p_a95f84: 0.5112149185250571, p_b2df8c: 5.897054719225356})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_4365eb2e84b746b6b18ec0429d1b6d7d = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_4365eb2e84b746b6b18ec0429d1b6d7d, shots=1385).result().get_counts(qc)
RESULT = counts
