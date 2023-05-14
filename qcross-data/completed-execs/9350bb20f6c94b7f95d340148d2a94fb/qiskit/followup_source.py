# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_76b5c9 = Parameter('p_76b5c9')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(2, name='qr')
cr = ClassicalRegister(2, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZZGate(p_76b5c9), qargs=[qr[1], qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_76b5c9: 6.163759533339787})
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=['ccx', 'h'], optimization_level=3,
    coupling_map=[[0, 1], [0, 2], [1, 0], [2, 0]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_6c0ef4b69f5a41799c2e4b62d10642d7 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_6c0ef4b69f5a41799c2e4b62d10642d7, shots=346).result().get_counts(qc)
RESULT = counts
