# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(4, name='qr')
cr = ClassicalRegister(4, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(CYGate(), qargs=[qr[1], qr[3]], cargs=[])
qc.append(CSdgGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(U2Gate(6.224224267022873, 0.5062108542599196), qargs=[qr[0]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(RXXGate(2.849709666292305), qargs=[qr[2], qr[0]], cargs=[])
qc.append(CUGate(1.4830756139727388, 4.336270484416077, 4.496803337305518, 0.23255854856360128), qargs=[qr[2], qr[0]], cargs=[])
qc.append(U1Gate(3.989772590171974), qargs=[qr[2]], cargs=[])
qc.append(RVGate(2.3749233592982653, 1.242766903811508, 5.902936157186667), qargs=[qr[1]], cargs=[])
qc.append(CCXGate(), qargs=[qr[2], qr[1], qr[3]], cargs=[])
qc.append(RGate(5.3389684124335135, 4.983335490773843), qargs=[qr[0]], cargs=[])
qc.append(CU3Gate(2.9985355066762964, 4.6584355985305175, 5.286009370798176), qargs=[qr[1], qr[2]], cargs=[])
qc.append(U1Gate(1.23766565597922), qargs=[qr[1]], cargs=[])
qc.append(CRYGate(0.7050339438266124), qargs=[qr[3], qr[0]], cargs=[])
qc.append(CU3Gate(0.26880077817102677, 4.703772321262758, 2.2003352220865064), qargs=[qr[0], qr[3]], cargs=[])
qc.append(RXXGate(1.7988659594922651), qargs=[qr[1], qr[3]], cargs=[])
qc.append(CZGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(U1Gate(3.091046473463947), qargs=[qr[2]], cargs=[])
qc.append(CU3Gate(4.07826629550777, 0.6948315212195522, 3.971785158778898), qargs=[qr[1], qr[0]], cargs=[])
qc.append(RZGate(6.114994939448648), qargs=[qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[3], qr[1], qr[0], qr[2]], cargs=[])
qc.append(U1Gate(3.885678856232139), qargs=[qr[1]], cargs=[])
qc.append(U3Gate(1.3122881955531616, 0.33578911439943154, 4.332701855049643), qargs=[qr[1]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(CSwapGate(), qargs=[qr[3], qr[0], qr[1]], cargs=[])
qc.append(CZGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(U3Gate(0.07989271098060978, 3.2475433527931767, 3.3028156122014454), qargs=[qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=['rx', 'ry', 'rz', 'p', 'cx'], optimization_level=3, coupling_map=None)# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_ef673dd3cdab4645a44ab80170dbc2ed = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_ef673dd3cdab4645a44ab80170dbc2ed, shots=692).result().get_counts(qc)
RESULT = counts
