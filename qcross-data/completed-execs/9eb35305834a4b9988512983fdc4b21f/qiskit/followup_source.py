# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS
# SECTION
# NAME: PARAMETERS
p_a2a414 = Parameter('p_a2a414')
p_560035 = Parameter('p_560035')
p_47c65c = Parameter('p_47c65c')
p_0a6c0e = Parameter('p_0a6c0e')
p_fa3e46 = Parameter('p_fa3e46')
p_26dfb8 = Parameter('p_26dfb8')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(9, name='qr')
cr = ClassicalRegister(9, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_0a6c0e), qargs=[qr[8]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[4]], cargs=[])
qc.append(CUGate(p_a2a414, p_560035, p_26dfb8, p_47c65c), qargs=[qr[0], qr[
    6]], cargs=[])
qc.append(SdgGate(), qargs=[qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[8], qr[7], qr[5]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[5]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[8]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[3], qr[2], qr[0]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(CU1Gate(p_fa3e46), qargs=[qr[8], qr[3]], cargs=[])
qc.append(CRZGate(1.4112277317699358), qargs=[qr[5], qr[8]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[7]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_a2a414: 0.5112149185250571,
    p_560035: 5.897054719225356,
    p_47c65c: 5.987304452123941,
    p_0a6c0e: 6.163759533339787,
    p_fa3e46: 3.2142159669963557,
    p_26dfb8: 2.3864521352475245,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=3, coupling_map=[[0, 1], [0, 6], [1, 0], [1, 2], [1, 3], [1, 5], [2, 1], [3, 1], [4, 9], [5, 1], [5, 8], [5, 9], [6, 0], [7, 8], [7, 10], [8, 5], [8, 7], [9, 4], [9, 5], [10, 7]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_811d141f489447518b874f96efefbd0b = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_811d141f489447518b874f96efefbd0b, shots=3919).result().get_counts(qc)
RESULT = counts
