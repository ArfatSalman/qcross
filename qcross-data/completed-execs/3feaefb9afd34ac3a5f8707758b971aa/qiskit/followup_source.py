# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZXGate(3.813624597382902), qargs=[qr[1], qr[7]], cargs=[])
qc.append(HGate(), qargs=[qr[3]], cargs=[])
qc.append(U1Gate(1.7474579084583979), qargs=[qr[5]], cargs=[])
qc.append(YGate(), qargs=[qr[1]], cargs=[])
qc.append(CZGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(U1Gate(2.3042652898695457), qargs=[qr[6]], cargs=[])
qc.append(UGate(2.879770697683128, 2.335112883423633, 4.1410857855717005), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[5]], cargs=[])
qc.append(U2Gate(4.529061112043725, 0.1128558241378929), qargs=[qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(SXGate(), qargs=[qr[4]], cargs=[])
qc.append(HGate(), qargs=[qr[0]], cargs=[])
qc.append(CXGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(SXGate(), qargs=[qr[2]], cargs=[])
qc.append(U1Gate(2.0589291173378608), qargs=[qr[5]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[6], qr[4], qr[2], qr[7]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[7]], cargs=[])
qc.append(RYYGate(0.1445200040685528), qargs=[qr[2], qr[6]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(CUGate(2.2742238751077037, 5.678583788689636, 5.945356410023023, 1.2692738094959353), qargs=[qr[5], qr[2]], cargs=[])
qc.append(YGate(), qargs=[qr[5]], cargs=[])
qc.append(HGate(), qargs=[qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[3], qr[5], qr[7]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=['rx', 'ry', 'rz', 'p', 'cx'], optimization_level=1, coupling_map=None)# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_bda6578239184cc59dd273fc9f26c254 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_bda6578239184cc59dd273fc9f26c254, shots=2771).result().get_counts(qc)
RESULT = counts
