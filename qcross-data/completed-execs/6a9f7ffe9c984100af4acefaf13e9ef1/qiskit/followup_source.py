# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[4]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[7], qr[4]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[2], qr[8]], cargs=[])
qc.append(CCXGate(), qargs=[qr[5], qr[6], qr[8]], cargs=[])
qc.append(ZGate(), qargs=[qr[9]], cargs=[])
qc.append(TGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[2], qr[7]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[2]], cargs=[])
qc.append(SXGate(), qargs=[qr[9]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CCXGate(), qargs=[qr[0], qr[6], qr[5]], cargs=[])
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
backend_35791cfb30ee449aa0475ae5f2785e05 = Aer.get_backend('aer_simulator_statevector')
counts = execute(qc, backend=backend_35791cfb30ee449aa0475ae5f2785e05, shots=5542).result().get_counts(qc)
RESULT = counts
