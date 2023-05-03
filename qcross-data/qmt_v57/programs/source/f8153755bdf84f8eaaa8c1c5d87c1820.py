
# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter

# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(11, name='qr')
cr = ClassicalRegister(11, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(CRXGate(4.905634676582973), qargs=[qr[4], qr[1]], cargs=[])
qc.append(RGate(4.591350839465064,1.2679876620814976), qargs=[qr[5]], cargs=[])
qc.append(CZGate(), qargs=[qr[4], qr[10]], cargs=[])
qc.append(U3Gate(4.438175883374682,5.014778227242978,0.395105964485411), qargs=[qr[9]], cargs=[])
qc.append(IGate(), qargs=[qr[10]], cargs=[])
qc.append(CRXGate(2.8176864996575204), qargs=[qr[3], qr[4]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(IGate(), qargs=[qr[4]], cargs=[])
qc.append(SGate(), qargs=[qr[9]], cargs=[])
qc.append(CRXGate(6.06720431582227), qargs=[qr[0], qr[8]], cargs=[])
qc.append(U2Gate(3.8396484521920486,5.389605086705323), qargs=[qr[0]], cargs=[])
qc.append(CYGate(), qargs=[qr[0], qr[9]], cargs=[])
qc.append(CRXGate(0.6410834959357722), qargs=[qr[1], qr[2]], cargs=[])
qc.append(CRXGate(3.152773209785367), qargs=[qr[5], qr[2]], cargs=[])
qc.append(CSGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[0], qr[8], qr[6], qr[4]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[3], qr[6]], cargs=[])
qc.append(CRYGate(3.8184925395522673), qargs=[qr[7], qr[1]], cargs=[])
qc.append(RZXGate(5.0844543693921445), qargs=[qr[9], qr[0]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[4], qr[3], qr[2]], cargs=[])
qc.append(U2Gate(0.5232088988285076,1.5882644602699434), qargs=[qr[7]], cargs=[])
qc.append(CCZGate(), qargs=[qr[5], qr[2], qr[6]], cargs=[])
qc.append(IGate(), qargs=[qr[10]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[6], qr[10]], cargs=[])

# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1, coupling_map=None)

# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_ab59878383fc4156b5150c5c856312ec = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_ab59878383fc4156b5150c5c856312ec, shots=7838).result().get_counts(qc)
RESULT = counts