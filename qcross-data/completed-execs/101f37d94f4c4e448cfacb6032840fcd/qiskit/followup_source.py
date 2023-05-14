# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_189742 = Parameter('p_189742')
p_d42ab6 = Parameter('p_d42ab6')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(4, name='qr')
cr = ClassicalRegister(4, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_d42ab6), qargs=[qr[1]], cargs=[])
qc.append(RZZGate(p_189742), qargs=[qr[2], qr[3]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[2], qr[3]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_189742: 4.066449154047175, p_d42ab6: 6.163759533339787})
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_1190936a8df4489fb5af414825309822 = Aer.get_backend('statevector_simulator')
counts = execute(qc, backend=backend_1190936a8df4489fb5af414825309822, shots=692).result().get_counts(qc)
RESULT = counts
