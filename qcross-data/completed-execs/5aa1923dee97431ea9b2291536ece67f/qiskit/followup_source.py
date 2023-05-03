# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(11, name='qr')
cr = ClassicalRegister(11, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[6], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(CCXGate(), qargs=[qr[5], qr[9], qr[7]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[7]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[10], qr[6], qr[8]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[0]], cargs=[])
qc.append(CCXGate(), qargs=[qr[7], qr[10], qr[2]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CYGate(), qargs=[qr[9], qr[0]], cargs=[])
subcircuit.append(SXGate(), qargs=[qr[3]], cargs=[])
subcircuit.append(XGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(RCCXGate(), qargs=[qr[8], qr[10], qr[6]], cargs=[])
subcircuit.append(CUGate(5.0063780207098425,3.1562533916051736,4.940217775579305,2.419481683937988), qargs=[qr[2], qr[1]], cargs=[])
subcircuit.append(CSwapGate(), qargs=[qr[10], qr[0], qr[7]], cargs=[])
subcircuit.append(PhaseGate(5.5146057452272546), qargs=[qr[0]], cargs=[])
subcircuit.append(ECRGate(), qargs=[qr[3], qr[0]], cargs=[])
subcircuit.append(PhaseGate(0.4827903095199283), qargs=[qr[0]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(SdgGate(), qargs=[qr[7]], cargs=[])
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
backend_9e1a0230a7074a90be502d725373d32d = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_9e1a0230a7074a90be502d725373d32d, shots=7838).result().get_counts(qc)
RESULT = counts
