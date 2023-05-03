
# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter

# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(2, name='qr')
cr = ClassicalRegister(2, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(UGate(1.0932143214299395,6.100531540039404,4.859714896792146), qargs=[qr[1]], cargs=[])
qc.append(CYGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(RXGate(4.335996068527454), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[1]], cargs=[])
qc.append(RXGate(6.070601620234646), qargs=[qr[0]], cargs=[])
qc.append(RZXGate(3.9660842997699097), qargs=[qr[0], qr[1]], cargs=[])
qc.append(HGate(), qargs=[qr[1]], cargs=[])

# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1, coupling_map=None)

# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_5d6a769fcdcd4d108cb39014668c0094 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_5d6a769fcdcd4d108cb39014668c0094, shots=346).result().get_counts(qc)
RESULT = counts