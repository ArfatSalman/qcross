# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(7, name='qr')
cr = ClassicalRegister(7, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[4]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(TdgGate(), qargs=[qr[6]], cargs=[])
subcircuit.append(XGate(), qargs=[qr[4]], cargs=[])
subcircuit.append(ZGate(), qargs=[qr[5]], cargs=[])
subcircuit.append(TGate(), qargs=[qr[2]], cargs=[])
subcircuit.append(CZGate(), qargs=[qr[1], qr[4]], cargs=[])
subcircuit.append(CU3Gate(1.2827690425732097,1.3283826543858017,3.672121211148789), qargs=[qr[2], qr[6]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[3]], cargs=[])
qc.append(CRXGate(2.0099472182748075), qargs=[qr[2], qr[5]], cargs=[])
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
backend_e12f4db44b46459f911b3ea9bbed0ad8 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_e12f4db44b46459f911b3ea9bbed0ad8, shots=1959).result().get_counts(qc)
RESULT = counts
