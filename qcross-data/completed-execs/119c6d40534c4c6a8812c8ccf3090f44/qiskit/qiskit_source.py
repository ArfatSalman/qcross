
# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter

# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(4, name='qr')
cr = ClassicalRegister(4, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(SdgGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(2.10593478876119), qargs=[qr[2], qr[1]], cargs=[])
qc.append(IGate(), qargs=[qr[1]], cargs=[])
qc.append(CZGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(CZGate(), qargs=[qr[0], qr[3]], cargs=[])
qc.append(CZGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(CU3Gate(5.177552214723695,3.7847055340640803,5.596894918056728), qargs=[qr[2], qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(CPhaseGate(5.982058731459433), qargs=[qr[2], qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(C3XGate(), qargs=[qr[3], qr[1], qr[2], qr[0]], cargs=[])

# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=None)

# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_175df900d2fe417bb4ef66ecf8261790 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_175df900d2fe417bb4ef66ecf8261790, shots=692).result().get_counts(qc)
RESULT = counts