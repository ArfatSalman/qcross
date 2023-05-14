# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_6981a8 = Parameter('p_6981a8')
p_ab5b20 = Parameter('p_ab5b20')
p_41c813 = Parameter('p_41c813')
p_209e7d = Parameter('p_209e7d')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(7, name='qr')
cr = ClassicalRegister(7, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_ab5b20), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[3]], cargs=[])
qc.append(CRXGate(p_209e7d), qargs=[qr[2], qr[5]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[6], qr[0], qr[1], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[4], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[2], qr[1], qr[5]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(ECRGate(), qargs=[qr[6], qr[3]], cargs=[])
qc.append(SdgGate(), qargs=[qr[6]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CZGate(), qargs=[qr[4], qr[1]], cargs=[])
subcircuit.append(IGate(), qargs=[qr[1]], cargs=[])
subcircuit.append(RXGate(p_6981a8), qargs=[qr[0]], cargs=[])
subcircuit.append(RZXGate(4.563562108824195), qargs=[qr[4], qr[0]], cargs=[])
subcircuit.append(C3XGate(p_41c813), qargs=[qr[4], qr[6], qr[2], qr[1]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(RCCXGate(), qargs=[qr[2], qr[5], qr[0]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_0b0641 = QuantumRegister(3, name='qr_0b0641')
qc.add_register(qr_0b0641)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_6981a8: 0.2906326206587185, p_ab5b20: 6.163759533339787, p_41c813: 5.94477504571567, p_209e7d: 2.0099472182748075})
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=['ccx', 'h'], optimization_level=2,
    coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_7281520708bc4a3994ba0cf15dbca2c8 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_7281520708bc4a3994ba0cf15dbca2c8, shots=1959).result().get_counts(qc)
RESULT = counts
