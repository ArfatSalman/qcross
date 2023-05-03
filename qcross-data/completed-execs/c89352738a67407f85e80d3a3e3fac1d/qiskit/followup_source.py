# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS
# SECTION
# NAME: PARAMETERS
p_435387 = Parameter('p_435387')
p_ad6c48 = Parameter('p_ad6c48')
p_7baf10 = Parameter('p_7baf10')
p_3c5bca = Parameter('p_3c5bca')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(4, name='qr')
cr = ClassicalRegister(4, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_435387), qargs=[qr[1]], cargs=[])
qc.append(RZZGate(p_7baf10), qargs=[qr[2], qr[3]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(CUGate(p_3c5bca, 5.897054719225356, 2.3864521352475245, p_ad6c48),
    qargs=[qr[0], qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_435387: 6.163759533339787,
    p_ad6c48: 5.987304452123941,
    p_7baf10: 4.066449154047175,
    p_3c5bca: 0.5112149185250571,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_e776c95208ee4e48a041b1a0ce4ff81d = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_e776c95208ee4e48a041b1a0ce4ff81d, shots=692).result().get_counts(qc)
RESULT = counts
