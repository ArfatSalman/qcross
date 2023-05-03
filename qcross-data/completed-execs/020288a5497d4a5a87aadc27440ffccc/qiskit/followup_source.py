# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr_1 = QuantumRegister(10, name='qr_1')
cr_1 = ClassicalRegister(10, name='cr_1')
qc_1 = QuantumCircuit(qr_1, cr_1, name='qc_1')


qc_1.append(CRZGate(4.2641612072511235), qargs=[qr_1[2], qr_1[1]], cargs=[])
qc_1.append(ZGate(), qargs=[qr_1[0]], cargs=[])


qr_2 = QuantumRegister(1, name='qr_2')
cr_2 = ClassicalRegister(1, name='cr_2')
qc_2 = QuantumCircuit(qr_2, cr_2, name='qc_2')


qc_2.append(RZGate(6.163759533339787), qargs=[qr_2[0]], cargs=[])
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
backend_3dda4bbb43f442a5af3a926d6a28250c = Aer.get_backend('qasm_simulator')
counts_1 = execute(qc_1, backend=backend_3dda4bbb43f442a5af3a926d6a28250c, shots=7838).result().get_counts(qc_1)
counts_2 = execute(qc_2, backend=backend_3dda4bbb43f442a5af3a926d6a28250c, shots=7838).result().get_counts(qc_2)
RESULT = [counts_1, counts_2]
