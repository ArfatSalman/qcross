# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_97fd86 = Parameter('p_97fd86')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_97fd86), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_97fd86: 6.163759533339787})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 2], [0, 4], [0, 7], [1, 0], [1, 6], [2, 0], [2, 5], [3, 4], [4, 0], [4, 3], [4, 8], [5, 2], [6, 1], [7, 0], [8, 4]])
# SECTION
# NAME: EXECUTION
from qiskit import Aer, transpile, execute
backend_2af62e90478d436893ec3fc93522c313 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_2af62e90478d436893ec3fc93522c313,
    shots=2771).result().get_counts(qc)
RESULT = counts
