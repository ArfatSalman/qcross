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
qc.append(XGate(), qargs=[qr[2]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CU1Gate(6.086884486572108), qargs=[qr[3], qr[0]], cargs=[])
subcircuit.append(TdgGate(), qargs=[qr[2]], cargs=[])
subcircuit.append(U1Gate(5.01836135520768), qargs=[qr[1]], cargs=[])
subcircuit.append(CRYGate(4.736752714049485), qargs=[qr[0], qr[3]], cargs=[])
subcircuit.append(RXGate(6.1292830756636185), qargs=[qr[2]], cargs=[])
subcircuit.append(CHGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245, 5.987304452123941), qargs=[qr[0], qr[2]], cargs=[])
qc.append(CU1Gate(5.154187354656876), qargs=[qr[3], qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[3], qr[0], qr[1], qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: QASM_CONVERSION

qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_3a2a2e4ee9ac4c38b14aec55b900affc = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_3a2a2e4ee9ac4c38b14aec55b900affc, shots=692).result().get_counts(qc)
RESULT = counts
