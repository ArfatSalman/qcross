# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_7b7b65 = Parameter('p_7b7b65')
p_e65c05 = Parameter('p_e65c05')
p_e39fe0 = Parameter('p_e39fe0')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_7b7b65), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[6]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CRZGate(1.0296448789776642), qargs=[qr[1], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[7], qr[6], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(p_e65c05), qargs=[qr[6], qr[7]], cargs=[])
qc.append(CRZGate(p_e39fe0), qargs=[qr[1], qr[7]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_7b7b65: 6.163759533339787, p_e65c05: 1.740253089260498, p_e39fe0: 4.167661441102218})
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0,
    1], [0, 4], [0, 6], [0, 8], [1, 0], [1, 11], [2, 4], [3, 11], [4, 0], [
    4, 2], [4, 9], [5, 9], [6, 0], [7, 9], [8, 0], [9, 4], [9, 5], [9, 7],
    [10, 11], [11, 1], [11, 3], [11, 10]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_7ebb3c9dd4204abbb3296de6db3e8634 = Aer.get_backend('aer_simulator_density_matrix')
counts = execute(qc, backend=backend_7ebb3c9dd4204abbb3296de6db3e8634, shots=2771).result().get_counts(qc)
RESULT = counts
