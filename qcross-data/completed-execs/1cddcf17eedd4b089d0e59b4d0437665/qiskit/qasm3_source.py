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
qc.append(CYGate(), qargs=[qr[1], qr[7]], cargs=[])
qc.append(SXGate(), qargs=[qr[6]], cargs=[])
qc.append(CU3Gate(0.023756915335071876, 3.9408516686255095, 1.960506194168338), qargs=[qr[3], qr[7]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[4], qr[5], qr[2], qr[6]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=3, coupling_map=None)
# SECTION
# NAME: QASM_CONVERSION


from qiskit.qasm3 import loads, dumps
qc = loads(dumps(qc))

# SECTION
# NAME: EXECUTION
from qiskit import Aer, transpile, execute
backend_a698dbdc336240e3bfa77cdc96dfd0ad = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_a698dbdc336240e3bfa77cdc96dfd0ad, shots=2771).result().get_counts(qc)
RESULT = counts