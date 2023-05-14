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
p_9de5f6 = Parameter('p_9de5f6')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(6, name='qr')
cr = ClassicalRegister(6, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_9de5f6), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_9de5f6: 6.163759533339787,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 3], [0, 4], [0, 5], [1, 0], [1, 2], [2, 1], [3, 0], [4, 0], [5, 0]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_41868752a9be41d6ac6f5dc1caf5b66f = Aer.get_backend('aer_simulator')
counts = execute(qc, backend=backend_41868752a9be41d6ac6f5dc1caf5b66f, shots=1385).result().get_counts(qc)
RESULT = counts
