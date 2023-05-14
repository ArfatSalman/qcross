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
p_8f5281 = Parameter('p_8f5281')
p_39dba4 = Parameter('p_39dba4')
p_5f2994 = Parameter('p_5f2994')
p_b6dc31 = Parameter('p_b6dc31')
p_078f44 = Parameter('p_078f44')
p_7ad57d = Parameter('p_7ad57d')
p_bb9f8c = Parameter('p_bb9f8c')
p_31d873 = Parameter('p_31d873')
p_ab882a = Parameter('p_ab882a')
p_3d1a45 = Parameter('p_3d1a45')
p_14147f = Parameter('p_14147f')
p_584aac = Parameter('p_584aac')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(9, name='qr')
cr = ClassicalRegister(9, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_bb9f8c), qargs=[qr[8]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[4]], cargs=[])
qc.append(CUGate(p_8f5281, p_b6dc31, p_ab882a, p_31d873), qargs=[qr[0], qr[
    6]], cargs=[])
qc.append(SdgGate(), qargs=[qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[8], qr[7], qr[5]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[5]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[8]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[3], qr[2], qr[0]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(CU1Gate(p_078f44), qargs=[qr[8], qr[3]], cargs=[])
qc.append(CRZGate(p_7ad57d), qargs=[qr[5], qr[8]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CSwapGate(), qargs=[qr[0], qr[6], qr[5]], cargs=[])
subcircuit.append(CSXGate(), qargs=[qr[6], qr[1]], cargs=[])
subcircuit.append(SXGate(), qargs=[qr[3]], cargs=[])
subcircuit.append(SXdgGate(), qargs=[qr[6]], cargs=[])
subcircuit.append(RYYGate(p_3d1a45), qargs=[qr[0], qr[4]], cargs=[])
subcircuit.append(iSwapGate(), qargs=[qr[5], qr[7]], cargs=[])
subcircuit.append(UGate(p_39dba4, p_14147f, p_5f2994), qargs=[qr[3]], cargs=[])
subcircuit.append(PhaseGate(p_584aac), qargs=[qr[8]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_8f5281: 0.5112149185250571,
    p_39dba4: 2.438459595578943,
    p_5f2994: 3.4232119351142516,
    p_b6dc31: 5.897054719225356,
    p_078f44: 3.2142159669963557,
    p_7ad57d: 1.4112277317699358,
    p_bb9f8c: 6.163759533339787,
    p_31d873: 5.987304452123941,
    p_ab882a: 2.3864521352475245,
    p_3d1a45: 0.6724371252296606,
    p_14147f: 3.326780904591333,
    p_584aac: 0.4827903095199283,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_f787c372005f47a198a9bc98f8ce3fc1 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_f787c372005f47a198a9bc98f8ce3fc1, shots=3919).result().get_counts(qc)
RESULT = counts
