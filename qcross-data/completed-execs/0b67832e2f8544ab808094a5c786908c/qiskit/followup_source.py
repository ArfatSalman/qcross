# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_c748d9 = Parameter('p_c748d9')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(2, name='qr')
cr = ClassicalRegister(2, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZZGate(p_c748d9), qargs=[qr[1], qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_c748d9: 6.163759533339787})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=['cx', 'h', 's', 't'], optimization_level=2, coupling_map=[[0, 1], [0, 2], [1, 0], [2, 0]])
# SECTION
# NAME: EXECUTION
from qiskit import Aer, transpile, execute
backend_36ec37c95a964b3f99d1fd599e0135c6 = Aer.get_backend(
    'statevector_simulator')
counts = execute(qc, backend=backend_36ec37c95a964b3f99d1fd599e0135c6,
    shots=346).result().get_counts(qc)
RESULT = counts
