
# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter

# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(2, name='qr')
cr = ClassicalRegister(2, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RYYGate(0.040332757463886044), qargs=[qr[1], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(RZXGate(2.0199977459798464), qargs=[qr[0], qr[1]], cargs=[])
qc.append(RXXGate(3.927829733740478), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CYGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CRZGate(5.451741496819523), qargs=[qr[0], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RXXGate(2.6277753952279403), qargs=[qr[0], qr[1]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(CRZGate(3.555542082325973), qargs=[qr[0], qr[1]], cargs=[])
qc.append(RYYGate(5.488061464125162), qargs=[qr[0], qr[1]], cargs=[])
qc.append(RXGate(3.657037356032689), qargs=[qr[0]], cargs=[])
qc.append(RXGate(4.976946713501052), qargs=[qr[1]], cargs=[])
qc.append(ECRGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[1]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(RGate(5.88245539296814,5.313337512106651), qargs=[qr[1]], cargs=[])
qc.append(RXGate(3.1801000664195067), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(2.60217238429383), qargs=[qr[1], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(CYGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[1]], cargs=[])

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
backend_7f8640fa487647fca511dc020a826ee2 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_7f8640fa487647fca511dc020a826ee2, shots=346).result().get_counts(qc)
RESULT = counts