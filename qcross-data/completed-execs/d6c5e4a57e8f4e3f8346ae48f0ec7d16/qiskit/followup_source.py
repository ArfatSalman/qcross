# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_fe09fb = Parameter('p_fe09fb')
p_21c486 = Parameter('p_21c486')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(6, name='qr')
cr = ClassicalRegister(6, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_fe09fb), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_21c486), qargs=[qr[2], qr[4]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_fe09fb: 6.163759533339787, p_21c486: 4.2641612072511235})
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=[[0,
    1], [0, 2], [0, 6], [1, 0], [1, 4], [2, 0], [2, 5], [3, 6], [4, 1], [5,
    2], [6, 0], [6, 3], [6, 7], [7, 6]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_8edeb999972946e192a702c10e4addb7 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_8edeb999972946e192a702c10e4addb7, shots=1385).result().get_counts(qc)
RESULT = counts
