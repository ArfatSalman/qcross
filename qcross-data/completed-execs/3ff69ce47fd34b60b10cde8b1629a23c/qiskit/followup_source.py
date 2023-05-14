# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_2f6fa1 = Parameter('p_2f6fa1')
p_d2b7ff = Parameter('p_d2b7ff')
p_796036 = Parameter('p_796036')
p_deb987 = Parameter('p_deb987')
p_f98523 = Parameter('p_f98523')
p_31d9e7 = Parameter('p_31d9e7')
p_7d1017 = Parameter('p_7d1017')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(6, name='qr')
cr = ClassicalRegister(6, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_d2b7ff), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[2], qr[4]], cargs=[])
qc.append(CUGate(p_2f6fa1, p_31d9e7, p_deb987, p_f98523), qargs=[qr[2], qr[3]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[4], qr[0], qr[2]], cargs=[])
qc.append(CCXGate(), qargs=[qr[1], qr[5], qr[0]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[4], qr[3], qr[5], qr[0]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(RZZGate(5.017245588344839), qargs=[qr[0], qr[1]], cargs=[])
subcircuit.append(iSwapGate(), qargs=[qr[3], qr[2]], cargs=[])
subcircuit.append(XGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(CSXGate(), qargs=[qr[0], qr[1]], cargs=[])
subcircuit.append(RCCXGate(), qargs=[qr[4], qr[5], qr[1]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[5], qr[3], qr[4]], cargs=[])
qc.append(SGate(), qargs=[qr[5]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[1], qr[5]], cargs=[])
qc.append(RZGate(p_796036), qargs=[qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[2], qr[1], qr[3]], cargs=[])
qc.append(CU1Gate(3.2142159669963557), qargs=[qr[3], qr[0]], cargs=[])
qc.append(UGate(5.887184334931191, p_7d1017, 1.4112277317699358), qargs=[qr[5]], cargs=[])
qc.append(RZZGate(5.1829934776392745), qargs=[qr[0], qr[5]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_2f6fa1: 0.5112149185250571, p_d2b7ff: 6.163759533339787, p_796036: 4.229610589867865, p_deb987: 2.3864521352475245, p_f98523: 5.987304452123941, p_31d9e7: 5.897054719225356, p_7d1017: 0.07157463504881167})
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_acbd29ba51e74045b8969bc071b85eab = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_acbd29ba51e74045b8969bc071b85eab, shots=1385).result().get_counts(qc)
RESULT = counts
