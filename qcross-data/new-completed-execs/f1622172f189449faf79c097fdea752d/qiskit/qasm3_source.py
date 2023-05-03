# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(6, name='qr')
cr = ClassicalRegister(6, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(CSGate(), qargs=[qr[5], qr[0]], cargs=[])
qc.append(SXGate(), qargs=[qr[5]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[4]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[5], qr[0], qr[4], qr[2]], cargs=[])
qc.append(RZGate(4.9678427199825475), qargs=[qr[2]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CSGate(), qargs=[qr[0], qr[2]], cargs=[])
subcircuit.append(XGate(), qargs=[qr[1]], cargs=[])
subcircuit.append(UGate(0.21975397537203006, 2.6790197391768045, 5.406299174556028), qargs=[qr[3]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CXGate(), qargs=[qr[3], qr[1]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[4], qr[2], qr[0], qr[5]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1, coupling_map=None)
# SECTION
# NAME: QASM_CONVERSION

from qiskit.qasm3 import loads, dumps
qc = loads(dumps(qc))

# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_a566b13e842a4b9994925a924b6d6663 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_a566b13e842a4b9994925a924b6d6663, shots=1385).result().get_counts(qc)
RESULT = counts
