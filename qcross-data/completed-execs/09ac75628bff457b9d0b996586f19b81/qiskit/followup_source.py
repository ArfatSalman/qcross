# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_b2b67d = Parameter('p_b2b67d')
p_4c7bdf = Parameter('p_4c7bdf')
p_543c46 = Parameter('p_543c46')
p_86736a = Parameter('p_86736a')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(6, name='qr')
cr = ClassicalRegister(6, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_543c46), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_86736a), qargs=[qr[2], qr[4]], cargs=[])
qc.append(CUGate(p_b2b67d, p_4c7bdf, 2.3864521352475245, 5.987304452123941), qargs=[qr[2], qr[3]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[4], qr[0], qr[2]], cargs=[])
qc.append(CCXGate(), qargs=[qr[1], qr[5], qr[0]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[4], qr[3], qr[5], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_b2b67d: 0.5112149185250571, p_4c7bdf: 5.897054719225356, p_543c46: 6.163759533339787, p_86736a: 4.2641612072511235})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 4], [1, 0], [1, 2], [2, 1], [3, 4], [3, 5], [4, 0], [4, 3], [5, 3]])
# SECTION
# NAME: QASM_CONVERSION
qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_f8c90c558f644ec0854f03d18a46b242 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_f8c90c558f644ec0854f03d18a46b242, shots=1385).result().get_counts(qc)
RESULT = counts
