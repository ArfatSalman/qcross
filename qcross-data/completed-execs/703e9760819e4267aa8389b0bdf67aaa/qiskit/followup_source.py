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
p_94d012 = Parameter('p_94d012')
p_7f95e9 = Parameter('p_7f95e9')
p_97b6e3 = Parameter('p_97b6e3')
p_3bb993 = Parameter('p_3bb993')
p_3ab710 = Parameter('p_3ab710')
p_77c43b = Parameter('p_77c43b')
p_3c804b = Parameter('p_3c804b')
p_5a4f4d = Parameter('p_5a4f4d')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(9, name='qr')
cr = ClassicalRegister(9, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_7f95e9), qargs=[qr[8]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(RZGate(p_77c43b), qargs=[qr[0]], cargs=[])
subcircuit.append(CZGate(), qargs=[qr[5], qr[0]], cargs=[])
subcircuit.append(U1Gate(p_5a4f4d), qargs=[qr[0]], cargs=[])
subcircuit.append(ECRGate(), qargs=[qr[3], qr[0]], cargs=[])
subcircuit.append(U2Gate(p_97b6e3, p_3bb993), qargs=[qr[6]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CSXGate(), qargs=[qr[2], qr[4]], cargs=[])
qc.append(CUGate(p_3ab710, 5.897054719225356, p_94d012, p_3c804b), qargs=[
    qr[0], qr[6]], cargs=[])
qc.append(SdgGate(), qargs=[qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[8], qr[7], qr[5]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[5]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_8e3ddb = QuantumRegister(5, name='qr_8e3ddb')
subcircuit.add_register(qr_8e3ddb)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_94d012: 2.3864521352475245,
    p_7f95e9: 6.163759533339787,
    p_97b6e3: 5.887184334931191,
    p_3bb993: 0.07157463504881167,
    p_3ab710: 0.5112149185250571,
    p_77c43b: 3.672121211148789,
    p_3c804b: 5.987304452123941,
    p_5a4f4d: 6.2047416485134805,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_891cc4ab55304443822a123fc3eaaa1e = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_891cc4ab55304443822a123fc3eaaa1e, shots=3919).result().get_counts(qc)
RESULT = counts
