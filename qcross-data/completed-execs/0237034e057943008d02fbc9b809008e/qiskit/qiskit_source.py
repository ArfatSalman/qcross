
# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter

# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(4, name='qr')
cr = ClassicalRegister(4, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[1]], cargs=[])
qc.append(RZZGate(4.066449154047175), qargs=[qr[2], qr[3]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])

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
backend_e2f4fd5e0d7f4fdd9bd0017fff597ea4 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_e2f4fd5e0d7f4fdd9bd0017fff597ea4, shots=692).result().get_counts(qc)
RESULT = counts