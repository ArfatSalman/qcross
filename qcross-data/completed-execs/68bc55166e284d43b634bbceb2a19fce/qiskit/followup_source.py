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
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CSwapGate(), qargs=[qr[0], qr[5], qr[4]], cargs=[])
subcircuit.append(CSXGate(), qargs=[qr[4], qr[0]], cargs=[])
subcircuit.append(SwapGate(), qargs=[qr[1], qr[4]], cargs=[])
subcircuit.append(RYYGate(0.5501056885328758), qargs=[qr[2], qr[0]], cargs=[])
subcircuit.append(SXdgGate(), qargs=[qr[5]], cargs=[])
subcircuit.append(DCXGate(), qargs=[qr[2], qr[1]], cargs=[])
subcircuit.append(CSwapGate(), qargs=[qr[6], qr[5], qr[4]], cargs=[])
subcircuit.append(CXGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[3]], cargs=[])
qc.append(CRXGate(2.0099472182748075), qargs=[qr[2], qr[5]], cargs=[])
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
# SECTION
# NAME: USELESS_ENTITIES

qr_a2badd = QuantumRegister(3, name='qr_a2badd')
subcircuit.add_register(qr_a2badd)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_16625294d8a045e6906122e4bafc225a = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_16625294d8a045e6906122e4bafc225a, shots=1959).result().get_counts(qc)
RESULT = counts
