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
qc.append(CPhaseGate(0.464603434869698), qargs=[qr[3], qr[0]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[1], qr[2], qr[3], qr[0]], cargs=[])
qc.append(CU3Gate(4.577871395666417, 2.824995733037649, 4.570764402928323), qargs=[qr[2], qr[0]], cargs=[])
qc.append(YGate(), qargs=[qr[2]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[1], qr[3], qr[0], qr[2]], cargs=[])
qc.append(SwapGate(), qargs=[qr[3], qr[0]], cargs=[])
qc.append(SwapGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(RYGate(4.123988453145662), qargs=[qr[3]], cargs=[])
qc.append(RXGate(5.977019956470354), qargs=[qr[0]], cargs=[])
qc.append(RYGate(5.340081963621594), qargs=[qr[0]], cargs=[])
qc.append(CXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(RZGate(0.902460456423349), qargs=[qr[2]], cargs=[])
qc.append(U1Gate(1.191082687926663), qargs=[qr[3]], cargs=[])
qc.append(RYGate(2.426038592845313), qargs=[qr[3]], cargs=[])
qc.append(CPhaseGate(1.9801508534447856), qargs=[qr[2], qr[0]], cargs=[])
qc.append(U1Gate(0.7620531016010672), qargs=[qr[3]], cargs=[])
qc.append(RZGate(1.1210417983863055), qargs=[qr[0]], cargs=[])
qc.append(C3XGate(), qargs=[qr[3], qr[2], qr[1], qr[0]], cargs=[])
qc.append(CU3Gate(3.3468514586446996, 0.09605123198475385, 1.9104022337738353), qargs=[qr[2], qr[0]], cargs=[])
qc.append(RYGate(5.21436875895587), qargs=[qr[2]], cargs=[])
qc.append(RYGate(1.876889866834255), qargs=[qr[2]], cargs=[])
qc.append(U3Gate(3.580262460733749, 2.5952409532269898, 0.3968947480833723), qargs=[qr[2]], cargs=[])
qc.append(U1Gate(1.8511699871735552), qargs=[qr[0]], cargs=[])
qc.append(RYYGate(0.8500918394546497), qargs=[qr[2], qr[0]], cargs=[])
qc.append(CU3Gate(1.4776100383750288, 4.796549499287292, 5.831783083594262), qargs=[qr[3], qr[1]], cargs=[])
qc.append(C3XGate(), qargs=[qr[2], qr[0], qr[3], qr[1]], cargs=[])
qc.append(CU3Gate(2.6606132436968934, 0.25042616078481367, 0.47890039592537104), qargs=[qr[3], qr[0]], cargs=[])
qc.append(RXGate(5.381463645700576), qargs=[qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
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
backend_33d9bd291abe4d75809e6d11d3b46f78 = Aer.get_backend('aer_simulator_matrix_product_state')
counts = execute(qc, backend=backend_33d9bd291abe4d75809e6d11d3b46f78, shots=692).result().get_counts(qc)
RESULT = counts