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
p_bec6f4 = Parameter('p_bec6f4')
p_6e47ec = Parameter('p_6e47ec')
p_b52923 = Parameter('p_b52923')
p_b0edf1 = Parameter('p_b0edf1')
p_7fdf26 = Parameter('p_7fdf26')
p_c19a9b = Parameter('p_c19a9b')
p_4a7236 = Parameter('p_4a7236')
p_eca484 = Parameter('p_eca484')
p_7c75a3 = Parameter('p_7c75a3')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_4a7236), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_7fdf26), qargs=[qr[6], qr[3]], cargs=[])
qc.append(CRXGate(p_bec6f4), qargs=[qr[1], qr[7]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CPhaseGate(4.63837786161633), qargs=[qr[3], qr[0]], cargs=[])
subcircuit.append(U2Gate(p_c19a9b, p_b0edf1), qargs=[qr[8]], cargs=[])
subcircuit.append(CXGate(), qargs=[qr[2], qr[4]], cargs=[])
subcircuit.append(SXGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(CRZGate(p_b52923), qargs=[qr[0], qr[5]], cargs=[])
subcircuit.append(RCCXGate(), qargs=[qr[9], qr[1], qr[8]], cargs=[])
subcircuit.append(RXXGate(p_6e47ec), qargs=[qr[4], qr[6]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CCXGate(), qargs=[qr[5], qr[9], qr[7]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[9]], cargs=[])
qc.append(XGate(), qargs=[qr[8]], cargs=[])
qc.append(CRZGate(p_7c75a3), qargs=[qr[1], qr[6]], cargs=[])
qc.append(RZGate(p_eca484), qargs=[qr[1]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_bec6f4: 5.987304452123941,
    p_6e47ec: 5.25962645863375,
    p_b52923: 2.008796895454228,
    p_b0edf1: 0.07157463504881167,
    p_7fdf26: 4.2641612072511235,
    p_c19a9b: 5.887184334931191,
    p_4a7236: 6.163759533339787,
    p_eca484: 4.229610589867865,
    p_7c75a3: 4.167661441102218,
})

# SECTION
# NAME: QASM_CONVERSION

qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_5ac6b0efd4d34c1190bcd749a73b9194 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_5ac6b0efd4d34c1190bcd749a73b9194, shots=5542).result().get_counts(qc)
RESULT = counts
