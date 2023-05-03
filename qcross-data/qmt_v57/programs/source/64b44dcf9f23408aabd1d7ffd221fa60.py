
# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter

# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(2, name='qr')
cr = ClassicalRegister(2, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(CRXGate(5.6533845632228195), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[1]], cargs=[])
qc.append(HGate(), qargs=[qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(PhaseGate(5.448773253310194), qargs=[qr[0]], cargs=[])
qc.append(HGate(), qargs=[qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CUGate(3.552828105055253,0.050781784962543756,5.809409378945297,5.875176200898725), qargs=[qr[1], qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(CSGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CRXGate(5.603552185188765), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CRZGate(0.9830641371913814), qargs=[qr[1], qr[0]], cargs=[])
qc.append(SXGate(), qargs=[qr[1]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(HGate(), qargs=[qr[1]], cargs=[])
qc.append(U2Gate(4.034105773017666,2.8882178453404466), qargs=[qr[0]], cargs=[])
qc.append(DCXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(RYGate(1.6125032339192695), qargs=[qr[0]], cargs=[])
qc.append(CU3Gate(5.655320258226846,4.3812370749870055,5.652256083574008), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(SwapGate(), qargs=[qr[0], qr[1]], cargs=[])

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
backend_a162af2e775e4a94a19b0c50b50a245a = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_a162af2e775e4a94a19b0c50b50a245a, shots=346).result().get_counts(qc)
RESULT = counts