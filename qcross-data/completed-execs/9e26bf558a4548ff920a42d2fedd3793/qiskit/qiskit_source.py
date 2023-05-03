
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
qc.append(CSXGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(CCXGate(), qargs=[qr[0], qr[1], qr[4]], cargs=[])
qc.append(RYYGate(3.630000846740864), qargs=[qr[4], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[4]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[4], qr[2], qr[1], qr[3]], cargs=[])
qc.append(CU1Gate(2.3801704973111244), qargs=[qr[1], qr[3]], cargs=[])
qc.append(RYYGate(2.26249791419463), qargs=[qr[3], qr[2]], cargs=[])
qc.append(IGate(), qargs=[qr[4]], cargs=[])
qc.append(U2Gate(0.024205049091638117,3.6641337073605276), qargs=[qr[4]], cargs=[])
qc.append(CRYGate(0.5432436418208648), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CPhaseGate(2.5556929743025827), qargs=[qr[0], qr[2]], cargs=[])
qc.append(IGate(), qargs=[qr[3]], cargs=[])
qc.append(CZGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CU1Gate(2.849292498056443), qargs=[qr[3], qr[0]], cargs=[])
qc.append(CSwapGate(), qargs=[qr[0], qr[3], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[4], qr[0]], cargs=[])

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
backend_ab8a26ca5de543a2a04ef3154346c786 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_ab8a26ca5de543a2a04ef3154346c786, shots=979).result().get_counts(qc)
RESULT = counts