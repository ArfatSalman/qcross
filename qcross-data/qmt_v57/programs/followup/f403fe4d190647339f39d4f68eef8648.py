# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(7, name='qr')
cr = ClassicalRegister(7, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(CPhaseGate(1.2090494827833855), qargs=[qr[5], qr[4]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CPhaseGate(2.767009041055994), qargs=[qr[1], qr[5]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(RXXGate(3.2070313364356364), qargs=[qr[5], qr[6]], cargs=[])
qc.append(U1Gate(2.9651284130043303), qargs=[qr[0]], cargs=[])
qc.append(RZXGate(0.27840038795582156), qargs=[qr[5], qr[3]], cargs=[])
qc.append(PhaseGate(4.59971292164702), qargs=[qr[3]], cargs=[])
qc.append(RYYGate(0.33311418158025663), qargs=[qr[6], qr[5]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[6], qr[0], qr[4]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: QASM_CONVERSION

qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_521f3fc2e191400684c1dd770473efcb = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_521f3fc2e191400684c1dd770473efcb, shots=1959).result().get_counts(qc)
RESULT = counts
