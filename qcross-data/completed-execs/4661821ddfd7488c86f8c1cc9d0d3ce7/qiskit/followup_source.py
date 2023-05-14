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
p_8fbc55 = Parameter('p_8fbc55')
p_57585f = Parameter('p_57585f')
p_285ae7 = Parameter('p_285ae7')
p_0602a6 = Parameter('p_0602a6')
p_0a2147 = Parameter('p_0a2147')
p_bb1901 = Parameter('p_bb1901')
p_82597a = Parameter('p_82597a')
p_34e682 = Parameter('p_34e682')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(6, name='qr')
cr = ClassicalRegister(6, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_34e682), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_0602a6), qargs=[qr[2], qr[4]], cargs=[])
qc.append(CUGate(p_285ae7, p_bb1901, p_8fbc55, p_57585f), qargs=[qr[2], qr[
    3]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[4], qr[0], qr[2]], cargs=[])
qc.append(CCXGate(), qargs=[qr[1], qr[5], qr[0]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[4], qr[3], qr[5], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[5], qr[3], qr[4]], cargs=[])
qc.append(SGate(), qargs=[qr[5]], cargs=[])
qc.append(CRZGate(p_82597a), qargs=[qr[1], qr[5]], cargs=[])
qc.append(RZGate(p_0a2147), qargs=[qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[2], qr[1], qr[3]], cargs=[])
qc.append(CU1Gate(3.2142159669963557), qargs=[qr[3], qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_8fbc55: 2.3864521352475245,
    p_57585f: 5.987304452123941,
    p_285ae7: 0.5112149185250571,
    p_0602a6: 4.2641612072511235,
    p_0a2147: 4.229610589867865,
    p_bb1901: 5.897054719225356,
    p_82597a: 4.167661441102218,
    p_34e682: 6.163759533339787,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_f175f4ada92a40f99b4c8bec2af805e3 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_f175f4ada92a40f99b4c8bec2af805e3, shots=1385).result().get_counts(qc)
RESULT = counts
