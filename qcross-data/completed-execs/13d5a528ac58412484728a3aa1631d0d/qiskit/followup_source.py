# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(2, name='qr')
cr = ClassicalRegister(2, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(SwapGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(RZXGate(3.8834807859507263), qargs=[qr[1], qr[0]], cargs=[])
qc.append(SwapGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(UGate(4.973624404177978, 1.450846828228022, 5.424728583609293), qargs=[qr[0]], cargs=[])
qc.append(CRXGate(3.510034154259637), qargs=[qr[1], qr[0]], cargs=[])
qc.append(RZXGate(1.9764943500940788), qargs=[qr[1], qr[0]], cargs=[])
qc.append(RXGate(1.444335936996841), qargs=[qr[1]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(UGate(0.7650180880812659, 1.1640465366080328, 3.351987550000961), qargs=[qr[1]], cargs=[])
qc.append(U2Gate(2.138082427163418, 5.230899032902529), qargs=[qr[1]], cargs=[])
qc.append(CPhaseGate(0.554577471370062), qargs=[qr[0], qr[1]], cargs=[])
qc.append(TGate(), qargs=[qr[1]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(U3Gate(0.9335631365840328, 4.520121169686029, 5.198491695816633), qargs=[qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[1]], cargs=[])
qc.append(HGate(), qargs=[qr[1]], cargs=[])
qc.append(CRXGate(3.4913681561376415), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[1]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: QASM_CONVERSION
qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=['ccx', 'h'], optimization_level=0, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_9a8e4da43db848a6bb6491f26fb71956 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_9a8e4da43db848a6bb6491f26fb71956, shots=346).result().get_counts(qc)
RESULT = counts
