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
qc.append(RZGate(6.163759533339787), qargs=[qr[4]], cargs=[])
qc.append(CSXGate(), qargs=[qr[6], qr[1]], cargs=[])
qc.append(CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245,
    5.987304452123941), qargs=[qr[3], qr[2]], cargs=[])
qc.append(SdgGate(), qargs=[qr[0]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[3], qr[4], qr[8], qr[5]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[5]], cargs=[])
qc.append(SGate(), qargs=[qr[3]], cargs=[])
qc.append(SGate(), qargs=[qr[4]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[7], qr[6], qr[3]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_25a1c8 = QuantumRegister(6, name='qr_25a1c8')
qc.add_register(qr_25a1c8)
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
backend_c11227fb41074cbabea875dcf304f07d = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_c11227fb41074cbabea875dcf304f07d, shots=3919).result().get_counts(qc)
RESULT = counts
