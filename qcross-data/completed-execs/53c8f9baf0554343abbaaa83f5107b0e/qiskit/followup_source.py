# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_cce11c = Parameter('p_cce11c')
p_8f908f = Parameter('p_8f908f')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(11, name='qr')
cr = ClassicalRegister(11, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_cce11c), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_8f908f), qargs=[qr[6], qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_cce11c: 6.163759533339787, p_8f908f: 4.2641612072511235})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=3, coupling_map=None)
# SECTION
# NAME: EXECUTION
from qiskit import Aer, transpile, execute
backend_38560e66f390427885b4250ae60825b4 = Aer.get_backend(
    'aer_simulator_statevector')
counts = execute(qc, backend=backend_38560e66f390427885b4250ae60825b4,
    shots=7838).result().get_counts(qc)
RESULT = counts
