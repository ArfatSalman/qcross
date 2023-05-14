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
qc.append(RZGate(6.163759533339787), qargs=[qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(U3Gate(2.6397681660693015, 5.320621737498446, 
    3.427505621225153), qargs=[qr[2]], cargs=[])
subcircuit.append(RYYGate(6.033961191253911), qargs=[qr[0], qr[2]], cargs=[])
subcircuit.append(CU3Gate(6.086884486572108, 3.06538533241841, 
    1.7532443887147882), qargs=[qr[0], qr[1]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(iSwapGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(SdgGate(), qargs=[qr[2]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[1], qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [1, 0], [1, 2], [2, 1]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_b5456f3c87244c32941878a373538c89 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_b5456f3c87244c32941878a373538c89, shots=489).result().get_counts(qc)
RESULT = counts
