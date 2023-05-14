# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_257052 = Parameter('p_257052')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_257052), qargs=[qr[4]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_257052: 6.163759533339787})
# SECTION
# NAME: QASM_CONVERSION

qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=['ccx', 'h'], optimization_level=2,
    coupling_map=[[0, 1], [0, 2], [1, 0], [1, 3], [1, 5], [2, 0], [2, 4], [
    3, 1], [4, 2], [5, 1], [5, 6], [6, 5], [6, 7], [7, 6]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_d4e197a3f1db44449835d3cf83ee49c1 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_d4e197a3f1db44449835d3cf83ee49c1, shots=2771).result().get_counts(qc)
RESULT = counts
