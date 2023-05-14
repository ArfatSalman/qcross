# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[2]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[4]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(C3XGate(5.94477504571567), qargs=[qr[4], qr[3], qr[0], qr
    [1]], cargs=[])
subcircuit.append(CSwapGate(), qargs=[qr[3], qr[1], qr[0]], cargs=[])
subcircuit.append(HGate(), qargs=[qr[3]], cargs=[])
subcircuit.append(CRXGate(5.091930552861214), qargs=[qr[4], qr[3]], cargs=[])
subcircuit.append(SXGate(), qargs=[qr[3]], cargs=[])
subcircuit.append(CRZGate(2.008796895454228), qargs=[qr[3], qr[2]], cargs=[])
subcircuit.append(YGate(), qargs=[qr[3]], cargs=[])
subcircuit.append(RCCXGate(), qargs=[qr[1], qr[0], qr[4]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CSXGate(), qargs=[qr[0], qr[3]], cargs=[])
qc.append(ECRGate(), qargs=[qr[2], qr[4]], cargs=[])
qc.append(CRXGate(2.0099472182748075), qargs=[qr[1], qr[2]], cargs=[])
qc.append(SGate(), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(1.0296448789776642), qargs=[qr[2], qr[1]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(RYYGate(1.6723037552953224), qargs=[qr[3], qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[4]], cargs=[])
qc.append(TGate(), qargs=[qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[3]], cargs=[])
qc.append(SGate(), qargs=[qr[1]], cargs=[])
qc.append(CUGate(5.708725119517347, 4.167661441102218, 4.623446645668956, 
    3.865496458458116), qargs=[qr[0], qr[1]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[0]], cargs=[])
qc.append(RYYGate(5.398622178940033), qargs=[qr[3], qr[4]], cargs=[])
qc.append(CU1Gate(3.2142159669963557), qargs=[qr[2], qr[3]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_31c29b = QuantumRegister(3, name='qr_31c29b')
qc.add_register(qr_31c29b)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_073f9811f214420abad498e0c08c3ed1 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_073f9811f214420abad498e0c08c3ed1, shots=979).result().get_counts(qc)
RESULT = counts
