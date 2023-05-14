# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_98235d = Parameter('p_98235d')
p_a82456 = Parameter('p_a82456')
p_2c89fd = Parameter('p_2c89fd')
p_878d4a = Parameter('p_878d4a')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(4, name='qr')
cr = ClassicalRegister(4, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[1]], cargs=[])
qc.append(RZZGate(4.066449154047175), qargs=[qr[2], qr[3]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(CUGate(p_878d4a, 5.897054719225356, p_98235d, p_a82456), qargs=[qr[0], qr[2]], cargs=[])
qc.append(CU1Gate(p_2c89fd), qargs=[qr[3], qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[3], qr[0], qr[1], qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[3], qr[1], qr[0], qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[2]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_02b267 = QuantumRegister(4, name='qr_02b267')
qc.add_register(qr_02b267)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_98235d: 2.3864521352475245, p_a82456: 5.987304452123941, p_2c89fd: 5.154187354656876, p_878d4a: 0.5112149185250571})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=None)
# SECTION
# NAME: EXECUTION
from qiskit import Aer, transpile, execute
backend_1492648ce9534c56b080743e55c8b85c = Aer.get_backend('aer_simulator')
counts = execute(qc, backend=backend_1492648ce9534c56b080743e55c8b85c,
    shots=692).result().get_counts(qc)
RESULT = counts
