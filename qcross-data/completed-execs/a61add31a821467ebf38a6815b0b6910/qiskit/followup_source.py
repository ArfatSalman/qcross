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
qc.append(RZGate(6.163759533339787), qargs=[qr[5]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(XGate(), qargs=[qr[3]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[0], qr[3]], cargs=[])
qc.append(CRZGate(1.0296448789776642), qargs=[qr[2], qr[3]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[1], qr[3], qr[7]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_54618b = QuantumRegister(9, name='qr_54618b')
qc.add_register(qr_54618b)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=3, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_46f5dba38cc14535acbcd8525452037d = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_46f5dba38cc14535acbcd8525452037d, shots=2771).result().get_counts(qc)
RESULT = counts
