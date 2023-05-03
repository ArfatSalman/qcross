# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_779df3 = Parameter('p_779df3')
p_9d7c85 = Parameter('p_9d7c85')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(6, name='qr')
cr = ClassicalRegister(6, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_779df3), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_9d7c85), qargs=[qr[2], qr[4]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_779df3: 6.163759533339787, p_9d7c85: 4.2641612072511235})
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=['ccx', 'h'], optimization_level=2,
    coupling_map=[[0, 1], [0, 2], [0, 4], [0, 7], [1, 0], [2, 0], [3, 7], [
    4, 0], [5, 7], [6, 7], [7, 0], [7, 3], [7, 5], [7, 6]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_2b4b9d63dd3447f6a1ffe81ed4b72d2c = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_2b4b9d63dd3447f6a1ffe81ed4b72d2c, shots=1385).result().get_counts(qc)
RESULT = counts
