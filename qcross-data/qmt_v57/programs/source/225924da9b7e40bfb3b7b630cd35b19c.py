
# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter

# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RXXGate(2.4627742512178394), qargs=[qr[4], qr[1]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
qc.append(CPhaseGate(0.18944650038921448), qargs=[qr[2], qr[0]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[1], qr[3], qr[0]], cargs=[])
qc.append(C3XGate(), qargs=[qr[3], qr[2], qr[0], qr[1]], cargs=[])
qc.append(U1Gate(2.995981763732353), qargs=[qr[3]], cargs=[])
qc.append(U3Gate(5.224415207920243,0.15651583077800743,4.618151048803292), qargs=[qr[0]], cargs=[])

# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)

# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_66f693e373654a5fa4fefcf452b9eaeb = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_66f693e373654a5fa4fefcf452b9eaeb, shots=979).result().get_counts(qc)
RESULT = counts