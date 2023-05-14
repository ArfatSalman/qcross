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
p_be1456 = Parameter('p_be1456')
p_9729f9 = Parameter('p_9729f9')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(3, name='qr')
cr = ClassicalRegister(3, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_9729f9), qargs=[qr[1]], cargs=[])
qc.append(CHGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[2], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(SGate(), qargs=[qr[2]], cargs=[])
qc.append(SdgGate(), qargs=[qr[1]], cargs=[])
qc.append(CRXGate(p_be1456), qargs=[qr[0], qr[2]], cargs=[])
qc.append(SGate(), qargs=[qr[2]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_064354 = QuantumRegister(5, name='qr_064354')
qc.add_register(qr_064354)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_be1456: 5.987304452123941,
    p_9729f9: 6.163759533339787,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_7d9a848f73a64e34a4572ddbf25f8d58 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_7d9a848f73a64e34a4572ddbf25f8d58, shots=489).result().get_counts(qc)
RESULT = counts
