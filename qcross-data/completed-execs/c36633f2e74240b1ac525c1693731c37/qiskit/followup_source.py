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
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[6], qr[3]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(TdgGate(), qargs=[qr[4]], cargs=[])
subcircuit.append(CYGate(), qargs=[qr[2], qr[4]], cargs=[])
subcircuit.append(SXGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(CRZGate(2.008796895454228), qargs=[qr[0], qr[5]], cargs=[])
subcircuit.append(RCCXGate(), qargs=[qr[9], qr[1], qr[8]], cargs=[])
subcircuit.append(RXXGate(5.25962645863375), qargs=[qr[4], qr[6]], cargs=[])
subcircuit.append(DCXGate(), qargs=[qr[2], qr[7]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CRXGate(5.987304452123941), qargs=[qr[1], qr[7]], cargs=[])
qc.append(CCXGate(), qargs=[qr[5], qr[9], qr[7]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[9]], cargs=[])
qc.append(XGate(), qargs=[qr[8]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[1], qr[6]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[4], qr[8]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0,
    1], [0, 4], [0, 8], [0, 9], [1, 0], [2, 7], [2, 9], [3, 8], [4, 0], [4,
    5], [5, 4], [6, 9], [7, 2], [8, 0], [8, 3], [9, 0], [9, 2], [9, 6]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_804660baf25e434abaf5de394dc179fa = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_804660baf25e434abaf5de394dc179fa, shots=5542).result().get_counts(qc)
RESULT = counts
