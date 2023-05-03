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
qc.append(CRXGate(5.987304452123941), qargs=[qr[1], qr[7]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CPhaseGate(4.63837786161633), qargs=[qr[3], qr[0]], cargs=[])
subcircuit.append(U2Gate(5.887184334931191, 0.07157463504881167), qargs=[qr[8]], cargs=[])
subcircuit.append(CXGate(), qargs=[qr[2], qr[4]], cargs=[])
subcircuit.append(SXGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(CRZGate(2.008796895454228), qargs=[qr[0], qr[5]], cargs=[])
subcircuit.append(RCCXGate(), qargs=[qr[9], qr[1], qr[8]], cargs=[])
subcircuit.append(RXXGate(5.25962645863375), qargs=[qr[4], qr[6]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CCXGate(), qargs=[qr[5], qr[9], qr[7]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[9]], cargs=[])
qc.append(XGate(), qargs=[qr[8]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[1], qr[6]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[1]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: QASM_CONVERSION

qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 5], [0, 11], [0, 13], [1, 0], [1, 8], [2, 13], [3, 9], [3, 12], [4, 8], [5, 0], [5, 10], [6, 9], [7, 11], [8, 1], [8, 4], [9, 3], [9, 6], [9, 11], [10, 5], [11, 0], [11, 7], [11, 9], [12, 3], [13, 0], [13, 2]])
# SECTION
# NAME: EXECUTION
from qiskit import Aer, transpile, execute
backend_3bbec91a477b4a56948bfcf5d4a0bdc7 = Aer.get_backend(
    'aer_simulator_statevector')
counts = execute(qc, backend=backend_3bbec91a477b4a56948bfcf5d4a0bdc7,
    shots=5542).result().get_counts(qc)
RESULT = counts
