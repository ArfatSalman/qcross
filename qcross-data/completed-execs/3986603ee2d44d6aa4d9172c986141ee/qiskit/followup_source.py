# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_16f9a8 = Parameter('p_16f9a8')
p_8c2b7b = Parameter('p_8c2b7b')
p_a9d3df = Parameter('p_a9d3df')
p_804b37 = Parameter('p_804b37')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_804b37), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[6]], cargs=[])
qc.append(CRXGate(p_8c2b7b), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CRZGate(p_16f9a8), qargs=[qr[1], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[7], qr[6], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(p_a9d3df), qargs=[qr[6], qr[7]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_884337 = QuantumRegister(6, name='qr_884337')
qc.add_register(qr_884337)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_16f9a8: 1.0296448789776642, p_8c2b7b: 5.987304452123941, p_a9d3df: 1.740253089260498, p_804b37: 6.163759533339787})
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=['cx', 'h', 's', 't'], optimization_level=2,
    coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_dbe0f7a7533c41bd9d4b536f8d4f07b8 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_dbe0f7a7533c41bd9d4b536f8d4f07b8, shots=2771).result().get_counts(qc)
RESULT = counts
