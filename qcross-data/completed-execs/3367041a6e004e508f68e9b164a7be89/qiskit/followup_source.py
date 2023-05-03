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
p_5e2272 = Parameter('p_5e2272')
p_f1d349 = Parameter('p_f1d349')
p_6cc0de = Parameter('p_6cc0de')
p_093bc9 = Parameter('p_093bc9')
p_96f88b = Parameter('p_96f88b')
p_4e3e7e = Parameter('p_4e3e7e')
p_5c737b = Parameter('p_5c737b')
p_47b2f7 = Parameter('p_47b2f7')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CRXGate(p_093bc9), qargs=[qr[4], qr[3]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(CRZGate(p_6cc0de), qargs=[qr[3], qr[4]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[4]], cargs=[])
qc.append(RYYGate(p_5c737b), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[4]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[4]], cargs=[])
qc.append(CUGate(p_5e2272, p_4e3e7e, 4.623446645668956, p_f1d349), qargs=[
    qr[1], qr[4]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(p_96f88b), qargs=[qr[0], qr[2]], cargs=[])
qc.append(CU1Gate(p_47b2f7), qargs=[qr[3], qr[0]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_82f68e = QuantumRegister(2, name='qr_82f68e')
qc.add_register(qr_82f68e)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_5e2272: 5.708725119517347,
    p_f1d349: 3.865496458458116,
    p_6cc0de: 1.0296448789776642,
    p_093bc9: 2.0099472182748075,
    p_96f88b: 5.398622178940033,
    p_4e3e7e: 4.167661441102218,
    p_5c737b: 1.6723037552953224,
    p_47b2f7: 3.2142159669963557,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_6b97a9ce981e43f3a0b39312d3d1f4da = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_6b97a9ce981e43f3a0b39312d3d1f4da, shots=979).result().get_counts(qc)
RESULT = counts
