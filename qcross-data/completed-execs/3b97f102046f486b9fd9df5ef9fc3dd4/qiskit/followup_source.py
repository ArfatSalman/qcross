# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_26bdc5 = Parameter('p_26bdc5')
p_ef51d2 = Parameter('p_ef51d2')
p_b28578 = Parameter('p_b28578')
p_129651 = Parameter('p_129651')
p_ca72f6 = Parameter('p_ca72f6')
p_6111a3 = Parameter('p_6111a3')
p_04934c = Parameter('p_04934c')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(4, name='qr')
cr = ClassicalRegister(4, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_26bdc5), qargs=[qr[1]], cargs=[])
qc.append(RZZGate(p_b28578), qargs=[qr[2], qr[3]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(TdgGate(), qargs=[qr[2]], cargs=[])
subcircuit.append(U1Gate(5.01836135520768), qargs=[qr[1]], cargs=[])
subcircuit.append(CRYGate(4.736752714049485), qargs=[qr[0], qr[3]], cargs=[])
subcircuit.append(RXGate(6.1292830756636185), qargs=[qr[2]], cargs=[])
subcircuit.append(CHGate(), qargs=[qr[2], qr[3]], cargs=[])
subcircuit.append(CXGate(), qargs=[qr[2], qr[0]], cargs=[])
subcircuit.append(RZZGate(3.516607467010828), qargs=[qr[3], qr[1]], cargs=[])
subcircuit.append(PhaseGate(3.2287759437031154), qargs=[qr[1]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(iSwapGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(CUGate(p_ef51d2, p_ca72f6, p_6111a3, p_129651), qargs=[qr[0], qr[2]], cargs=[])
qc.append(CU1Gate(p_04934c), qargs=[qr[3], qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[3], qr[0], qr[1], qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_26bdc5: 6.163759533339787, p_ef51d2: 0.5112149185250571, p_b28578: 4.066449154047175, p_129651: 5.987304452123941, p_ca72f6: 5.897054719225356, p_6111a3: 2.3864521352475245, p_04934c: 5.154187354656876})
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_047d9ba09e684047b9b3f61aa020d7c1 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_047d9ba09e684047b9b3f61aa020d7c1, shots=692).result().get_counts(qc)
RESULT = counts
