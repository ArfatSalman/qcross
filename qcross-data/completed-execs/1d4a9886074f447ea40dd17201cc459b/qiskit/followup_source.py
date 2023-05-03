# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_4a0ceb = Parameter('p_4a0ceb')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_4a0ceb), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_4a0ceb: 6.163759533339787})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 2], [0, 5], [0, 7], [0, 8], [1, 0], [1, 6], [1, 10], [2, 0], [3, 10], [4, 8], [5, 0], [6, 1], [7, 0], [8, 0], [8, 4], [9, 10], [10, 1], [10, 3], [10, 9]])
# SECTION
# NAME: EXECUTION
from qiskit import Aer, transpile, execute
backend_18b6238901fe4ec2ba93360cd98541f0 = Aer.get_backend(
    'statevector_simulator')
counts = execute(qc, backend=backend_18b6238901fe4ec2ba93360cd98541f0,
    shots=2771).result().get_counts(qc)
RESULT = counts
