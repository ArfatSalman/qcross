# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_d17c51 = Parameter('p_d17c51')
p_ec6063 = Parameter('p_ec6063')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_d17c51), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[6]], cargs=[])
qc.append(CRXGate(p_ec6063), qargs=[qr[0], qr[6]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_c86ed0 = QuantumRegister(2, name='qr_c86ed0')
qc.add_register(qr_c86ed0)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_d17c51: 6.163759533339787, p_ec6063: 5.987304452123941})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_1e04d2dabcdb45f28b08fb8df19779b5 = Aer.get_backend('aer_simulator_matrix_product_state')
counts = execute(qc, backend=backend_1e04d2dabcdb45f28b08fb8df19779b5, shots=2771).result().get_counts(qc)
RESULT = counts
