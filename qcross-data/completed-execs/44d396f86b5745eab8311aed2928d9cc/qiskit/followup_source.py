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
qc.append(CCXGate(), qargs=[qr[5], qr[9], qr[7]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[9]], cargs=[])
qc.append(XGate(), qargs=[qr[8]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[1], qr[6]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[4], qr[8]], cargs=[])
qc.append(CCXGate(), qargs=[qr[4], qr[9], qr[5]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[4], qr[0], qr[9]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CSwapGate(), qargs=[qr[0], qr[5], qr[4]], cargs=[])
subcircuit.append(RCCXGate(), qargs=[qr[9], qr[1], qr[8]], cargs=[])
subcircuit.append(RXXGate(5.25962645863375), qargs=[qr[4], qr[6]], cargs=[])
subcircuit.append(DCXGate(), qargs=[qr[2], qr[7]], cargs=[])
subcircuit.append(ECRGate(), qargs=[qr[2], qr[0]], cargs=[])
subcircuit.append(PhaseGate(5.5146057452272546), qargs=[qr[0]], cargs=[])
subcircuit.append(ECRGate(), qargs=[qr[3], qr[4]], cargs=[])
subcircuit.append(PhaseGate(0.4827903095199283), qargs=[qr[8]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_a1bb74 = QuantumRegister(9, name='qr_a1bb74')
qc.add_register(qr_a1bb74)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: QASM_CONVERSION
qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_4632d38baf754ddf8db9a2ef157f910f = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_4632d38baf754ddf8db9a2ef157f910f, shots=5542).result().get_counts(qc)
RESULT = counts
