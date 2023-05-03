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
p_22f003 = Parameter('p_22f003')
p_b0e1f1 = Parameter('p_b0e1f1')
p_74570c = Parameter('p_74570c')
p_2ab273 = Parameter('p_2ab273')
p_0e1639 = Parameter('p_0e1639')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(11, name='qr')
cr = ClassicalRegister(11, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_22f003), qargs=[qr[6], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(CCXGate(), qargs=[qr[5], qr[9], qr[7]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[7]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[10], qr[6], qr[8]], cargs=[])
qc.append(RZGate(p_74570c), qargs=[qr[0]], cargs=[])
qc.append(CCXGate(), qargs=[qr[7], qr[10], qr[2]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(RZGate(4.940217775579305), qargs=[qr[1]], cargs=[])
subcircuit.append(RYYGate(0.6724371252296606), qargs=[qr[9], qr[0]], cargs=[])
subcircuit.append(PhaseGate(p_0e1639), qargs=[qr[0]], cargs=[])
subcircuit.append(ECRGate(), qargs=[qr[3], qr[0]], cargs=[])
subcircuit.append(PhaseGate(p_2ab273), qargs=[qr[0]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(SdgGate(), qargs=[qr[7]], cargs=[])
qc.append(U2Gate(4.214504315296764, p_b0e1f1), qargs=[qr[10]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_22f003: 4.2641612072511235,
    p_b0e1f1: 4.6235667602042065,
    p_74570c: 4.229610589867865,
    p_2ab273: 0.4827903095199283,
    p_0e1639: 5.5146057452272546,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 8], [0, 13], [1, 0], [2, 7], [3, 4], [3, 8], [3, 9], [3, 14], [4, 3], [5, 7], [5, 10], [5, 11], [6, 9], [7, 2], [7, 5], [7, 8], [8, 0], [8, 3], [8, 7], [8, 14], [9, 3], [9, 6], [10, 5], [11, 5], [12, 13], [13, 0], [13, 12], [14, 3], [14, 8]])
# SECTION
# NAME: QASM_CONVERSION

qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_542c934a40bc4425a988618767452a57 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_542c934a40bc4425a988618767452a57, shots=7838).result().get_counts(qc)
RESULT = counts
