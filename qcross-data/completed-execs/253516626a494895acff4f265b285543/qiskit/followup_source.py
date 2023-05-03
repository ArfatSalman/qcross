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
qc.append(DCXGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(RXGate(6.0811696452339525), qargs=[qr[0]], cargs=[])
qc.append(TdgGate(), qargs=[qr[1]], cargs=[])
qc.append(DCXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(SwapGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(RXGate(0.6094072051955249), qargs=[qr[2]], cargs=[])
qc.append(TdgGate(), qargs=[qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: QASM_CONVERSION
qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_08903a2209e44ba6bfd01ee7e104dca9 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_08903a2209e44ba6bfd01ee7e104dca9, shots=489).result().get_counts(qc)
RESULT = counts
