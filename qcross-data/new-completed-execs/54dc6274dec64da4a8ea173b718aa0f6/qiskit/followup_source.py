# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(CRXGate(0.027261864368738644), qargs=[qr[8], qr[1]], cargs=[])
qc.append(CXGate(), qargs=[qr[6], qr[9]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(CRXGate(0.9075502808788635), qargs=[qr[6], qr[8]], cargs=[])
qc.append(ECRGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(CSwapGate(), qargs=[qr[2], qr[8], qr[0]], cargs=[])
qc.append(RGate(6.099682100802839, 2.494306691997326), qargs=[qr[8]], cargs=[])
qc.append(RZXGate(3.7330617289797328), qargs=[qr[5], qr[2]], cargs=[])
qc.append(RYGate(3.5568415538710556), qargs=[qr[8]], cargs=[])
qc.append(U3Gate(1.0222809503303705, 1.6895773379952999, 3.5291798838720747), qargs=[qr[8]], cargs=[])
qc.append(CYGate(), qargs=[qr[5], qr[6]], cargs=[])
qc.append(U2Gate(3.044931199643564, 1.2044318302402206), qargs=[qr[2]], cargs=[])
qc.append(CSwapGate(), qargs=[qr[1], qr[6], qr[8]], cargs=[])
qc.append(SXGate(), qargs=[qr[5]], cargs=[])
qc.append(UGate(3.5905146351798125, 1.4398630066945612, 4.930260809283397), qargs=[qr[7]], cargs=[])
qc.append(UGate(1.945778856930902, 5.959001893737209, 3.3890130318399554), qargs=[qr[6]], cargs=[])
qc.append(CRXGate(6.15516938685536), qargs=[qr[5], qr[1]], cargs=[])
qc.append(U2Gate(4.734912763130236, 2.0633539972431736), qargs=[qr[7]], cargs=[])
qc.append(RGate(3.329578139088272, 2.6679935782057154), qargs=[qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[3]], cargs=[])
qc.append(CRXGate(0.9250999602143393), qargs=[qr[6], qr[0]], cargs=[])
qc.append(RZXGate(3.9273226264569736), qargs=[qr[5], qr[1]], cargs=[])
qc.append(CPhaseGate(2.3272657174534204), qargs=[qr[5], qr[6]], cargs=[])
qc.append(CSwapGate(), qargs=[qr[2], qr[5], qr[7]], cargs=[])
qc.append(RYGate(3.9320786554188296), qargs=[qr[6]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(U2Gate(1.5093939547937507, 0.3575732764804263), qargs=[qr[6]], cargs=[])
qc.append(CRXGate(3.1862838323251004), qargs=[qr[2], qr[5]], cargs=[])
qc.append(CHGate(), qargs=[qr[4], qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1, coupling_map=None)# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_d7d77b3a2cc04c3c9b9433ac0ccb6546 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_d7d77b3a2cc04c3c9b9433ac0ccb6546, shots=5542).result().get_counts(qc)
RESULT = counts
