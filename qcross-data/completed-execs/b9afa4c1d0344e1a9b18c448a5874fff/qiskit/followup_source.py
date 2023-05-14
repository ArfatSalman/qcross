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
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CXGate(), qargs=[qr[10], qr[3]], cargs=[])
subcircuit.append(RYGate(2.3864521352475245), qargs=[qr[1]], cargs=[])
subcircuit.append(CPhaseGate(1.6161683469432118), qargs=[qr[5], qr[9]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: QASM_CONVERSION

qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=3, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_456350ad6d7b4fa2a38bc1b5df252a28 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_456350ad6d7b4fa2a38bc1b5df252a28, shots=7838).result().get_counts(qc)
RESULT = counts
