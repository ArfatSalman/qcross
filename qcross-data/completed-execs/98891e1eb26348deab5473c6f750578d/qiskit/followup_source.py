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
qc.append(CRYGate(1.075739919522674), qargs=[qr[8], qr[2]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[6], qr[2], qr[5], qr[3]], cargs=[])
qc.append(CRZGate(1.6326010370730453), qargs=[qr[1], qr[8]], cargs=[])
qc.append(CRZGate(6.113712295160513), qargs=[qr[0], qr[1]], cargs=[])
qc.append(UGate(1.4807775550519449, 4.708394834982332, 5.108906631758365), qargs=[qr[6]], cargs=[])
qc.append(CU3Gate(1.445874138242965, 0.4812746367052968, 1.4437703311652539), qargs=[qr[2], qr[6]], cargs=[])
qc.append(U1Gate(1.55032177844381), qargs=[qr[2]], cargs=[])
qc.append(RZZGate(0.023161113352440612), qargs=[qr[2], qr[6]], cargs=[])
qc.append(C3XGate(), qargs=[qr[5], qr[2], qr[3], qr[8]], cargs=[])
qc.append(C3XGate(), qargs=[qr[3], qr[8], qr[0], qr[1]], cargs=[])
qc.append(U1Gate(5.302777250135231), qargs=[qr[3]], cargs=[])
qc.append(UGate(1.7927964637983416, 0.8353911218777099, 1.5856512163121241), qargs=[qr[1]], cargs=[])
qc.append(CU3Gate(4.746133300531744, 4.497432396200483, 4.25035932691423), qargs=[qr[8], qr[5]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(HGate(), qargs=[qr[5]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(PhaseGate(4.466750388800541), qargs=[qr[8]], cargs=[])
qc.append(HGate(), qargs=[qr[7]], cargs=[])
qc.append(SwapGate(), qargs=[qr[5], qr[0]], cargs=[])
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
backend_7576b3190d284b76a8a41ba3bf19cad1 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_7576b3190d284b76a8a41ba3bf19cad1, shots=3919).result().get_counts(qc)
RESULT = counts
