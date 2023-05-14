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
qc.append(RZGate(6.163759533339787), qargs=[qr[1]], cargs=[])
qc.append(RZZGate(4.066449154047175), qargs=[qr[2], qr[3]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CHGate(), qargs=[qr[0], qr[3]], cargs=[])
subcircuit.append(U1Gate(2.6397681660693015), qargs=[qr[3]], cargs=[])
subcircuit.append(YGate(), qargs=[qr[1]], cargs=[])
subcircuit.append(RXXGate(6.033961191253911), qargs=[qr[1], qr[3]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245, 5.987304452123941), qargs=[qr[0], qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: QASM_CONVERSION

qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_99046d70f2384cb48b43b84f5bad3eed = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_99046d70f2384cb48b43b84f5bad3eed, shots=692).result().get_counts(qc)
RESULT = counts
