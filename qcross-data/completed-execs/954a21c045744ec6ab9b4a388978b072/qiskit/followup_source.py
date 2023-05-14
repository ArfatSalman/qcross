# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_961b4a = Parameter('p_961b4a')
p_bc4b41 = Parameter('p_bc4b41')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(11, name='qr')
cr = ClassicalRegister(11, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_bc4b41), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_961b4a), qargs=[qr[6], qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_961b4a: 4.2641612072511235, p_bc4b41: 6.163759533339787})
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_b9752a6e32ee486e80d9a957c2437b88 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_b9752a6e32ee486e80d9a957c2437b88, shots=7838).result().get_counts(qc)
RESULT = counts
