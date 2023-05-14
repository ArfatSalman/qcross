# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_af69ea = Parameter('p_af69ea')
p_66b890 = Parameter('p_66b890')
p_8a1de7 = Parameter('p_8a1de7')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(9, name='qr')
cr = ClassicalRegister(9, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_66b890), qargs=[qr[8]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[4]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CUGate(p_8a1de7, 5.897054719225356, p_af69ea, 5.987304452123941), qargs=[qr[0], qr[6]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_af69ea: 2.3864521352475245, p_66b890: 6.163759533339787, p_8a1de7: 0.5112149185250571})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_a9a154acab0a4038957b25b6faae95dd = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_a9a154acab0a4038957b25b6faae95dd, shots=3919).result().get_counts(qc)
RESULT = counts
