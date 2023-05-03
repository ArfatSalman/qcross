
# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter

# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(7, name='qr')
cr = ClassicalRegister(7, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(1.011876271526295), qargs=[qr[1]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CUGate(4.470339697850853,2.3870542496998692,0.050955830933431714,0.06883225750858235), qargs=[qr[0], qr[4]], cargs=[])
qc.append(C3XGate(), qargs=[qr[6], qr[4], qr[5], qr[1]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[4], qr[6], qr[5], qr[2]], cargs=[])
qc.append(SdgGate(), qargs=[qr[5]], cargs=[])
qc.append(CCXGate(), qargs=[qr[0], qr[5], qr[6]], cargs=[])

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
backend_95afa613f7aa4de5a7f05087c116c9f5 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_95afa613f7aa4de5a7f05087c116c9f5, shots=1959).result().get_counts(qc)
RESULT = counts