# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_19ddc6 = Parameter('p_19ddc6')
p_9f1870 = Parameter('p_9f1870')
p_1f65b5 = Parameter('p_1f65b5')
p_e2c839 = Parameter('p_e2c839')
p_93e32f = Parameter('p_93e32f')
p_f0d0cc = Parameter('p_f0d0cc')
p_a85314 = Parameter('p_a85314')
p_87ae80 = Parameter('p_87ae80')
p_3d24b7 = Parameter('p_3d24b7')
p_1083ec = Parameter('p_1083ec')
p_05e304 = Parameter('p_05e304')
p_d719e6 = Parameter('p_d719e6')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(3, name='qr')
cr = ClassicalRegister(3, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(U3Gate(p_1f65b5, p_9f1870, 5.921099882361809), qargs=[qr[2]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(YGate(), qargs=[qr[1]], cargs=[])
qc.append(CU3Gate(3.5951128532694563, p_87ae80, 3.645329450090628), qargs=[qr[0], qr[2]], cargs=[])
qc.append(IGate(), qargs=[qr[1]], cargs=[])
qc.append(U2Gate(2.2781042293610834, p_19ddc6), qargs=[qr[1]], cargs=[])
qc.append(IGate(), qargs=[qr[0]], cargs=[])
qc.append(CRYGate(p_1083ec), qargs=[qr[1], qr[2]], cargs=[])
qc.append(U2Gate(5.5431459174826, 1.3400715972886643), qargs=[qr[0]], cargs=[])
qc.append(TdgGate(), qargs=[qr[1]], cargs=[])
qc.append(U2Gate(p_05e304, 2.4400424648148045), qargs=[qr[1]], cargs=[])
qc.append(YGate(), qargs=[qr[0]], cargs=[])
qc.append(RZZGate(5.7575659278310845), qargs=[qr[0], qr[2]], cargs=[])
qc.append(U1Gate(p_e2c839), qargs=[qr[1]], cargs=[])
qc.append(CUGate(1.0304702852384158, 2.6685497827460365, 3.99549985610294, 5.662035192382266), qargs=[qr[1], qr[2]], cargs=[])
qc.append(CRYGate(p_3d24b7), qargs=[qr[1], qr[2]], cargs=[])
qc.append(CYGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(TdgGate(), qargs=[qr[0]], cargs=[])
qc.append(RYGate(3.7754558724472616), qargs=[qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(U3Gate(p_f0d0cc, p_93e32f, 3.399676447189968), qargs=[qr[0]], cargs=[])
qc.append(RZZGate(0.3954282502495691), qargs=[qr[0], qr[2]], cargs=[])
qc.append(U3Gate(p_a85314, 3.495764555095602, p_d719e6), qargs=[qr[2]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(CU3Gate(3.8725614355577274, 3.7233769818737543, 0.6129863346305541), qargs=[qr[0], qr[1]], cargs=[])
qc.append(U1Gate(2.410525914389015), qargs=[qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(TdgGate(), qargs=[qr[1]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING
from qiskit.qasm3 import dumps
print(dumps(qc))
qc = qc.bind_parameters({p_19ddc6: 2.8111390321344745, p_9f1870: 1.2447972626729948, p_1f65b5: 0.7525107922079248, p_e2c839: 1.4699956697302532, p_93e32f: 2.72714859557862, p_f0d0cc: 6.01948050450523, p_a85314: 1.9629138136015831, p_87ae80: 0.010919193816599988, p_3d24b7: 3.4267977136464998, p_1083ec: 5.388940796049925, p_05e304: 0.15471247054287984, p_d719e6: 4.032386816161946})
# SECTION

print(qc.qasm())
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=['rx', 'ry', 'rz', 'p', 'cx'], optimization_level=2, coupling_map=None)# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_74c1b43af7f34812b61c02d7b7b32e5e = Aer.get_backend('aer_simulator_statevector')
counts = execute(qc, backend=backend_74c1b43af7f34812b61c02d7b7b32e5e, shots=489).result().get_counts(qc)
RESULT = counts
