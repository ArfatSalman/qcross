# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(3, name='qr')
cr = ClassicalRegister(3, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[1]], cargs=[])
qc.append(CHGate(), qargs=[qr[2], qr[0]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(UGate(4.2641612072511235,0.3737454361709458,1.8624239758032093), qargs=[qr[2]], cargs=[])
subcircuit.append(CRZGate(5.897054719225356), qargs=[qr[1], qr[2]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[2], qr[1]], cargs=[])
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
backend_4aa43aa6a7744840b74f1266cd2a4949 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_4aa43aa6a7744840b74f1266cd2a4949, shots=489).result().get_counts(qc)
RESULT = counts
