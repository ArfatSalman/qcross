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
qc.append(RZGate(6.163759533339787), qargs=[qr[1]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[4]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[1], qr[4]], cargs=[])
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
backend_978f34d57a7940c1baf292f56ee9d71d = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_978f34d57a7940c1baf292f56ee9d71d, shots=979).result().get_counts(qc)
RESULT = counts
