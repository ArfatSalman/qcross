
# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter

# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(9, name='qr')
cr = ClassicalRegister(9, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RYYGate(4.230538610152256), qargs=[qr[3], qr[8]], cargs=[])
qc.append(CRXGate(3.3203084344733997), qargs=[qr[2], qr[3]], cargs=[])
qc.append(CRXGate(4.622916213622228), qargs=[qr[6], qr[8]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[8], qr[2], qr[6], qr[1]], cargs=[])
qc.append(CRZGate(2.3252143484585774), qargs=[qr[4], qr[8]], cargs=[])
qc.append(CU3Gate(3.9779731506025207,1.8692602791557653,3.52092355767973), qargs=[qr[0], qr[7]], cargs=[])
qc.append(CSdgGate(), qargs=[qr[5], qr[7]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[6], qr[1], qr[8], qr[4]], cargs=[])
qc.append(CYGate(), qargs=[qr[8], qr[5]], cargs=[])
qc.append(CU1Gate(6.092983263138358), qargs=[qr[6], qr[8]], cargs=[])
qc.append(DCXGate(), qargs=[qr[2], qr[1]], cargs=[])
qc.append(CRZGate(0.2732434042738512), qargs=[qr[2], qr[8]], cargs=[])
qc.append(YGate(), qargs=[qr[1]], cargs=[])
qc.append(IGate(), qargs=[qr[1]], cargs=[])
qc.append(CYGate(), qargs=[qr[3], qr[4]], cargs=[])
qc.append(CSdgGate(), qargs=[qr[5], qr[2]], cargs=[])
qc.append(CYGate(), qargs=[qr[0], qr[5]], cargs=[])
qc.append(CUGate(1.3294053085361235,1.6134324891544933,1.3668738903035305,2.2614780495462785), qargs=[qr[1], qr[6]], cargs=[])
qc.append(CHGate(), qargs=[qr[6], qr[8]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[1], qr[7], qr[0], qr[8]], cargs=[])
qc.append(RVGate(4.325005000959295,1.4884924689724215,2.122323708296557), qargs=[qr[6]], cargs=[])
qc.append(CUGate(4.129509958864599,2.661313282317246,3.471286270687046,3.3400786207701714), qargs=[qr[2], qr[5]], cargs=[])
qc.append(CUGate(5.55653769076178,4.605056011495016,0.9700427538550028,1.9703735803987805), qargs=[qr[8], qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[3], qr[5], qr[2]], cargs=[])
qc.append(CCZGate(), qargs=[qr[1], qr[5], qr[0]], cargs=[])
qc.append(CSdgGate(), qargs=[qr[3], qr[8]], cargs=[])

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
backend_03d8ad528b3c448eaf5cb952ef1ad651 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_03d8ad528b3c448eaf5cb952ef1ad651, shots=3919).result().get_counts(qc)
RESULT = counts