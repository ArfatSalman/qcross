# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_e45b80 = Parameter('p_e45b80')
p_4ed418 = Parameter('p_4ed418')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(2, name='qr')
cr = ClassicalRegister(2, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZZGate(6.163759533339787), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(ECRGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(p_4ed418), qargs=[qr[0], qr[1]], cargs=[])
qc.append(TGate(), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[1]], cargs=[])
qc.append(CRXGate(p_e45b80), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[1]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_3ca7ae = QuantumRegister(6, name='qr_3ca7ae')
qc.add_register(qr_3ca7ae)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_e45b80: 5.987304452123941, p_4ed418: 1.977559237989846})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_0a5ef9062a864055b78bfaa9f69112af = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_0a5ef9062a864055b78bfaa9f69112af, shots=346).result().get_counts(qc)
RESULT = counts
