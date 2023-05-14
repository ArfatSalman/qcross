# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_028c2d = Parameter('p_028c2d')
p_77e236 = Parameter('p_77e236')
p_0f0077 = Parameter('p_0f0077')
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(3, name='qr')
cr = ClassicalRegister(3, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_028c2d), qargs=[qr[1]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(SdgGate(), qargs=[qr[1]], cargs=[])
qc.append(CRXGate(p_0f0077), qargs=[qr[2], qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(CCXGate(), qargs=[qr[1], qr[2], qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(RYYGate(p_77e236), qargs=[qr[1], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_028c2d: 6.163759533339787, p_77e236: 1.6723037552953224, p_0f0077: 5.987304452123941})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_535475abbe6c4b06b53176da4bb16592 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_535475abbe6c4b06b53176da4bb16592, shots=489).result().get_counts(qc)
RESULT = counts
