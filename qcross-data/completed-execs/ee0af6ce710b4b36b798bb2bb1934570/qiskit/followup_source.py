# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_1f78f3 = Parameter('p_1f78f3')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(7, name='qr')
cr = ClassicalRegister(7, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_1f78f3), qargs=[qr[4]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_1f78f3: 6.163759533339787})
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=['ccx', 'h'], optimization_level=2,
    coupling_map=[[0, 1], [0, 4], [0, 7], [1, 0], [1, 2], [1, 3], [2, 1], [
    2, 5], [2, 6], [3, 1], [4, 0], [5, 2], [6, 2], [7, 0]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_5dfdcab935194b4ba682e9b07b8a01c1 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_5dfdcab935194b4ba682e9b07b8a01c1, shots=1959).result().get_counts(qc)
RESULT = counts
