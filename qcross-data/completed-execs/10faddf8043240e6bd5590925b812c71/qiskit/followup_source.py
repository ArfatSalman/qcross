# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(3, name='qr')
cr = ClassicalRegister(3, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(CSXGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(U3Gate(5.449671872109171, 3.00254832672447, 1.991190402029831), qargs=[qr[1]], cargs=[])
qc.append(CCXGate(), qargs=[qr[0], qr[2], qr[1]], cargs=[])
qc.append(CU3Gate(3.490361155617595, 2.1967031852441936, 3.6089446638145946), qargs=[qr[2], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(HGate(), qargs=[qr[2]], cargs=[])
qc.append(CUGate(5.96415316326551, 5.459163154688654, 3.541730522116933, 2.478896182682137), qargs=[qr[1], qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CXGate(), qargs=[qr[1], qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=None)
# SECTION
# NAME: QASM_CONVERSION
qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_48791d01d8514928877cc41b974fdb3c = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_48791d01d8514928877cc41b974fdb3c, shots=489).result().get_counts(qc)
RESULT = counts
