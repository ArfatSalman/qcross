# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_f22bb0 = Parameter('p_f22bb0')
p_c746bf = Parameter('p_c746bf')
p_bd1c3c = Parameter('p_bd1c3c')
p_2c205c = Parameter('p_2c205c')
p_132f3b = Parameter('p_132f3b')
p_72ab38 = Parameter('p_72ab38')
p_d5c708 = Parameter('p_d5c708')
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_72ab38), qargs=[qr[5]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[0], qr[5]], cargs=[])
qc.append(CRXGate(p_d5c708), qargs=[qr[9], qr[3]], cargs=[])
qc.append(CCXGate(), qargs=[qr[6], qr[4], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[8]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(CRZGate(p_f22bb0), qargs=[qr[9], qr[0]], cargs=[])
qc.append(RZGate(p_132f3b), qargs=[qr[9]], cargs=[])
qc.append(SXGate(), qargs=[qr[8]], cargs=[])
qc.append(CSXGate(), qargs=[qr[7], qr[2]], cargs=[])
qc.append(CCXGate(), qargs=[qr[7], qr[4], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[8], qr[7], qr[1], qr[4]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[8]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(CHGate(), qargs=[qr[3], qr[9]], cargs=[])
qc.append(CSXGate(), qargs=[qr[8], qr[1]], cargs=[])
qc.append(CRZGate(p_bd1c3c), qargs=[qr[9], qr[8]], cargs=[])
qc.append(U2Gate(2.5163050709890156, p_2c205c), qargs=[qr[8]], cargs=[])
qc.append(TGate(), qargs=[qr[1]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[4]], cargs=[])
qc.append(TGate(), qargs=[qr[2]], cargs=[])
qc.append(RZGate(p_c746bf), qargs=[qr[9]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_f22bb0: 4.167661441102218, p_c746bf: 5.014941143947427, p_bd1c3c: 2.586208953975239, p_2c205c: 2.1276323672732023, p_132f3b: 4.229610589867865, p_72ab38: 6.163759533339787, p_d5c708: 5.987304452123941})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 4], [0, 9], [0, 10], [1, 0], [1, 14], [2, 9], [2, 13], [3, 9], [4, 0], [4, 5], [5, 4], [6, 8], [7, 13], [8, 6], [8, 9], [8, 12], [9, 0], [9, 2], [9, 3], [9, 8], [10, 0], [11, 14], [12, 8], [13, 2], [13, 7], [14, 1], [14, 11]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_c534b5e0c4974d968b639073f8493fcc = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_c534b5e0c4974d968b639073f8493fcc, shots=5542).result().get_counts(qc)
RESULT = counts
