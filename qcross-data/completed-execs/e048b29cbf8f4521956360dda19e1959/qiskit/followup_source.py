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
qc.append(RZGate(6.163759533339787), qargs=[qr[1]], cargs=[])
qc.append(RZZGate(4.066449154047175), qargs=[qr[2], qr[3]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(TdgGate(), qargs=[qr[2]], cargs=[])
subcircuit.append(U1Gate(5.01836135520768), qargs=[qr[1]], cargs=[])
subcircuit.append(CRYGate(4.736752714049485), qargs=[qr[0], qr[3]], cargs=[])
subcircuit.append(RXGate(6.1292830756636185), qargs=[qr[2]], cargs=[])
subcircuit.append(CHGate(), qargs=[qr[2], qr[3]], cargs=[])
subcircuit.append(CXGate(), qargs=[qr[2], qr[0]], cargs=[])
subcircuit.append(RZZGate(3.516607467010828), qargs=[qr[3], qr[1]], cargs=[])
subcircuit.append(PhaseGate(3.2287759437031154), qargs=[qr[1]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(iSwapGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245, 5.987304452123941), qargs=[qr[0], qr[2]], cargs=[])
qc.append(CU1Gate(5.154187354656876), qargs=[qr[3], qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[3], qr[0], qr[1], qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[3], qr[1], qr[0], qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0,
    1], [1, 0], [1, 3], [1, 4], [2, 3], [3, 1], [3, 2], [4, 1]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_9124fb2417c2405bb11a0d992e6d52d3 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_9124fb2417c2405bb11a0d992e6d52d3, shots=692).result().get_counts(qc)
RESULT = counts
