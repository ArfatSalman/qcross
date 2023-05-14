# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[5]], cargs=[])
qc.append(XGate(), qargs=[qr[5]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[0], qr[5]], cargs=[])
qc.append(CRZGate(1.0296448789776642), qargs=[qr[2], qr[5]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[7], qr[5], qr[3]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CU3Gate(1.2827690425732097, 1.3283826543858017, 
    3.672121211148789), qargs=[qr[1], qr[6]], cargs=[])
subcircuit.append(CZGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
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
backend_5a0f858d749641be9219f3a1c559fedf = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_5a0f858d749641be9219f3a1c559fedf, shots=2771).result().get_counts(qc)
RESULT = counts
