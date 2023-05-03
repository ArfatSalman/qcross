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
qc.append(RZGate(6.163759533339787), qargs=[qr[4]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_f86a24 = QuantumRegister(4, name='qr_f86a24')
qc.add_register(qr_f86a24)
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
backend_0e28f063f35c4d49aad9fbac793cc2ce = Aer.get_backend(
    'aer_simulator_statevector')
counts = execute(qc, backend=backend_0e28f063f35c4d49aad9fbac793cc2ce,
    shots=2771).result().get_counts(qc)
RESULT = counts
