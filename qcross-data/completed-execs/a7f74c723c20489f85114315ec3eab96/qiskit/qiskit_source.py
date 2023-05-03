
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
qc.append(CXGate(), qargs=[qr[3], qr[1]], cargs=[])
qc.append(ECRGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(HGate(), qargs=[qr[0]], cargs=[])
qc.append(CUGate(1.304613255698255,3.4040230460574685,6.192826337087571,0.1235604738481236), qargs=[qr[2], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])

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
backend_c9e75dc814ef4bde8c77aeafa9845889 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_c9e75dc814ef4bde8c77aeafa9845889, shots=692).result().get_counts(qc)
RESULT = counts