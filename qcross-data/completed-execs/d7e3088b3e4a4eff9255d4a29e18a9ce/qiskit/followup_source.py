# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_597899 = Parameter('p_597899')
p_300a3c = Parameter('p_300a3c')
p_b934bd = Parameter('p_b934bd')
p_9136a9 = Parameter('p_9136a9')
p_bcf56a = Parameter('p_bcf56a')
p_ee7fe0 = Parameter('p_ee7fe0')
p_9fd00a = Parameter('p_9fd00a')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(4, name='qr')
cr = ClassicalRegister(4, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_bcf56a), qargs=[qr[1]], cargs=[])
qc.append(RZZGate(p_597899), qargs=[qr[2], qr[3]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(CUGate(p_9136a9, p_b934bd, 2.3864521352475245, p_9fd00a), qargs=[qr[0], qr[2]], cargs=[])
qc.append(CU1Gate(p_ee7fe0), qargs=[qr[3], qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[3], qr[2]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(ECRGate(), qargs=[qr[1], qr[3]], cargs=[])
subcircuit.append(U2Gate(6.171674001528992,4.948673314014118), qargs=[qr[0]], cargs=[])
subcircuit.append(SGate(), qargs=[qr[1]], cargs=[])
subcircuit.append(CXGate(), qargs=[qr[0], qr[3]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CHGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[3], qr[0], qr[1], qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[3], qr[1], qr[0], qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[2]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[1], qr[0], qr[3]], cargs=[])
qc.append(RYYGate(p_300a3c), qargs=[qr[2], qr[0]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[2], qr[3], qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_597899: 4.066449154047175, p_300a3c: 1.740253089260498, p_b934bd: 5.897054719225356, p_9136a9: 0.5112149185250571, p_bcf56a: 6.163759533339787, p_ee7fe0: 5.154187354656876, p_9fd00a: 5.987304452123941})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=3, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_5ece2a44284a44bfbb98030c96efd70b = Aer.get_backend('aer_simulator_matrix_product_state')
counts = execute(qc, backend=backend_5ece2a44284a44bfbb98030c96efd70b, shots=692).result().get_counts(qc)
RESULT = counts
