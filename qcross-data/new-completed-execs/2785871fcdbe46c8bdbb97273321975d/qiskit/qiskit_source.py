
# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter

# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(SGate(), qargs=[qr[3]], cargs=[])
qc.append(CSdgGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(RXGate(5.16336000498251), qargs=[qr[2]], cargs=[])
qc.append(SGate(), qargs=[qr[3]], cargs=[])
qc.append(CRXGate(3.8747797547682863), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(SwapGate(), qargs=[qr[3], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(CSdgGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(DCXGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(CPhaseGate(1.6310047821220433), qargs=[qr[3], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])

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
backend_231057da500e42c5ad60bce1fb79c55b = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_231057da500e42c5ad60bce1fb79c55b, shots=979).result().get_counts(qc)
RESULT = counts