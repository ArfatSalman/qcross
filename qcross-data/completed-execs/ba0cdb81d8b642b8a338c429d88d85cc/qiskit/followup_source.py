# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_51446f = Parameter('p_51446f')
p_40d80f = Parameter('p_40d80f')
p_2e845a = Parameter('p_2e845a')
p_75570c = Parameter('p_75570c')
p_94fb1b = Parameter('p_94fb1b')
p_002797 = Parameter('p_002797')
p_b6d4eb = Parameter('p_b6d4eb')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(4, name='qr')
cr = ClassicalRegister(4, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_40d80f), qargs=[qr[1]], cargs=[])
qc.append(RZZGate(p_75570c), qargs=[qr[2], qr[3]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(CUGate(p_94fb1b, p_002797, p_51446f, p_b6d4eb), qargs=[qr[0], qr[2]], cargs=[])
qc.append(CU1Gate(p_2e845a), qargs=[qr[3], qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[3], qr[0], qr[1], qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[3], qr[1], qr[0], qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[2]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[1], qr[0], qr[3]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_51446f: 2.3864521352475245, p_40d80f: 6.163759533339787, p_2e845a: 5.154187354656876, p_75570c: 4.066449154047175, p_94fb1b: 0.5112149185250571, p_002797: 5.897054719225356, p_b6d4eb: 5.987304452123941})
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_cc19013cb79546c8bc09ae5fc149c1f0 = Aer.get_backend('aer_simulator_statevector')
counts = execute(qc, backend=backend_cc19013cb79546c8bc09ae5fc149c1f0, shots=692).result().get_counts(qc)
RESULT = counts
