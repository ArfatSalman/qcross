
# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter

# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(9, name='qr')
cr = ClassicalRegister(9, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(YGate(), qargs=[qr[0]], cargs=[])
qc.append(SwapGate(), qargs=[qr[5], qr[8]], cargs=[])
qc.append(CRYGate(0.4514529683521159), qargs=[qr[3], qr[4]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[2], qr[8]], cargs=[])
qc.append(CYGate(), qargs=[qr[4], qr[3]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[7]], cargs=[])

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
backend_49271f1149c6432189462802fd5f2bde = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_49271f1149c6432189462802fd5f2bde, shots=3919).result().get_counts(qc)
RESULT = counts