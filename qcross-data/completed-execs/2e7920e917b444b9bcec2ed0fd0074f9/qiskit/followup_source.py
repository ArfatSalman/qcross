# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[6], qr[3]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[1], qr[7]], cargs=[])
qc.append(CCXGate(), qargs=[qr[5], qr[9], qr[7]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[9]], cargs=[])
qc.append(XGate(), qargs=[qr[8]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[1], qr[6]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[4], qr[8]], cargs=[])
qc.append(CCXGate(), qargs=[qr[4], qr[9], qr[5]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[4], qr[0], qr[9]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CSwapGate(), qargs=[qr[0], qr[4], qr[1]], cargs=[])
subcircuit.append(iSwapGate(), qargs=[qr[6], qr[5]], cargs=[])
subcircuit.append(UGate(2.438459595578943, 3.326780904591333, 3.4232119351142516), qargs=[qr[3]], cargs=[])
subcircuit.append(PhaseGate(0.4827903095199283), qargs=[qr[8]], cargs=[])
subcircuit.append(ECRGate(), qargs=[qr[1], qr[8]], cargs=[])
subcircuit.append(SwapGate(), qargs=[qr[1], qr[7]], cargs=[])
subcircuit.append(iSwapGate(), qargs=[qr[2], qr[7]], cargs=[])
subcircuit.append(RCCXGate(), qargs=[qr[2], qr[0], qr[5]], cargs=[])
subcircuit.append(CUGate(2.862865991712737, 6.0504088665633065, 1.7203758404994713, 2.8704483107274004), qargs=[qr[3], qr[1]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[7], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(CRZGate(2.586208953975239), qargs=[qr[1], qr[2]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_51b36a = QuantumRegister(5, name='qr_51b36a')
qc.add_register(qr_51b36a)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=['rx', 'ry', 'rz', 'p', 'cx'],
    optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_8769e8bb249247e5b6bba98f40b96cab = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_8769e8bb249247e5b6bba98f40b96cab, shots=5542).result().get_counts(qc)
RESULT = counts
