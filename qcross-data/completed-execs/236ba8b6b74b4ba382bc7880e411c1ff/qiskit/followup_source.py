# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_ce7cb6 = Parameter('p_ce7cb6')
p_97c5b0 = Parameter('p_97c5b0')
p_3124eb = Parameter('p_3124eb')
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_3124eb), qargs=[qr[4]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[2], qr[4]], cargs=[])
qc.append(CRXGate(p_ce7cb6), qargs=[qr[1], qr[3]], cargs=[])
qc.append(CCXGate(), qargs=[qr[5], qr[9], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(TGate(), qargs=[qr[9]], cargs=[])
qc.append(XGate(), qargs=[qr[8]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[1], qr[2]], cargs=[])
qc.append(RZGate(p_97c5b0), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[6]], cargs=[])
qc.append(CSXGate(), qargs=[qr[7], qr[8]], cargs=[])
qc.append(CCXGate(), qargs=[qr[7], qr[9], qr[5]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[6], qr[7], qr[0], qr[9]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[6]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[3], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[6], qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_ce7cb6: 5.987304452123941, p_97c5b0: 4.229610589867865, p_3124eb: 6.163759533339787})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_87bd8f4471f24be9982baed65b7b415d = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_87bd8f4471f24be9982baed65b7b415d, shots=5542).result().get_counts(qc)
RESULT = counts
