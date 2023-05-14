# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_52c643 = Parameter('p_52c643')
p_827e55 = Parameter('p_827e55')
p_8ff258 = Parameter('p_8ff258')
p_7054b2 = Parameter('p_7054b2')
p_e129ef = Parameter('p_e129ef')
p_11ec22 = Parameter('p_11ec22')
p_d24d8a = Parameter('p_d24d8a')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(4, name='qr')
cr = ClassicalRegister(4, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_e129ef), qargs=[qr[1]], cargs=[])
qc.append(RZZGate(p_52c643), qargs=[qr[2], qr[3]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(CUGate(p_11ec22, p_d24d8a, p_827e55, p_8ff258), qargs=[qr[0], qr[2]], cargs=[])
qc.append(CU1Gate(p_7054b2), qargs=[qr[3], qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[3], qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_52c643: 4.066449154047175, p_827e55: 2.3864521352475245, p_8ff258: 5.987304452123941, p_7054b2: 5.154187354656876, p_e129ef: 6.163759533339787, p_11ec22: 0.5112149185250571, p_d24d8a: 5.897054719225356})
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0,
    1], [0, 3], [1, 0], [1, 4], [2, 4], [2, 5], [3, 0], [4, 1], [4, 2], [5, 2]]
    )
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_0ca2cb96498f4ce9b062ec96ef195048 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_0ca2cb96498f4ce9b062ec96ef195048, shots=692).result().get_counts(qc)
RESULT = counts
