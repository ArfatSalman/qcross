# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(9, name='qr')
cr = ClassicalRegister(9, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[8]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[4]], cargs=[])
qc.append(CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245, 5.987304452123941), qargs=[qr[0], qr[6]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CPhaseGate(4.63837786161633), qargs=[qr[7], qr[5]], cargs=[])
subcircuit.append(UGate(3.5173414605326783, 2.3568871696687452, 6.011900464835247), qargs=[qr[4]], cargs=[])
subcircuit.append(XGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(RZZGate(5.017245588344839), qargs=[qr[0], qr[8]], cargs=[])
subcircuit.append(CRZGate(2.008796895454228), qargs=[qr[0], qr[6]], cargs=[])
subcircuit.append(CSXGate(), qargs=[qr[6], qr[1]], cargs=[])
subcircuit.append(SXGate(), qargs=[qr[3]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(SdgGate(), qargs=[qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[8], qr[7], qr[5]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[5]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[8]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[3], qr[2], qr[0]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_0ba758 = QuantumRegister(1, name='qr_0ba758')
qc.add_register(qr_0ba758)
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
backend_f75c0c278733421a989415d18627c459 = Aer.get_backend(
    'aer_simulator_statevector')
counts = execute(qc, backend=backend_f75c0c278733421a989415d18627c459,
    shots=3919).result().get_counts(qc)
RESULT = counts
