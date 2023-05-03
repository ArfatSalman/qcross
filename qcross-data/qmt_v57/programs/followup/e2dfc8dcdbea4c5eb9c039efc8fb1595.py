# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(4, name='qr')
cr = ClassicalRegister(4, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(TdgGate(), qargs=[qr[3]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(TGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(XGate(), qargs=[qr[3]], cargs=[])
subcircuit.append(CSdgGate(), qargs=[qr[1], qr[2]], cargs=[])
subcircuit.append(RXGate(3.585933838237832), qargs=[qr[3]], cargs=[])
subcircuit.append(RZGate(4.327708900759496), qargs=[qr[2]], cargs=[])
subcircuit.append(CSdgGate(), qargs=[qr[1], qr[2]], cargs=[])
subcircuit.append(CSdgGate(), qargs=[qr[2], qr[1]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(RC3XGate(), qargs=[qr[3], qr[2], qr[0], qr[1]], cargs=[])
qc.append(CRXGate(3.8220531708356265), qargs=[qr[2], qr[3]], cargs=[])
qc.append(RYYGate(0.706851892491546), qargs=[qr[0], qr[3]], cargs=[])
qc.append(SGate(), qargs=[qr[3]], cargs=[])
qc.append(CCXGate(), qargs=[qr[2], qr[3], qr[0]], cargs=[])
qc.append(U2Gate(4.244731333359949, 5.111240623114551), qargs=[qr[1]], cargs=[])
qc.append(U1Gate(6.038142598726985), qargs=[qr[3]], cargs=[])
qc.append(RZZGate(4.711366793785529), qargs=[qr[0], qr[3]], cargs=[])
qc.append(CCZGate(), qargs=[qr[1], qr[2], qr[3]], cargs=[])
qc.append(SGate(), qargs=[qr[1]], cargs=[])
qc.append(CXGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(U1Gate(3.792448958077701), qargs=[qr[3]], cargs=[])
qc.append(RZZGate(0.34163860688651065), qargs=[qr[1], qr[0]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(RXXGate(0.5068226496124109), qargs=[qr[0], qr[1]], cargs=[])
qc.append(RYYGate(2.3758586345554287), qargs=[qr[2], qr[0]], cargs=[])
qc.append(RXGate(1.4237342865387943), qargs=[qr[0]], cargs=[])
qc.append(U1Gate(6.094655700711693), qargs=[qr[2]], cargs=[])
qc.append(CSGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CYGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(CYGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(IGate(), qargs=[qr[3]], cargs=[])
qc.append(CSGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(U2Gate(4.750593946827152, 1.9165638225080148), qargs=[qr[0]], cargs=[])
qc.append(RXXGate(2.141645891766187), qargs=[qr[1], qr[2]], cargs=[])
qc.append(RXGate(5.97814280452802), qargs=[qr[3]], cargs=[])
qc.append(CSXGate(), qargs=[qr[3], qr[1]], cargs=[])
qc.append(CSGate(), qargs=[qr[2], qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1, coupling_map=None)
# SECTION
# NAME: QASM_CONVERSION
qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_2f817173758341c1ad3cc49fd8de764b = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_2f817173758341c1ad3cc49fd8de764b, shots=692).result().get_counts(qc)
RESULT = counts
