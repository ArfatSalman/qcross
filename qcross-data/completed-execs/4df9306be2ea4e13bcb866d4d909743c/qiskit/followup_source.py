# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_6737bd = Parameter('p_6737bd')
p_b168d0 = Parameter('p_b168d0')
p_89415d = Parameter('p_89415d')
p_523a69 = Parameter('p_523a69')
p_9cb6f3 = Parameter('p_9cb6f3')
p_2d91b4 = Parameter('p_2d91b4')
p_c146ca = Parameter('p_c146ca')
p_a51026 = Parameter('p_a51026')
p_e5e707 = Parameter('p_e5e707')
p_7f3871 = Parameter('p_7f3871')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(11, name='qr')
cr = ClassicalRegister(11, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_c146ca), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_6737bd), qargs=[qr[6], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(CCXGate(), qargs=[qr[5], qr[9], qr[7]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[7]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[10], qr[6], qr[8]], cargs=[])
qc.append(RZGate(p_b168d0), qargs=[qr[0]], cargs=[])
qc.append(CCXGate(), qargs=[qr[7], qr[10], qr[2]], cargs=[])
qc.append(SdgGate(), qargs=[qr[7]], cargs=[])
qc.append(U2Gate(p_7f3871, p_9cb6f3), qargs=[qr[10]], cargs=[])
qc.append(CSXGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[7]], cargs=[])
qc.append(CU1Gate(p_523a69), qargs=[qr[9], qr[0]], cargs=[])
qc.append(RZGate(p_a51026), qargs=[qr[6]], cargs=[])
qc.append(U2Gate(p_2d91b4, p_e5e707), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[0]], cargs=[])
qc.append(RZZGate(p_89415d), qargs=[qr[4], qr[0]], cargs=[])
qc.append(TGate(), qargs=[qr[0]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_04780e = QuantumRegister(4, name='qr_04780e')
qc.add_register(qr_04780e)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_6737bd: 4.2641612072511235, p_b168d0: 4.229610589867865, p_89415d: 3.950837470808744, p_523a69: 4.028174522740928, p_9cb6f3: 4.6235667602042065, p_2d91b4: 2.5163050709890156, p_c146ca: 6.163759533339787, p_a51026: 5.0063780207098425, p_e5e707: 2.1276323672732023, p_7f3871: 4.214504315296764})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_b29f0a010587483594633e8555040d76 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_b29f0a010587483594633e8555040d76, shots=7838).result().get_counts(qc)
RESULT = counts
