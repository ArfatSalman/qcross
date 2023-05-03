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
p_2bf712 = Parameter('p_2bf712')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(11, name='qr')
cr = ClassicalRegister(11, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_2bf712), qargs=[qr[3]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_2bf712: 6.163759533339787,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 2], [0, 7], [0, 8], [1, 0], [1, 3], [1, 10], [1, 13], [2, 0], [2, 9], [2, 14], [3, 1], [3, 14], [4, 11], [4, 13], [5, 7], [5, 11], [5, 13], [6, 14], [7, 0], [7, 5], [7, 8], [7, 11], [8, 0], [8, 7], [8, 10], [9, 2], [10, 1], [10, 8], [11, 4], [11, 5], [11, 7], [11, 12], [11, 13], [12, 11], [13, 1], [13, 4], [13, 5], [13, 11], [14, 2], [14, 3], [14, 6]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_c18e3ccebdcf401baa90918aefbdd7ea = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_c18e3ccebdcf401baa90918aefbdd7ea, shots=7838).result().get_counts(qc)
RESULT = counts
