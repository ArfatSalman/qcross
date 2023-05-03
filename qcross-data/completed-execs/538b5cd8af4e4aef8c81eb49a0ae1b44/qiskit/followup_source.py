# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(6, name='qr')
cr = ClassicalRegister(6, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[2], qr[4]], cargs=[])
qc.append(CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245, 5.987304452123941), qargs=[qr[2], qr[3]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[4], qr[0], qr[2]], cargs=[])
qc.append(CCXGate(), qargs=[qr[1], qr[5], qr[0]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[4], qr[3], qr[5], qr[0]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CU3Gate(1.2827690425732097, 1.3283826543858017, 3.672121211148789), qargs=[qr[2], qr[5]], cargs=[])
subcircuit.append(TGate(), qargs=[qr[1]], cargs=[])
subcircuit.append(CUGate(4.229610589867865, 2.696266694818697, 5.631160518436971, 2.9151388486514547), qargs=[qr[0], qr[3]], cargs=[])
subcircuit.append(TGate(), qargs=[qr[2]], cargs=[])
subcircuit.append(RZXGate(4.563562108824195), qargs=[qr[4], qr[0]], cargs=[])
subcircuit.append(C3XGate(5.94477504571567), qargs=[qr[4], qr[5], qr[2], qr[1]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_fea763 = QuantumRegister(7, name='qr_fea763')
qc.add_register(qr_fea763)
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
backend_5db6aa48d8d3497da00c886e621dd826 = Aer.get_backend(
    'aer_simulator_statevector')
counts = execute(qc, backend=backend_5db6aa48d8d3497da00c886e621dd826,
    shots=1385).result().get_counts(qc)
RESULT = counts
