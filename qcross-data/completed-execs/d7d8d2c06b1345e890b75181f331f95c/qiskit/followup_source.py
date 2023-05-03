# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(6, name='qr')
cr = ClassicalRegister(6, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(SXdgGate(), qargs=[qr[5]], cargs=[])
qc.append(RZGate(0.6386974670970621), qargs=[qr[2]], cargs=[])
qc.append(SdgGate(), qargs=[qr[3]], cargs=[])
qc.append(CPhaseGate(4.103056419716538), qargs=[qr[1], qr[4]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[1], qr[0], qr[3]], cargs=[])
qc.append(CPhaseGate(1.57456137798405), qargs=[qr[0], qr[3]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[4], qr[5], qr[2]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[3], qr[1]], cargs=[])
qc.append(RYGate(4.436548686510933), qargs=[qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[5]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=['cx', 'h', 's', 't'], optimization_level=0, coupling_map=None)# SECTION
# NAME: QASM_CONVERSION

qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_31052af679fd4580b78c31f04a4e3330 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_31052af679fd4580b78c31f04a4e3330, shots=1385).result().get_counts(qc)
RESULT = counts
