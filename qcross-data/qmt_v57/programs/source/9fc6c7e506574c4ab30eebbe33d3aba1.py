
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
qc.append(XGate(), qargs=[qr[3]], cargs=[])
qc.append(CRYGate(2.4498821250483043), qargs=[qr[10], qr[9]], cargs=[])
qc.append(HGate(), qargs=[qr[1]], cargs=[])
qc.append(HGate(), qargs=[qr[2]], cargs=[])
qc.append(CPhaseGate(3.3516599839543195), qargs=[qr[4], qr[3]], cargs=[])
qc.append(ECRGate(), qargs=[qr[5], qr[8]], cargs=[])
qc.append(CU3Gate(5.423661738344168,1.2257558063112008,4.146906161622092), qargs=[qr[1], qr[8]], cargs=[])
qc.append(RXXGate(0.4988271119481185), qargs=[qr[7], qr[0]], cargs=[])

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
backend_b680b5720a554baeb0bf35fe02b097a3 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_b680b5720a554baeb0bf35fe02b097a3, shots=7838).result().get_counts(qc)
RESULT = counts