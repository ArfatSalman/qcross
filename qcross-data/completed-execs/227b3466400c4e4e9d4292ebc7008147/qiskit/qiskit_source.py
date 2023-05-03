
# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter

# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(2, name='qr')
cr = ClassicalRegister(2, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(TdgGate(), qargs=[qr[0]], cargs=[])
qc.append(PhaseGate(1.3428862289262922), qargs=[qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CU3Gate(4.165123907650545,2.6766240976228306,5.851109164020841), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CZGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(U3Gate(3.1124943003575862,5.033907753688158,3.427635111293556), qargs=[qr[1]], cargs=[])
qc.append(RZZGate(5.9643464495294385), qargs=[qr[0], qr[1]], cargs=[])
qc.append(U1Gate(3.005113685069328), qargs=[qr[0]], cargs=[])
qc.append(HGate(), qargs=[qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(PhaseGate(0.3147213681222795), qargs=[qr[0]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(YGate(), qargs=[qr[1]], cargs=[])
qc.append(CYGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[1]], cargs=[])
qc.append(YGate(), qargs=[qr[0]], cargs=[])
qc.append(U3Gate(0.6932622610946984,0.5005689189307869,3.802023333380939), qargs=[qr[1]], cargs=[])
qc.append(CZGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CYGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(U2Gate(1.5441062376251906,1.6281357791932107), qargs=[qr[0]], cargs=[])
qc.append(CYGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(PhaseGate(3.369665394386499), qargs=[qr[1]], cargs=[])
qc.append(HGate(), qargs=[qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(U1Gate(2.7233411978459645), qargs=[qr[0]], cargs=[])
qc.append(YGate(), qargs=[qr[0]], cargs=[])
qc.append(RXXGate(4.459276651579209), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[1]], cargs=[])

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
backend_75de0846eb99438f940d7bddd35177ea = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_75de0846eb99438f940d7bddd35177ea, shots=346).result().get_counts(qc)
RESULT = counts