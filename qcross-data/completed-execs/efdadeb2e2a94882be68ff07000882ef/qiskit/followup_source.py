# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_4470c9 = Parameter('p_4470c9')
p_56e60c = Parameter('p_56e60c')
p_f8c16b = Parameter('p_f8c16b')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_56e60c), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[6]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(RC3XGate(), qargs=[qr[4], qr[6], qr[7], qr[5]], cargs=[])
subcircuit.append(DCXGate(), qargs=[qr[5], qr[2]], cargs=[])
subcircuit.append(RYGate(3.393897726708824), qargs=[qr[2]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CRXGate(5.987304452123941), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CRZGate(1.0296448789776642), qargs=[qr[1], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[7], qr[6], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(1.740253089260498), qargs=[qr[6], qr[7]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[1], qr[7]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(CU1Gate(p_f8c16b), qargs=[qr[4], qr[0]], cargs=[])
qc.append(CRXGate(5.94477504571567), qargs=[qr[6], qr[4]], cargs=[])
qc.append(RZZGate(p_4470c9), qargs=[qr[7], qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_4470c9: 5.1829934776392745, p_56e60c: 6.163759533339787, p_f8c16b: 3.2142159669963557})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 2], [0, 8], [1, 0], [1, 5], [2, 0], [3, 4], [3, 7], [3, 8], [3, 10], [4, 3], [4, 9], [5, 1], [6, 8], [7, 3], [8, 0], [8, 3], [8, 6], [9, 4], [9, 11], [10, 3], [11, 9]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_cc0886f809d347789efd27a53a60edab = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_cc0886f809d347789efd27a53a60edab, shots=2771).result().get_counts(qc)
RESULT = counts
