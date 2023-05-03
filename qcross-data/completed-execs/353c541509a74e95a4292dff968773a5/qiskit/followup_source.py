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
p_ca4ae7 = Parameter('p_ca4ae7')
p_350212 = Parameter('p_350212')
p_3be268 = Parameter('p_3be268')
p_e86f21 = Parameter('p_e86f21')
p_8cc9b1 = Parameter('p_8cc9b1')
p_09c913 = Parameter('p_09c913')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(4, name='qr')
cr = ClassicalRegister(4, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_ca4ae7), qargs=[qr[1]], cargs=[])
qc.append(RZZGate(p_e86f21), qargs=[qr[2], qr[3]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(CUGate(p_350212, p_8cc9b1, p_09c913, 5.987304452123941), qargs=[
    qr[0], qr[2]], cargs=[])
qc.append(CU1Gate(5.154187354656876), qargs=[qr[3], qr[0]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CXGate(), qargs=[qr[3], qr[0]], cargs=[])
subcircuit.append(RZGate(p_3be268), qargs=[qr[2]], cargs=[])
subcircuit.append(TdgGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(HGate(), qargs=[qr[1]], cargs=[])
subcircuit.append(CU1Gate(4.229610589867865), qargs=[qr[1], qr[3]], cargs=[])
subcircuit.append(ECRGate(), qargs=[qr[1], qr[3]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CHGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[3], qr[0], qr[1], qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[3], qr[1], qr[0], qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[2]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_ca4ae7: 6.163759533339787,
    p_350212: 0.5112149185250571,
    p_3be268: 3.8580685613059242,
    p_e86f21: 4.066449154047175,
    p_8cc9b1: 5.897054719225356,
    p_09c913: 2.3864521352475245,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_ce1a41a5a7464ce5bf365213644cdef6 = Aer.get_backend('aer_simulator_matrix_product_state')
counts = execute(qc, backend=backend_ce1a41a5a7464ce5bf365213644cdef6, shots=692).result().get_counts(qc)
RESULT = counts
