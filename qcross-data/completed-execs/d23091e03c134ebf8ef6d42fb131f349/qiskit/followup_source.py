# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(SGate(), qargs=[qr[4]], cargs=[])
subcircuit.append(C4XGate(), qargs=[qr[1], qr[7], qr[4], qr[3], qr[6]], cargs=[])
subcircuit.append(HGate(), qargs=[qr[1]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=['cx', 'h', 's', 't'], optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION
from qiskit import Aer, transpile, execute
backend_88f0ca8ab2ba40dea4fd943810e8167a = Aer.get_backend(
    'aer_simulator_statevector')
counts = execute(qc, backend=backend_88f0ca8ab2ba40dea4fd943810e8167a,
    shots=2771).result().get_counts(qc)
RESULT = counts
