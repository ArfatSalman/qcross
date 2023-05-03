
# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter

# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(2, name='qr')
cr = ClassicalRegister(2, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(CPhaseGate(3.5690023406020117), qargs=[qr[1], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(CRXGate(0.5834164558695757), qargs=[qr[1], qr[0]], cargs=[])
qc.append(PhaseGate(3.894930545586774), qargs=[qr[0]], cargs=[])
qc.append(IGate(), qargs=[qr[1]], cargs=[])
qc.append(CZGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(U2Gate(5.482574947566191,0.8373110034524618), qargs=[qr[0]], cargs=[])
qc.append(PhaseGate(0.3578418944802631), qargs=[qr[1]], cargs=[])
qc.append(SwapGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[1]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CPhaseGate(5.397112728340784), qargs=[qr[1], qr[0]], cargs=[])
qc.append(SXGate(), qargs=[qr[1]], cargs=[])
qc.append(CRYGate(1.174494077676677), qargs=[qr[0], qr[1]], cargs=[])
qc.append(HGate(), qargs=[qr[1]], cargs=[])
qc.append(YGate(), qargs=[qr[0]], cargs=[])
qc.append(RGate(2.8467414627241734,3.5481884646507713), qargs=[qr[1]], cargs=[])
qc.append(RZXGate(3.2681088907886817), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CRYGate(5.6914225992075504), qargs=[qr[0], qr[1]], cargs=[])
qc.append(U3Gate(4.266994303739899,1.914216390388542,1.0614410494494415), qargs=[qr[1]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CU3Gate(0.6949120689264752,0.9164071466076199,5.136397164125832), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CRYGate(2.843774029250561), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CU3Gate(0.6994648472584757,3.50667959618503,5.986466284185033), qargs=[qr[1], qr[0]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])

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
backend_7490686d89f54e3b88aa7b9d2587fbb5 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_7490686d89f54e3b88aa7b9d2587fbb5, shots=346).result().get_counts(qc)
RESULT = counts