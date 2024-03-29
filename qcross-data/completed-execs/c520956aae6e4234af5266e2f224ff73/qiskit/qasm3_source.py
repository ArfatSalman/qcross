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
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[6]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[0], qr[6]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: QASM_CONVERSION


from qiskit.qasm3 import loads, dumps
qc = loads(dumps(qc))

# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0,
    1], [0, 4], [0, 5], [0, 6], [1, 0], [2, 6], [2, 8], [3, 8], [4, 0], [5,
    0], [6, 0], [6, 2], [6, 7], [7, 6], [8, 2], [8, 3]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_24f0970c973e4798b1b954a31e63e5ae = Aer.get_backend('aer_simulator_density_matrix')
counts = execute(qc, backend=backend_24f0970c973e4798b1b954a31e63e5ae, shots=2771).result().get_counts(qc)
RESULT = counts
