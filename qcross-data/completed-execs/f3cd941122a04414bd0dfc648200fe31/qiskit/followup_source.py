# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[4]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(RZXGate(0.6833824466861163), qargs=[qr[0], qr[6]], cargs=[])
subcircuit.append(SXdgGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(CZGate(), qargs=[qr[4], qr[3]], cargs=[])
subcircuit.append(ZGate(), qargs=[qr[4]], cargs=[])
subcircuit.append(RZZGate(1.927446989780488), qargs=[qr[6], qr[7]], cargs=[])
subcircuit.append(CRXGate(4.736752714049485), qargs=[qr[4], qr[0]], cargs=[])
subcircuit.append(DCXGate(), qargs=[qr[1], qr[6]], cargs=[])
subcircuit.append(CUGate(4.229610589867865, 2.696266694818697, 5.631160518436971, 2.9151388486514547), qargs=[qr[0], qr[6]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[6]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0,
    1], [0, 3], [1, 0], [1, 2], [1, 4], [1, 5], [1, 7], [1, 8], [2, 1], [3,
    0], [3, 11], [4, 1], [5, 1], [6, 8], [7, 1], [8, 1], [8, 6], [8, 10], [
    9, 10], [10, 8], [10, 9], [11, 3]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_03587d2064da4ff486f9756c71cdcbe5 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_03587d2064da4ff486f9756c71cdcbe5, shots=2771).result().get_counts(qc)
RESULT = counts
