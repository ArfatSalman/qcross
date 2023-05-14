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
p_e377c8 = Parameter('p_e377c8')
p_9593ea = Parameter('p_9593ea')
p_751f8c = Parameter('p_751f8c')
p_7227de = Parameter('p_7227de')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_751f8c), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[6]], cargs=[])
qc.append(CRXGate(p_9593ea), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CRZGate(p_e377c8), qargs=[qr[1], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[7], qr[6], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(p_7227de), qargs=[qr[6], qr[7]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_e377c8: 1.0296448789776642,
    p_9593ea: 5.987304452123941,
    p_751f8c: 6.163759533339787,
    p_7227de: 1.740253089260498,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_d4064f0baf9b4fe29e10b162e1fa9912 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_d4064f0baf9b4fe29e10b162e1fa9912, shots=2771).result().get_counts(qc)
RESULT = counts
