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
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])
qc.append(RZZGate(4.066449154047175), qargs=[qr[0], qr[2]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[3], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245,
    5.987304452123941), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CU1Gate(5.154187354656876), qargs=[qr[2], qr[1]], cargs=[])
qc.append(CHGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[3], qr[0]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[1], qr[3], qr[0]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[3], qr[1], qr[0]], cargs=[])
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
backend_bf5eb957ca384015a2cb6706f9769071 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_bf5eb957ca384015a2cb6706f9769071, shots=692).result().get_counts(qc)
RESULT = counts
