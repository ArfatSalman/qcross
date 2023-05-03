
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
qc.append(DCXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(DCXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(UGate(4.403788193532198,5.238005217278175,2.414376925356305), qargs=[qr[1]], cargs=[])
qc.append(RGate(3.9800961208659213,2.54258238968427), qargs=[qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CRXGate(3.0761375449158193), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CSdgGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(YGate(), qargs=[qr[1]], cargs=[])
qc.append(CU3Gate(3.359364374345002,4.018048446348199,2.251031643786726), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CZGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(RGate(4.3040860238694725,4.7611258330830655), qargs=[qr[1]], cargs=[])
qc.append(DCXGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(DCXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CYGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(UGate(3.820196974130503,1.381440535002157,5.6467633400840755), qargs=[qr[1]], cargs=[])
qc.append(YGate(), qargs=[qr[1]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[1], qr[0]], cargs=[])

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
backend_1ead1f5c4766491b96e9a32f39b7cda8 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_1ead1f5c4766491b96e9a32f39b7cda8, shots=346).result().get_counts(qc)
RESULT = counts