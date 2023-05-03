
# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter

# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(3, name='qr')
cr = ClassicalRegister(3, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(CPhaseGate(1.7910282654595102), qargs=[qr[1], qr[2]], cargs=[])
qc.append(U1Gate(5.072633818750175), qargs=[qr[2]], cargs=[])
qc.append(UGate(3.8090985869250003,1.2201500361327853,4.276690396183425), qargs=[qr[2]], cargs=[])
qc.append(PhaseGate(2.482034489972267), qargs=[qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[0]], cargs=[])

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
backend_a08aa04906704b39985f20fd74bced81 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_a08aa04906704b39985f20fd74bced81, shots=489).result().get_counts(qc)
RESULT = counts