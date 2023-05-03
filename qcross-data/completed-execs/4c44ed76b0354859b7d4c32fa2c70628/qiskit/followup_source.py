# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(11, name='qr')
cr = ClassicalRegister(11, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[0]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[4], qr[10]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(CCXGate(), qargs=[qr[9], qr[6], qr[8]], cargs=[])
qc.append(ZGate(), qargs=[qr[10]], cargs=[])
qc.append(XGate(), qargs=[qr[8]], cargs=[])
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
backend_330dc532a3734fab935fbd34b1bf3041 = Aer.get_backend('aer_simulator_matrix_product_state')
counts = execute(qc, backend=backend_330dc532a3734fab935fbd34b1bf3041, shots=7838).result().get_counts(qc)
RESULT = counts
