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
qc.append(RZGate(6.163759533339787), qargs=[qr[5]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[4]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245,
    5.987304452123941), qargs=[qr[7], qr[1]], cargs=[])
qc.append(SdgGate(), qargs=[qr[3]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[7], qr[5], qr[2], qr[8]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_ed5edb = QuantumRegister(7, name='qr_ed5edb')
qc.add_register(qr_ed5edb)
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
backend_34c12d0540e04aad98211e8f918d678f = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_34c12d0540e04aad98211e8f918d678f, shots=3919).result().get_counts(qc)
RESULT = counts
