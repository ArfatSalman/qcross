# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_57577b = Parameter('p_57577b')
p_68346f = Parameter('p_68346f')
p_92d853 = Parameter('p_92d853')
p_8852a5 = Parameter('p_8852a5')
p_86d3c5 = Parameter('p_86d3c5')
p_877ff6 = Parameter('p_877ff6')
p_a29d5d = Parameter('p_a29d5d')
p_03605d = Parameter('p_03605d')
p_f61ac5 = Parameter('p_f61ac5')
p_9d2b67 = Parameter('p_9d2b67')
p_a10a46 = Parameter('p_a10a46')
p_aa393d = Parameter('p_aa393d')
p_17cd9d = Parameter('p_17cd9d')
p_8a5847 = Parameter('p_8a5847')
p_ec60d4 = Parameter('p_ec60d4')
p_4c3455 = Parameter('p_4c3455')
p_0783a3 = Parameter('p_0783a3')
p_655fcc = Parameter('p_655fcc')
p_169d88 = Parameter('p_169d88')
p_6773c4 = Parameter('p_6773c4')
p_b5202c = Parameter('p_b5202c')
p_fa03ad = Parameter('p_fa03ad')
p_823d76 = Parameter('p_823d76')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(7, name='qr')
cr = ClassicalRegister(7, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RYYGate(p_86d3c5), qargs=[qr[0], qr[5]], cargs=[])
qc.append(PhaseGate(p_03605d), qargs=[qr[6]], cargs=[])
qc.append(RYGate(p_a29d5d), qargs=[qr[2]], cargs=[])
qc.append(CU1Gate(p_823d76), qargs=[qr[4], qr[1]], cargs=[])
qc.append(CCXGate(), qargs=[qr[4], qr[3], qr[2]], cargs=[])
qc.append(ECRGate(), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CSwapGate(), qargs=[qr[0], qr[6], qr[4]], cargs=[])
qc.append(ECRGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(SwapGate(), qargs=[qr[3], qr[5]], cargs=[])
qc.append(CSwapGate(), qargs=[qr[3], qr[6], qr[1]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[6], qr[1], qr[4], qr[0]], cargs=[])
qc.append(HGate(), qargs=[qr[2]], cargs=[])
qc.append(UGate(p_68346f, p_fa03ad, p_92d853), qargs=[qr[2]], cargs=[])
qc.append(U2Gate(p_8852a5, p_4c3455), qargs=[qr[4]], cargs=[])
qc.append(CSGate(), qargs=[qr[2], qr[5]], cargs=[])
qc.append(U2Gate(p_0783a3, p_169d88), qargs=[qr[6]], cargs=[])
qc.append(RYYGate(p_6773c4), qargs=[qr[1], qr[5]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[3], qr[1], qr[4], qr[5]], cargs=[])
qc.append(UGate(p_aa393d, p_8a5847, p_655fcc), qargs=[qr[3]], cargs=[])
qc.append(CUGate(p_877ff6, p_ec60d4, p_f61ac5, p_b5202c), qargs=[qr[3], qr[5]], cargs=[])
qc.append(U2Gate(p_17cd9d, p_a10a46), qargs=[qr[6]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[1], qr[3], qr[2], qr[0]], cargs=[])
qc.append(RXGate(p_57577b), qargs=[qr[0]], cargs=[])
qc.append(CRYGate(p_9d2b67), qargs=[qr[6], qr[1]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_9287f2 = QuantumRegister(4, name='qr_9287f2')
qc.add_register(qr_9287f2)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_57577b: 5.129266867572668, p_68346f: 5.066050249739578, p_92d853: 2.5510590709018732, p_8852a5: 4.9702527118009066, p_86d3c5: 1.7892872835005398, p_877ff6: 5.814210499839879, p_a29d5d: 3.6138974545836176, p_03605d: 3.7964394792576885, p_f61ac5: 5.986977817617511, p_9d2b67: 2.998268232293747, p_a10a46: 2.4524844691285543, p_aa393d: 0.8822742453157227, p_17cd9d: 4.95448520957096, p_8a5847: 3.4849606070943584, p_ec60d4: 2.2396990253899713, p_4c3455: 3.5114983819004046, p_0783a3: 1.6924855892819173, p_655fcc: 4.713462039096519, p_169d88: 6.035455549292343, p_6773c4: 3.0928548495797905, p_b5202c: 6.091448724065051, p_fa03ad: 3.676251393433825, p_823d76: 4.877167017151953})
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=['cx', 'h', 's', 't'], optimization_level=1, coupling_map=None)# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_f942a370704e467aa681067f28978a83 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_f942a370704e467aa681067f28978a83, shots=1959).result().get_counts(qc)
RESULT = counts
