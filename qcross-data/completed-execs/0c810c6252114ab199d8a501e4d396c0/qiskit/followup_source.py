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
p_879f8b = Parameter('p_879f8b')
p_6f6166 = Parameter('p_6f6166')
p_0b24f3 = Parameter('p_0b24f3')
p_4f0dc0 = Parameter('p_4f0dc0')
p_b4f3fe = Parameter('p_b4f3fe')
p_0ac045 = Parameter('p_0ac045')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(9, name='qr')
cr = ClassicalRegister(9, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_879f8b), qargs=[qr[8]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[4]], cargs=[])
qc.append(CUGate(p_4f0dc0, 5.897054719225356, 2.3864521352475245, 
    5.987304452123941), qargs=[qr[0], qr[6]], cargs=[])
qc.append(SdgGate(), qargs=[qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[8], qr[7], qr[5]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[5]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[8]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[3], qr[2], qr[0]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(CU1Gate(p_b4f3fe), qargs=[qr[8], qr[3]], cargs=[])
qc.append(CRZGate(1.4112277317699358), qargs=[qr[5], qr[8]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[7]], cargs=[])
qc.append(CHGate(), qargs=[qr[6], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[3], qr[0]], cargs=[])
qc.append(CRZGate(p_0b24f3), qargs=[qr[1], qr[2]], cargs=[])
qc.append(U2Gate(p_0ac045, p_6f6166), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[8]], cargs=[])
qc.append(CCXGate(), qargs=[qr[0], qr[6], qr[1]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[4], qr[0], qr[1]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_879f8b: 6.163759533339787,
    p_6f6166: 2.1276323672732023,
    p_0b24f3: 2.586208953975239,
    p_4f0dc0: 0.5112149185250571,
    p_b4f3fe: 3.2142159669963557,
    p_0ac045: 2.5163050709890156,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_0c42bca73a234715852cfc6c28116c30 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_0c42bca73a234715852cfc6c28116c30, shots=3919).result().get_counts(qc)
RESULT = counts
