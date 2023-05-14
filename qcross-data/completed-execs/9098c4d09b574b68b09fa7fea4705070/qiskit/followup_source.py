# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_eed10c = Parameter('p_eed10c')
p_55f179 = Parameter('p_55f179')
p_3b8fbf = Parameter('p_3b8fbf')
p_0989aa = Parameter('p_0989aa')
p_d3bd13 = Parameter('p_d3bd13')
p_c0fb12 = Parameter('p_c0fb12')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(6, name='qr')
cr = ClassicalRegister(6, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_3b8fbf), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_0989aa), qargs=[qr[2], qr[4]], cargs=[])
qc.append(CUGate(p_eed10c, p_c0fb12, p_d3bd13, p_55f179), qargs=[qr[2], qr[3]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[4], qr[0], qr[2]], cargs=[])
qc.append(CCXGate(), qargs=[qr[1], qr[5], qr[0]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[4], qr[3], qr[5], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[5], qr[3], qr[4]], cargs=[])
qc.append(SGate(), qargs=[qr[5]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_d7d03d = QuantumRegister(9, name='qr_d7d03d')
qc.add_register(qr_d7d03d)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_eed10c: 0.5112149185250571, p_55f179: 5.987304452123941, p_3b8fbf: 6.163759533339787, p_0989aa: 4.2641612072511235, p_d3bd13: 2.3864521352475245, p_c0fb12: 5.897054719225356})
# SECTION
# NAME: QASM_CONVERSION

qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=['cx', 'h', 's', 't'], optimization_level=2,
    coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_de7f63a4aca04cb88e86004add2818c3 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_de7f63a4aca04cb88e86004add2818c3, shots=1385).result().get_counts(qc)
RESULT = counts
