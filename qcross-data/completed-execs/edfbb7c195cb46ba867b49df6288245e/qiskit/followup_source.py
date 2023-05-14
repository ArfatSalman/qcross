# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(3, name='qr')
cr = ClassicalRegister(3, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[1]], cargs=[])
qc.append(CHGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[2], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(U1Gate(4.654977034583802), qargs=[qr[2]], cargs=[])
subcircuit.append(U3Gate(5.01836135520768,5.190931186022931,1.2128092629174942), qargs=[qr[1]], cargs=[])
subcircuit.append(CYGate(), qargs=[qr[0], qr[1]], cargs=[])
subcircuit.append(RYGate(6.1292830756636185), qargs=[qr[2]], cargs=[])
subcircuit.append(CPhaseGate(4.167661441102218), qargs=[qr[2], qr[1]], cargs=[])
subcircuit.append(IGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(UGate(2.9790366726895714,5.974354952564585,3.2287759437031154), qargs=[qr[1]], cargs=[])
subcircuit.append(SdgGate(), qargs=[qr[1]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(SGate(), qargs=[qr[2]], cargs=[])
qc.append(SdgGate(), qargs=[qr[1]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[0], qr[2]], cargs=[])
qc.append(SGate(), qargs=[qr[2]], cargs=[])
qc.append(CCXGate(), qargs=[qr[1], qr[0], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(RYYGate(1.6723037552953224), qargs=[qr[1], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[0]], cargs=[])
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
backend_5448ccbfdfea426b8f434636a751a103 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_5448ccbfdfea426b8f434636a751a103, shots=489).result().get_counts(qc)
RESULT = counts
