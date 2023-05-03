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
p_c3b88e = Parameter('p_c3b88e')
p_6af2ec = Parameter('p_6af2ec')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(4, name='qr')
cr = ClassicalRegister(4, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[1]], cargs=[])
qc.append(RZZGate(4.066449154047175), qargs=[qr[2], qr[3]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(CUGate(p_c3b88e, p_6af2ec, 2.3864521352475245, 5.987304452123941),
    qargs=[qr[0], qr[2]], cargs=[])
qc.append(CU1Gate(5.154187354656876), qargs=[qr[3], qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[3], qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_c3b88e: 0.5112149185250571,
    p_6af2ec: 5.897054719225356,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 4], [1, 0], [1, 2], [2, 1], [2, 5], [3, 4], [4, 0], [4, 3], [5, 2]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_67a25246b8d54b82ac918a314b0ee1de = Aer.get_backend('aer_simulator_matrix_product_state')
counts = execute(qc, backend=backend_67a25246b8d54b82ac918a314b0ee1de, shots=692).result().get_counts(qc)
RESULT = counts
