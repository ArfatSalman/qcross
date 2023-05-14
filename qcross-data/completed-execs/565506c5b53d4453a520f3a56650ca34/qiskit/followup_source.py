# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(9, name='qr')
cr = ClassicalRegister(9, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[8]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(IGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(CXGate(), qargs=[qr[2], qr[7]], cargs=[])
subcircuit.append(CZGate(), qargs=[qr[5], qr[7]], cargs=[])
subcircuit.append(RC3XGate(), qargs=[qr[0], qr[2], qr[6], qr[8]], cargs=[])
subcircuit.append(CZGate(), qargs=[qr[5], qr[0]], cargs=[])
subcircuit.append(U1Gate(6.2047416485134805), qargs=[qr[0]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CSXGate(), qargs=[qr[2], qr[4]], cargs=[])
qc.append(CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245, 5.987304452123941), qargs=[qr[0], qr[6]], cargs=[])
qc.append(SdgGate(), qargs=[qr[1]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: QASM_CONVERSION

qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=['rx', 'ry', 'rz', 'p', 'cx'],
    optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_c8f8d9c261974c0dab72843a5d7bda4c = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_c8f8d9c261974c0dab72843a5d7bda4c, shots=3919).result().get_counts(qc)
RESULT = counts
