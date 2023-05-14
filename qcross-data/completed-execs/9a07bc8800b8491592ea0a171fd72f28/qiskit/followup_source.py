# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(2, name='qr')
cr = ClassicalRegister(2, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CHGate(), qargs=[qr[0], qr[1]], cargs=[])
subcircuit.append(SXdgGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(CPhaseGate(1.7280044377928914), qargs=[qr[0], qr[1]],
    cargs=[])
subcircuit.append(RXXGate(0.5112149185250571), qargs=[qr[0], qr[1]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(RZZGate(6.163759533339787), qargs=[qr[0], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[0], qr[1]], cargs=[])
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
backend_b236fe3c8ae74609b42adc343a3e1138 = Aer.get_backend('aer_simulator')
counts = execute(qc, backend=backend_b236fe3c8ae74609b42adc343a3e1138, shots=346).result().get_counts(qc)
RESULT = counts
