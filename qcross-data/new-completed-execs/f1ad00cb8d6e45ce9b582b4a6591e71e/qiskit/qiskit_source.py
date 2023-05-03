
# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter

# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(TdgGate(), qargs=[qr[1]], cargs=[])
qc.append(CRYGate(0.8476513988624245), qargs=[qr[4], qr[0]], cargs=[])
qc.append(CU1Gate(1.5710197357755318), qargs=[qr[3], qr[2]], cargs=[])
qc.append(TdgGate(), qargs=[qr[2]], cargs=[])
qc.append(TdgGate(), qargs=[qr[1]], cargs=[])
qc.append(CCZGate(), qargs=[qr[2], qr[1], qr[3]], cargs=[])
qc.append(UGate(0.708502006099043,2.97765669736744,5.6444063351584415), qargs=[qr[2]], cargs=[])
qc.append(CPhaseGate(5.597667172921795), qargs=[qr[3], qr[4]], cargs=[])
qc.append(SXGate(), qargs=[qr[2]], cargs=[])
qc.append(CRYGate(0.3177314062860099), qargs=[qr[4], qr[1]], cargs=[])
qc.append(CU1Gate(1.9730677082046415), qargs=[qr[4], qr[2]], cargs=[])

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
backend_b1df125757c44a908a68e42ab2f8cb56 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_b1df125757c44a908a68e42ab2f8cb56, shots=979).result().get_counts(qc)
RESULT = counts