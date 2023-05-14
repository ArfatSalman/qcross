# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_3be9dd = Parameter('p_3be9dd')
p_7c0930 = Parameter('p_7c0930')
p_1ba891 = Parameter('p_1ba891')
p_c8dca5 = Parameter('p_c8dca5')
p_abdae9 = Parameter('p_abdae9')
p_fd3e2d = Parameter('p_fd3e2d')
p_177252 = Parameter('p_177252')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(4, name='qr')
cr = ClassicalRegister(4, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_1ba891), qargs=[qr[1]], cargs=[])
qc.append(RZZGate(p_fd3e2d), qargs=[qr[2], qr[3]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(CUGate(p_c8dca5, p_177252, p_3be9dd, p_abdae9), qargs=[qr[0], qr[
    2]], cargs=[])
qc.append(CU1Gate(p_7c0930), qargs=[qr[3], qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[3], qr[0], qr[1], qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[3], qr[1], qr[0], qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_3be9dd: 2.3864521352475245, p_7c0930: 5.154187354656876, p_1ba891: 6.163759533339787, p_c8dca5: 0.5112149185250571, p_abdae9: 5.987304452123941, p_fd3e2d: 4.066449154047175,
    p_177252: 5.897054719225356,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [1, 0], [1, 2], [1, 3], [2, 1], [3, 1], [3, 4], [4, 3]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_faf6dc5535404a57ba6d1b36be5a3776 = Aer.get_backend('statevector_simulator')
counts = execute(qc, backend=backend_faf6dc5535404a57ba6d1b36be5a3776, shots=692).result().get_counts(qc)
RESULT = counts
