# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(SGate(), qargs=[qr[4]], cargs=[])
subcircuit.append(C4XGate(), qargs=[qr[1], qr[7], qr[4], qr[3], qr[6]], cargs=[])
subcircuit.append(HGate(), qargs=[qr[1]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 5], [1, 0], [1, 7], [2, 8], [3, 6], [4, 6], [5, 0], [5, 10], [6, 3], [6, 4], [6, 7], [7, 1], [7, 6], [7, 8], [8, 2], [8, 7], [9, 10], [10, 5], [10, 9]])
# SECTION
# NAME: EXECUTION
from qiskit import Aer, transpile, execute
backend_bf862e6e4dff473fbdc72faa76e8ed07 = Aer.get_backend(
    'aer_simulator_matrix_product_state')
counts = execute(qc, backend=backend_bf862e6e4dff473fbdc72faa76e8ed07,
    shots=2771).result().get_counts(qc)
RESULT = counts
