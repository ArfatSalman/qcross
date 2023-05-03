
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
qc.append(U3Gate(0.7525107922079248,1.2447972626729948,5.921099882361809), qargs=[qr[2]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(YGate(), qargs=[qr[1]], cargs=[])
qc.append(CU3Gate(3.5951128532694563,0.010919193816599988,3.645329450090628), qargs=[qr[0], qr[2]], cargs=[])
qc.append(IGate(), qargs=[qr[1]], cargs=[])
qc.append(U2Gate(2.2781042293610834,2.8111390321344745), qargs=[qr[1]], cargs=[])
qc.append(IGate(), qargs=[qr[0]], cargs=[])
qc.append(CRYGate(5.388940796049925), qargs=[qr[1], qr[2]], cargs=[])
qc.append(U2Gate(5.5431459174826,1.3400715972886643), qargs=[qr[0]], cargs=[])
qc.append(TdgGate(), qargs=[qr[1]], cargs=[])
qc.append(U2Gate(0.15471247054287984,2.4400424648148045), qargs=[qr[1]], cargs=[])
qc.append(YGate(), qargs=[qr[0]], cargs=[])
qc.append(RZZGate(5.7575659278310845), qargs=[qr[0], qr[2]], cargs=[])
qc.append(U1Gate(1.4699956697302532), qargs=[qr[1]], cargs=[])
qc.append(CUGate(1.0304702852384158,2.6685497827460365,3.99549985610294,5.662035192382266), qargs=[qr[1], qr[2]], cargs=[])
qc.append(CRYGate(3.4267977136464998), qargs=[qr[1], qr[2]], cargs=[])
qc.append(CYGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(TdgGate(), qargs=[qr[0]], cargs=[])
qc.append(RYGate(3.7754558724472616), qargs=[qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(U3Gate(6.01948050450523,2.72714859557862,3.399676447189968), qargs=[qr[0]], cargs=[])
qc.append(RZZGate(0.3954282502495691), qargs=[qr[0], qr[2]], cargs=[])
qc.append(U3Gate(1.9629138136015831,3.495764555095602,4.032386816161946), qargs=[qr[2]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(CU3Gate(3.8725614355577274,3.7233769818737543,0.6129863346305541), qargs=[qr[0], qr[1]], cargs=[])
qc.append(U1Gate(2.410525914389015), qargs=[qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(TdgGate(), qargs=[qr[1]], cargs=[])

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
backend_74c1b43af7f34812b61c02d7b7b32e5e = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_74c1b43af7f34812b61c02d7b7b32e5e, shots=489).result().get_counts(qc)
RESULT = counts