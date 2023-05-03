# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(3, name='qr')
cr = ClassicalRegister(3, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[1]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(SGate(), qargs=[qr[1]], cargs=[])
qc.append(SdgGate(), qargs=[qr[2]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SGate(), qargs=[qr[1]], cargs=[])
qc.append(CCXGate(), qargs=[qr[2], qr[0], qr[1]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[2], qr[1]], cargs=[])
qc.append(RYYGate(1.6723037552953224), qargs=[qr[2], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(TGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(SGate(), qargs=[qr[1]], cargs=[])
qc.append(ECRGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[2], qr[0], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(SdgGate(), qargs=[qr[1]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[0], qr[1], qr[2]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[1], qr[2]], cargs=[])
qc.append(SGate(), qargs=[qr[1]], cargs=[])
qc.append(CRZGate(0.05525155902669336), qargs=[qr[1], qr[2]], cargs=[])
qc.append(RYYGate(3.2287759437031154), qargs=[qr[2], qr[1]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_069905 = QuantumRegister(6, name='qr_069905')
qc.add_register(qr_069905)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=['rx', 'ry', 'rz', 'p', 'cx'], optimization_level=0, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_07cceee203c84d7e879588246482e9e4 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_07cceee203c84d7e879588246482e9e4, shots=489).result().get_counts(qc)
RESULT = counts
