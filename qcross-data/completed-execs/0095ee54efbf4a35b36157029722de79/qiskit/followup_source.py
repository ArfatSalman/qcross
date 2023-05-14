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
qc.append(SdgGate(), qargs=[qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[8], qr[7], qr[5]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[5]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[8]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[3], qr[2], qr[0]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(CU1Gate(3.2142159669963557), qargs=[qr[8], qr[3]], cargs=[])
qc.append(CRZGate(1.4112277317699358), qargs=[qr[5], qr[8]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CSwapGate(), qargs=[qr[0], qr[1], qr[6]], cargs=[])
subcircuit.append(CXGate(), qargs=[qr[2], qr[0]], cargs=[])
subcircuit.append(PhaseGate(1.7897858384938228), qargs=[qr[0]], cargs=[])
subcircuit.append(CU3Gate(3.950837470808744, 0.31862897237472254, 0.35592835823340635), qargs=[qr[4], qr[0]], cargs=[])
subcircuit.append(PhaseGate(5.336667571035288), qargs=[qr[0]], cargs=[])
subcircuit.append(CRZGate(4.747288222618085), qargs=[qr[1], qr[5]], cargs=[])
subcircuit.append(RXGate(2.4205260581208594), qargs=[qr[5]], cargs=[])
subcircuit.append(CUGate(4.722103101046168, 5.3924725338944945, 4.88987246261121, 1.2497571638956968), qargs=[qr[2], qr[5]], cargs=[])
subcircuit.append(CUGate(2.862865991712737, 6.0504088665633065, 1.7203758404994713, 2.8704483107274004), qargs=[qr[3], qr[1]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[7]], cargs=[])
qc.append(CHGate(), qargs=[qr[6], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[3], qr[0]], cargs=[])
qc.append(CRZGate(2.586208953975239), qargs=[qr[1], qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0,
    1], [0, 5], [1, 0], [1, 7], [2, 3], [3, 2], [3, 7], [4, 9], [5, 0], [6,
    7], [7, 1], [7, 3], [7, 6], [7, 8], [7, 9], [8, 7], [9, 4], [9, 7]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_b623de63b5d54df8854ef0845cbb121e = Aer.get_backend('aer_simulator')
counts = execute(qc, backend=backend_b623de63b5d54df8854ef0845cbb121e, shots=3919).result().get_counts(qc)
RESULT = counts
