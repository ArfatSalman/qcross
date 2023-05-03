
# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter

# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(6, name='qr')
cr = ClassicalRegister(6, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RXXGate(2.061982306423713), qargs=[qr[0], qr[2]], cargs=[])
qc.append(RVGate(1.8242043393661458,4.419776500558505,0.43416461978491694), qargs=[qr[2]], cargs=[])
qc.append(PhaseGate(3.565985138018942), qargs=[qr[4]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(RXXGate(0.020795531533047435), qargs=[qr[1], qr[0]], cargs=[])

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
backend_4ee926a61bb64c599cab9507d39ca0b0 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_4ee926a61bb64c599cab9507d39ca0b0, shots=1385).result().get_counts(qc)
RESULT = counts