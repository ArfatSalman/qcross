
# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter

# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RC3XGate(), qargs=[qr[9], qr[6], qr[0], qr[2]], cargs=[])
qc.append(PhaseGate(6.09316043121222), qargs=[qr[7]], cargs=[])
qc.append(CHGate(), qargs=[qr[3], qr[9]], cargs=[])
qc.append(XGate(), qargs=[qr[7]], cargs=[])
qc.append(CU1Gate(3.0503162741407537), qargs=[qr[8], qr[6]], cargs=[])
qc.append(SdgGate(), qargs=[qr[3]], cargs=[])
qc.append(U1Gate(5.75020155959207), qargs=[qr[3]], cargs=[])
qc.append(XGate(), qargs=[qr[8]], cargs=[])
qc.append(IGate(), qargs=[qr[6]], cargs=[])
qc.append(RYGate(6.135776937038943), qargs=[qr[5]], cargs=[])
qc.append(RXGate(0.5846665175165219), qargs=[qr[2]], cargs=[])
qc.append(DCXGate(), qargs=[qr[0], qr[5]], cargs=[])
qc.append(RZZGate(5.985328734366836), qargs=[qr[0], qr[8]], cargs=[])
qc.append(CRYGate(2.033688313756901), qargs=[qr[8], qr[7]], cargs=[])
qc.append(SdgGate(), qargs=[qr[6]], cargs=[])

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
backend_5f7702fd9e5d4b158ebaa54a1fbc2ce0 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_5f7702fd9e5d4b158ebaa54a1fbc2ce0, shots=5542).result().get_counts(qc)
RESULT = counts