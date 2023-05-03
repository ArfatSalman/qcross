# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(4, name='qr')
cr = ClassicalRegister(4, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(CYGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(RZXGate(4.992926923750951), qargs=[qr[1], qr[3]], cargs=[])
qc.append(RYYGate(1.9555057510547085), qargs=[qr[0], qr[1]], cargs=[])
qc.append(U1Gate(0.8252193008316542), qargs=[qr[1]], cargs=[])
qc.append(CSwapGate(), qargs=[qr[3], qr[1], qr[0]], cargs=[])
qc.append(SdgGate(), qargs=[qr[1]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(RYYGate(3.416474043372992), qargs=[qr[1], qr[3]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(CRZGate(3.738048947778281), qargs=[qr[2], qr[0]], cargs=[])
qc.append(CXGate(), qargs=[qr[2], qr[1]], cargs=[])
qc.append(RXXGate(1.2110824459718403), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CPhaseGate(0.538151089952194), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CCXGate(), qargs=[qr[0], qr[1], qr[3]], cargs=[])
qc.append(RZGate(1.2470325800417235), qargs=[qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(CUGate(0.8310820236250993, 5.196031699053289, 1.9585166986172349, 4.659181440347051), qargs=[qr[3], qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=3, coupling_map=None)
# SECTION
# NAME: EXECUTION
from qiskit import Aer, transpile, execute
backend_f8ca00ff58dc49ae879f6d5c4ee3c629 = Aer.get_backend('aer_simulator_matrix_product_state')
counts = execute(qc, backend=backend_f8ca00ff58dc49ae879f6d5c4ee3c629, shots=692).result().get_counts(qc)
RESULT = counts