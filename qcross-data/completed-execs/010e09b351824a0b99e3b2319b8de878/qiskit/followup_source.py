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
p_0272f7 = Parameter('p_0272f7')
p_ea3f54 = Parameter('p_ea3f54')
p_0ac6c9 = Parameter('p_0ac6c9')
p_4e1de3 = Parameter('p_4e1de3')
p_7a489b = Parameter('p_7a489b')
p_74b354 = Parameter('p_74b354')
p_331ab9 = Parameter('p_331ab9')
p_2c12c6 = Parameter('p_2c12c6')
p_41dadf = Parameter('p_41dadf')
p_12df2a = Parameter('p_12df2a')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(9, name='qr')
cr = ClassicalRegister(9, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_2c12c6), qargs=[qr[8]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[4]], cargs=[])
qc.append(CUGate(p_41dadf, p_7a489b, p_12df2a, p_4e1de3), qargs=[qr[0], qr[
    6]], cargs=[])
qc.append(SdgGate(), qargs=[qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[8], qr[7], qr[5]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[5]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[8]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[3], qr[2], qr[0]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(CU1Gate(p_0ac6c9), qargs=[qr[8], qr[3]], cargs=[])
qc.append(CRZGate(p_74b354), qargs=[qr[5], qr[8]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[7]], cargs=[])
qc.append(CHGate(), qargs=[qr[6], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[3], qr[0]], cargs=[])
qc.append(CRZGate(p_ea3f54), qargs=[qr[1], qr[2]], cargs=[])
qc.append(U2Gate(p_0272f7, p_331ab9), qargs=[qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_0272f7: 2.5163050709890156,
    p_ea3f54: 2.586208953975239,
    p_0ac6c9: 3.2142159669963557,
    p_4e1de3: 5.987304452123941,
    p_7a489b: 5.897054719225356,
    p_74b354: 1.4112277317699358,
    p_331ab9: 2.1276323672732023,
    p_2c12c6: 6.163759533339787,
    p_41dadf: 0.5112149185250571,
    p_12df2a: 2.3864521352475245,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_a90048b9f81a45bf9b1e24cfda2c9128 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_a90048b9f81a45bf9b1e24cfda2c9128, shots=3919).result().get_counts(qc)
RESULT = counts
