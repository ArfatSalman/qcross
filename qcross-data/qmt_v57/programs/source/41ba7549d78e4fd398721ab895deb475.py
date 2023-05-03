
# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter

# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(3, name='qr')
cr = ClassicalRegister(3, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(iSwapGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(RZZGate(2.061149362743449), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CZGate(), qargs=[qr[2], qr[1]], cargs=[])
qc.append(CZGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(TGate(), qargs=[qr[2]], cargs=[])
qc.append(IGate(), qargs=[qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(YGate(), qargs=[qr[1]], cargs=[])
qc.append(CCZGate(), qargs=[qr[2], qr[1], qr[0]], cargs=[])
qc.append(CSwapGate(), qargs=[qr[2], qr[1], qr[0]], cargs=[])
qc.append(IGate(), qargs=[qr[1]], cargs=[])

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
backend_10fbd0a61ba148b4864caff27922c2b9 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_10fbd0a61ba148b4864caff27922c2b9, shots=489).result().get_counts(qc)
RESULT = counts