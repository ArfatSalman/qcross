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


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CUGate(5.320621737498446,3.427505621225153,5.512260524440591,1.350257477660173), qargs=[qr[3], qr[0]], cargs=[])
subcircuit.append(SwapGate(), qargs=[qr[1], qr[0]], cargs=[])
subcircuit.append(CU1Gate(6.086884486572108), qargs=[qr[3], qr[0]], cargs=[])
subcircuit.append(TdgGate(), qargs=[qr[2]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245, 5.987304452123941), qargs=[qr[0], qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [1, 0], [1, 2], [2, 1], [2, 3], [3, 2]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_d62cfc3d43d34b1db881c577d072c249 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_d62cfc3d43d34b1db881c577d072c249, shots=692).result().get_counts(qc)
RESULT = counts
