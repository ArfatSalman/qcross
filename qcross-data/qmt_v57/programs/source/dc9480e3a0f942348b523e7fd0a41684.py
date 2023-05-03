
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
qc.append(TGate(), qargs=[qr[9]], cargs=[])
qc.append(CRYGate(1.852579362704606), qargs=[qr[4], qr[7]], cargs=[])
qc.append(CYGate(), qargs=[qr[9], qr[0]], cargs=[])
qc.append(RXGate(5.276411432143827), qargs=[qr[1]], cargs=[])
qc.append(TGate(), qargs=[qr[1]], cargs=[])
qc.append(U1Gate(2.825051590836995), qargs=[qr[1]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[8], qr[9], qr[1], qr[5]], cargs=[])
qc.append(RYYGate(0.7867209387701732), qargs=[qr[7], qr[9]], cargs=[])
qc.append(UGate(4.576754367736335,5.4109147050480955,1.7256413064705036), qargs=[qr[7]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[3], qr[5], qr[1], qr[4]], cargs=[])
qc.append(RVGate(5.6896213477612445,6.047339853997451,5.623943529608011), qargs=[qr[7]], cargs=[])
qc.append(UGate(3.0132549867885063,6.182661801638049,5.885160602032744), qargs=[qr[7]], cargs=[])
qc.append(HGate(), qargs=[qr[4]], cargs=[])
qc.append(RVGate(4.1249177878170915,6.0745761147209345,2.4099754200724317), qargs=[qr[0]], cargs=[])
qc.append(CYGate(), qargs=[qr[10], qr[2]], cargs=[])
qc.append(HGate(), qargs=[qr[8]], cargs=[])
qc.append(UGate(2.169150328031207,1.7114617170345237,2.307521863987498), qargs=[qr[2]], cargs=[])
qc.append(UGate(5.430643357287303,0.6530454683497888,3.836596788250059), qargs=[qr[10]], cargs=[])
qc.append(RZXGate(5.431264813579931), qargs=[qr[1], qr[3]], cargs=[])
qc.append(CUGate(2.9821700362780588,1.3852421816440175,4.785976176026314,1.3657070275541772), qargs=[qr[4], qr[2]], cargs=[])
qc.append(SGate(), qargs=[qr[5]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[9], qr[3], qr[6]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[10], qr[8], qr[9], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RVGate(5.050073208732572,2.867190134610833,1.0118283033144115), qargs=[qr[2]], cargs=[])
qc.append(RXXGate(1.2634039528117698), qargs=[qr[1], qr[6]], cargs=[])
qc.append(RVGate(0.5734726823505982,3.854641723491838,1.0422555828622841), qargs=[qr[7]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[9], qr[10], qr[2], qr[8]], cargs=[])

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
backend_457b2e62e8964c05abebfa6668c68c47 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_457b2e62e8964c05abebfa6668c68c47, shots=7838).result().get_counts(qc)
RESULT = counts