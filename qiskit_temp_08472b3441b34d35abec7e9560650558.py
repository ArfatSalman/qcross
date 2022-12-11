
# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter

# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(CUGate(1.4006987211512518,5.87171748222823,1.6118094341214977,3.48470543480054), qargs=[qr[2], qr[3]], cargs=[])
qc.append(CUGate(1.1871631023192395,3.1208310247400375,4.6969093516914615,0.17758444859871442), qargs=[qr[4], qr[2]], cargs=[])
qc.append(CCXGate(), qargs=[qr[0], qr[1], qr[4]], cargs=[])
qc.append(CSwapGate(), qargs=[qr[4], qr[0], qr[3]], cargs=[])
qc.append(RYGate(1.6125723299807893), qargs=[qr[1]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[3], qr[1]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[0], qr[1], qr[2], qr[4]], cargs=[])
qc.append(C3XGate(5.748870687038669), qargs=[qr[1], qr[4], qr[2], qr[0]], cargs=[])
qc.append(TGate(), qargs=[qr[3]], cargs=[])
qc.append(RYGate(5.620914585085149), qargs=[qr[3]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[3]], cargs=[])
qc.append(TGate(), qargs=[qr[1]], cargs=[])

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
backend_38f514bd915e4e2481efcd217cdbf77b = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_38f514bd915e4e2481efcd217cdbf77b, shots=979).result().get_counts(qc)
RESULT = counts
print(RESULT)