# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_7813b3 = Parameter('p_7813b3')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(4, name='qr')
cr = ClassicalRegister(4, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(TdgGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(CCXGate(), qargs=[qr[2], qr[3], qr[1]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(RZGate(p_7813b3), qargs=[qr[1]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_5875bb = QuantumRegister(5, name='qr_5875bb')
subcircuit.add_register(qr_5875bb)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_7813b3: 6.163759533339787})
# SECTION
# NAME: QASM_CONVERSION
qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_502fc162390a4d5594688a9b07a4a9fa = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_502fc162390a4d5594688a9b07a4a9fa, shots=692).result().get_counts(qc)
RESULT = counts
