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
qc.append(CRZGate(1.3789403400889426), qargs=[qr[1], qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CRYGate(0.793394619995631), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CRYGate(1.751652383527618), qargs=[qr[0], qr[1]], cargs=[])
qc.append(RXXGate(0.19609305461275878), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(SwapGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CRZGate(0.4924711250283179), qargs=[qr[0], qr[1]], cargs=[])
qc.append(ECRGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CU1Gate(4.448608931258779), qargs=[qr[1], qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[1], qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: QASM_CONVERSION
qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_0fc1d661b5e44d02ad629338b5743c9a = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_0fc1d661b5e44d02ad629338b5743c9a, shots=346).result().get_counts(qc)
RESULT = counts
