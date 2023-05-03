# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_9d7979 = Parameter('p_9d7979')
p_bddf4b = Parameter('p_bddf4b')
p_8e5ef3 = Parameter('p_8e5ef3')
p_b8849a = Parameter('p_b8849a')
p_40773a = Parameter('p_40773a')
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(CRXGate(p_40773a), qargs=[qr[6], qr[0]], cargs=[])
qc.append(CRZGate(p_8e5ef3), qargs=[qr[5], qr[0]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[6], qr[4], qr[0], qr[1]], cargs=[])
qc.append(ZGate(), qargs=[qr[7]], cargs=[])
qc.append(XGate(), qargs=[qr[5]], cargs=[])
qc.append(RYYGate(p_b8849a), qargs=[qr[0], qr[4]], cargs=[])
qc.append(CRZGate(p_bddf4b), qargs=[qr[5], qr[4]], cargs=[])
qc.append(RZGate(p_9d7979), qargs=[qr[5]], cargs=[])
qc.append(SXGate(), qargs=[qr[6]], cargs=[])
qc.append(CU1Gate(3.2142159669963557), qargs=[qr[2], qr[6]], cargs=[])
qc.append(CRXGate(5.94477504571567), qargs=[qr[0], qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_9d7979: 4.229610589867865, p_bddf4b: 4.167661441102218, p_8e5ef3: 1.0296448789776642, p_b8849a: 1.740253089260498, p_40773a: 5.987304452123941})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=3, coupling_map=[[0, 1], [0, 6], [1, 0], [1, 2], [1, 3], [1, 7], [2, 1], [3, 1], [3, 9], [4, 9], [5, 6], [6, 0], [6, 5], [7, 1], [7, 8], [8, 7], [9, 3], [9, 4]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_0b6e5c05d99d43ff87bac68c2ed89993 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_0b6e5c05d99d43ff87bac68c2ed89993, shots=2771).result().get_counts(qc)
RESULT = counts
