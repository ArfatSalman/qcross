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
subcircuit.append(RYGate(3.393897726708824), qargs=[qr[0]], cargs=[])
subcircuit.append(iSwapGate(), qargs=[qr[2], qr[0]], cargs=[])
subcircuit.append(PhaseGate(1.7897858384938228), qargs=[qr[0]], cargs=[])
subcircuit.append(ECRGate(), qargs=[qr[0], qr[4]], cargs=[])
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
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [1, 0], [2, 3], [2, 5], [3, 2], [4, 8], [5, 0], [5, 2], [6, 0], [7, 0], [8, 0], [8, 4], [9, 0]])
# SECTION
# NAME: EXECUTION
from qiskit import Aer, transpile, execute
backend_ccd19c482f054440999e1768290040c9 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_ccd19c482f054440999e1768290040c9,
    shots=1959).result().get_counts(qc)
RESULT = counts
