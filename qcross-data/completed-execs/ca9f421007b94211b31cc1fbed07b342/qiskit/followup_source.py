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
subcircuit.append(U2Gate(2.932926420504681,6.014263058248304), qargs=[qr[2]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(RZGate(6.163759533339787), qargs=[qr[4]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_a3495c = QuantumRegister(10, name='qr_a3495c')
qc.add_register(qr_a3495c)
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
backend_2332cb0e2b5848b7878a3ccc5980ad5e = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_2332cb0e2b5848b7878a3ccc5980ad5e, shots=2771).result().get_counts(qc)
RESULT = counts
