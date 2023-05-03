# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(7, name='qr')
cr = ClassicalRegister(7, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[3]], cargs=[])
qc.append(CRXGate(2.0099472182748075), qargs=[qr[2], qr[5]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CSwapGate(), qargs=[qr[6], qr[5], qr[4]], cargs=[])
subcircuit.append(CXGate(), qargs=[qr[2], qr[3]], cargs=[])
subcircuit.append(iSwapGate(), qargs=[qr[1], qr[6]], cargs=[])
subcircuit.append(CPhaseGate(3.326780904591333), qargs=[qr[0], qr[6]], cargs=[])
subcircuit.append(CU1Gate(2.0685963035149753), qargs=[qr[4], qr[0]], cargs=[])
subcircuit.append(PhaseGate(5.336667571035288), qargs=[qr[0]], cargs=[])
subcircuit.append(CUGate(5.014941143947427, 4.437078557875917, 6.016631690603051, 3.1243053509071124), qargs=[qr[1], qr[2]], cargs=[])
subcircuit.append(SXGate(), qargs=[qr[1]], cargs=[])
subcircuit.append(iSwapGate(), qargs=[qr[3], qr[6]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(C3SXGate(), qargs=[qr[6], qr[0], qr[1], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[4], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[2], qr[1], qr[5]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(ECRGate(), qargs=[qr[6], qr[3]], cargs=[])
qc.append(SdgGate(), qargs=[qr[6]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[2], qr[5], qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[1]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[2], qr[1], qr[3]], cargs=[])
qc.append(CU1Gate(3.2142159669963557), qargs=[qr[4], qr[0]], cargs=[])
qc.append(CRXGate(5.94477504571567), qargs=[qr[4], qr[6]], cargs=[])
qc.append(CHGate(), qargs=[qr[4], qr[0]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[0], qr[3], qr[4]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[5]], cargs=[])
qc.append(CRZGate(4.833923139882297), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CU1Gate(4.028174522740928), qargs=[qr[1], qr[4]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[0], qr[5], qr[4]], cargs=[])
qc.append(CRZGate(2.586208953975239), qargs=[qr[6], qr[2]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_941308 = QuantumRegister(3, name='qr_941308')
qc.add_register(qr_941308)
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
backend_bf12772f867b47d8849c852d80d36504 = Aer.get_backend('aer_simulator_matrix_product_state')
counts = execute(qc, backend=backend_bf12772f867b47d8849c852d80d36504, shots=1959).result().get_counts(qc)
RESULT = counts
