# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_dda1d3 = Parameter('p_dda1d3')
p_ce61f1 = Parameter('p_ce61f1')
p_d9b1ff = Parameter('p_d9b1ff')
p_98dc6e = Parameter('p_98dc6e')
p_e3b9a1 = Parameter('p_e3b9a1')
p_1bb590 = Parameter('p_1bb590')
p_ac58f5 = Parameter('p_ac58f5')
p_a8532b = Parameter('p_a8532b')
p_42b602 = Parameter('p_42b602')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_a8532b), qargs=[qr[3]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CRXGate(p_dda1d3), qargs=[qr[4], qr[3]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(CRZGate(p_1bb590), qargs=[qr[3], qr[4]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[4]], cargs=[])
qc.append(RYYGate(1.6723037552953224), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[4]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[4]], cargs=[])
qc.append(CUGate(p_42b602, 4.167661441102218, p_98dc6e, p_d9b1ff), qargs=[qr[1], qr[4]], cargs=[])
qc.append(RZGate(p_ce61f1), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(p_e3b9a1), qargs=[qr[0], qr[2]], cargs=[])
qc.append(CU1Gate(3.2142159669963557), qargs=[qr[3], qr[0]], cargs=[])
qc.append(UGate(5.887184334931191, p_ac58f5, 1.4112277317699358), qargs=[qr[4]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(RYYGate(0.5501056885328758), qargs=[qr[3], qr[0]], cargs=[])
subcircuit.append(SXdgGate(), qargs=[qr[3]], cargs=[])
subcircuit.append(CRXGate(3.401136029677084), qargs=[qr[1], qr[2]], cargs=[])
subcircuit.append(RYYGate(0.6724371252296606), qargs=[qr[0], qr[4]], cargs=[])
subcircuit.append(SdgGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(iSwapGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CHGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[4]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_db075a = QuantumRegister(2, name='qr_db075a')
subcircuit.add_register(qr_db075a)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_dda1d3: 2.0099472182748075, p_ce61f1: 4.229610589867865, p_d9b1ff: 3.865496458458116, p_98dc6e: 4.623446645668956, p_e3b9a1: 5.398622178940033, p_1bb590: 1.0296448789776642, p_ac58f5: 0.07157463504881167, p_a8532b: 6.163759533339787, p_42b602: 5.708725119517347})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_ff8f16a1d5a2406895d5a6cdbffef9ed = Aer.get_backend('statevector_simulator')
counts = execute(qc, backend=backend_ff8f16a1d5a2406895d5a6cdbffef9ed, shots=979).result().get_counts(qc)
RESULT = counts
