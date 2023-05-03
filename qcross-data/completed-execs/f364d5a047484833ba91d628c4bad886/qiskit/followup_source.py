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
p_299687 = Parameter('p_299687')
p_2d28aa = Parameter('p_2d28aa')
p_efba95 = Parameter('p_efba95')
p_c3019d = Parameter('p_c3019d')
p_0fe9c2 = Parameter('p_0fe9c2')
p_9640e8 = Parameter('p_9640e8')
p_0e9aa7 = Parameter('p_0e9aa7')
p_101f6d = Parameter('p_101f6d')
p_2ef906 = Parameter('p_2ef906')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(9, name='qr')
cr = ClassicalRegister(9, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_2d28aa), qargs=[qr[8]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[4]], cargs=[])
qc.append(CUGate(p_9640e8, 5.897054719225356, p_2ef906, p_0fe9c2), qargs=[
    qr[0], qr[6]], cargs=[])
qc.append(SdgGate(), qargs=[qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[8], qr[7], qr[5]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[5]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[8]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[3], qr[2], qr[0]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(CU1Gate(p_299687), qargs=[qr[8], qr[3]], cargs=[])
qc.append(CRZGate(p_c3019d), qargs=[qr[5], qr[8]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[7]], cargs=[])
qc.append(CHGate(), qargs=[qr[6], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[3], qr[0]], cargs=[])
qc.append(CRZGate(p_efba95), qargs=[qr[1], qr[2]], cargs=[])
qc.append(U2Gate(p_0e9aa7, p_101f6d), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[8]], cargs=[])
qc.append(CCXGate(), qargs=[qr[0], qr[6], qr[1]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_299687: 3.2142159669963557,
    p_2d28aa: 6.163759533339787,
    p_efba95: 2.586208953975239,
    p_c3019d: 1.4112277317699358,
    p_0fe9c2: 5.987304452123941,
    p_9640e8: 0.5112149185250571,
    p_0e9aa7: 2.5163050709890156,
    p_101f6d: 2.1276323672732023,
    p_2ef906: 2.3864521352475245,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_47b5c0d975b045d0993ac4ebd55697f0 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_47b5c0d975b045d0993ac4ebd55697f0, shots=3919).result().get_counts(qc)
RESULT = counts
