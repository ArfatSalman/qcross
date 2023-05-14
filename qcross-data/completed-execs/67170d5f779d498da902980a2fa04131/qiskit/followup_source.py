# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_445472 = Parameter('p_445472')
p_893583 = Parameter('p_893583')
p_99b2af = Parameter('p_99b2af')
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(2, name='qr')
cr = ClassicalRegister(2, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZZGate(p_445472), qargs=[qr[0], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(RYYGate(1.977559237989846), qargs=[qr[1], qr[0]], cargs=[])
qc.append(TGate(), qargs=[qr[0]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(CRXGate(p_893583), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CRZGate(2.2498881927557752), qargs=[qr[1], qr[0]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(RZGate(5.320621737498446), qargs=[qr[0]], cargs=[])
qc.append(RZGate(5.512260524440591), qargs=[qr[0]], cargs=[])
qc.append(CU1Gate(p_99b2af), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(RZZGate(6.086884486572108), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(3.3705408413231095), qargs=[qr[1], qr[0]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(RZGate(5.190931186022931), qargs=[qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(RYYGate(5.167261531657622), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SGate(), qargs=[qr[1]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_445472: 6.163759533339787, p_893583: 5.987304452123941, p_99b2af: 1.6723037552953224})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_b76502fe39414cbc9330ac6daa0e21ac = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_b76502fe39414cbc9330ac6daa0e21ac, shots=346).result().get_counts(qc)
RESULT = counts
