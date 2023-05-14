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


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(PhaseGate(0.5112149185250571), qargs=[qr[1]], cargs=[])
subcircuit.append(SdgGate(), qargs=[qr[1]], cargs=[])
subcircuit.append(ZGate(), qargs=[qr[2]], cargs=[])
subcircuit.append(CPhaseGate(2.2498881927557752), qargs=[qr[1], qr[0]], cargs=[])
subcircuit.append(CU1Gate(5.320621737498446), qargs=[qr[1], qr[0]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(iSwapGate(), qargs=[qr[2], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: QASM_CONVERSION


from qiskit.qasm3 import loads, dumps
qc = loads(dumps(qc))

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_ebc240aa017542cea7d45a4f96e60918 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_ebc240aa017542cea7d45a4f96e60918, shots=489).result().get_counts(qc)
RESULT = counts
