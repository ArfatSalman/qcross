
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
qc.append(HGate(), qargs=[qr[1]], cargs=[])
qc.append(U3Gate(0.2435863694263356,4.952605016068409,1.0462631235631594), qargs=[qr[0]], cargs=[])
qc.append(CRZGate(3.8430137210716477), qargs=[qr[0], qr[3]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[1], qr[2], qr[0]], cargs=[])
qc.append(RYYGate(1.9038331447854693), qargs=[qr[0], qr[3]], cargs=[])
qc.append(SdgGate(), qargs=[qr[3]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[0], qr[2], qr[3], qr[1]], cargs=[])
qc.append(DCXGate(), qargs=[qr[3], qr[0]], cargs=[])
qc.append(U2Gate(2.315671616264609,3.642280082030703), qargs=[qr[1]], cargs=[])
qc.append(DCXGate(), qargs=[qr[1], qr[3]], cargs=[])

# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=None)

# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_4bc00c07bc264432949557ba54b1a0a7 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_4bc00c07bc264432949557ba54b1a0a7, shots=692).result().get_counts(qc)
RESULT = counts