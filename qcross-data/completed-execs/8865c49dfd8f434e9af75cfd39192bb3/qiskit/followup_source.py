# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr_1 = QuantumRegister(2, name='qr_1')
cr_1 = ClassicalRegister(2, name='cr_1')
qc_1 = QuantumCircuit(qr_1, cr_1, name='qc_1')


qc_1.append(RZGate(6.163759533339787), qargs=[qr_1[0]], cargs=[])


qr_2 = QuantumRegister(3, name='qr_2')
cr_2 = ClassicalRegister(3, name='cr_2')
qc_2 = QuantumCircuit(qr_2, cr_2, name='qc_2')


qc_2.append(SXdgGate(), qargs=[qr_2[0]], cargs=[])
qc_2.append(CSXGate(), qargs=[qr_2[2], qr_2[1]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_ed7b21 = QuantumRegister(2, name='qr_ed7b21')
qc_2.add_register(qr_ed7b21)
# SECTION
# NAME: MEASUREMENT

qc_1.measure(qr_1, cr_1)
qc_2.measure(qr_2, cr_2)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc_1 = transpile(qc_1, basis_gates=None, optimization_level=2, coupling_map=None)
qc_2 = transpile(qc_2, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_fae1394190bb403e807dcf9b4be37bd8 = Aer.get_backend('qasm_simulator')
counts_1 = execute(qc_1, backend=backend_fae1394190bb403e807dcf9b4be37bd8, shots=979).result().get_counts(qc_1)
counts_2 = execute(qc_2, backend=backend_fae1394190bb403e807dcf9b4be37bd8, shots=979).result().get_counts(qc_2)
RESULT = [counts_1, counts_2]
