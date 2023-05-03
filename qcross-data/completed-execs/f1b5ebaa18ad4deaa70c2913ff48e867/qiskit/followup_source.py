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
qc.append(RZGate(6.163759533339787), qargs=[qr[4]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[9], qr[4]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(TdgGate(), qargs=[qr[2]], cargs=[])
subcircuit.append(CYGate(), qargs=[qr[5], qr[2]], cargs=[])
subcircuit.append(SXGate(), qargs=[qr[8]], cargs=[])
subcircuit.append(CRZGate(2.008796895454228), qargs=[qr[8], qr[6]], cargs=[])
subcircuit.append(RCCXGate(), qargs=[qr[3], qr[7], qr[1]], cargs=[])
subcircuit.append(RXXGate(5.25962645863375), qargs=[qr[2], qr[9]], cargs=[])
subcircuit.append(DCXGate(), qargs=[qr[5], qr[0]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CRXGate(5.987304452123941), qargs=[qr[7], qr[0]], cargs=[])
qc.append(CCXGate(), qargs=[qr[6], qr[3], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[5]], cargs=[])
qc.append(TGate(), qargs=[qr[3]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[7], qr[9]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[7]], cargs=[])
qc.append(SXGate(), qargs=[qr[5]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[1]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_b0b0b7 = QuantumRegister(8, name='qr_b0b0b7')
subcircuit.add_register(qr_b0b0b7)
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
backend_11664f468d734260aa2572e8ad5334d4 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_11664f468d734260aa2572e8ad5334d4, shots=5542).result().get_counts(qc)
RESULT = counts
