# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter

# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(11, name="qr")
cr = ClassicalRegister(11, name="cr")
qc = QuantumCircuit(qr, cr, name="qc")
qc.append(SwapGate(), qargs=[qr[4], qr[2]], cargs=[])
qc.append(U2Gate(5.355095913145835, 0.5025385094232117), qargs=[qr[1]], cargs=[])
qc.append(SdgGate(), qargs=[qr[5]], cargs=[])
qc.append(CRZGate(2.5299146290041223), qargs=[qr[2], qr[10]], cargs=[])
qc.append(SXGate(), qargs=[qr[9]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[10]], cargs=[])
qc.append(CXGate(), qargs=[qr[3], qr[4]], cargs=[])
qc.append(IGate(), qargs=[qr[7]], cargs=[])
qc.append(DCXGate(), qargs=[qr[5], qr[7]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[7], qr[9], qr[6], qr[8]], cargs=[])
qc.append(CU1Gate(3.4774129386607884), qargs=[qr[8], qr[5]], cargs=[])

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

backend_57dc4610d51041c09029d8c22f124cf5 = Aer.get_backend("qasm_simulator")
counts = (
    execute(qc, backend=backend_57dc4610d51041c09029d8c22f124cf5, shots=7838)
    .result()
    .get_counts(qc)
)
RESULT = counts
