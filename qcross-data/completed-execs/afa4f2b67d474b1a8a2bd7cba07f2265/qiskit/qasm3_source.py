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
qc.append(RZGate(6.163759533339787), qargs=[qr[4]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=3, coupling_map=[[0, 1], [0, 4], [0, 7], [1, 0], [1, 2], [1, 3], [2, 1], [2, 5], [2, 6], [3, 1], [4, 0], [5, 2], [6, 2], [7, 0]])
# SECTION
# NAME: QASM_CONVERSION

from qiskit.qasm3 import loads, dumps
qc = loads(dumps(qc))

# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_cdc3143ef8444e1b9943ff9dce595959 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_cdc3143ef8444e1b9943ff9dce595959, shots=2771).result().get_counts(qc)
RESULT = counts
