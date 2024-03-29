# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_3aa544 = Parameter('p_3aa544')
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(3, name='qr')
cr = ClassicalRegister(3, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_3aa544), qargs=[qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[1]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(SGate(), qargs=[qr[1]], cargs=[])
qc.append(SdgGate(), qargs=[qr[0]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[2], qr[1]], cargs=[])
qc.append(SGate(), qargs=[qr[1]], cargs=[])
qc.append(CCXGate(), qargs=[qr[0], qr[2], qr[1]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(RYYGate(1.6723037552953224), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_3aa544: 6.163759533339787})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=3, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_79c3f4c54ad7472296122850fc96f424 = Aer.get_backend('aer_simulator')
counts = execute(qc, backend=backend_79c3f4c54ad7472296122850fc96f424, shots=489).result().get_counts(qc)
RESULT = counts
