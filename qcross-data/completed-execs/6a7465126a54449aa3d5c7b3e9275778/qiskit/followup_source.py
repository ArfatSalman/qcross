# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[1]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[6], qr[1]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[2], qr[8]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(U3Gate(5.007412428963378, 4.658325508156331, 
    3.8184561666262637), qargs=[qr[6]], cargs=[])
subcircuit.append(CRXGate(4.736752714049485), qargs=[qr[7], qr[5]], cargs=[])
subcircuit.append(TGate(), qargs=[qr[2]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CCXGate(), qargs=[qr[4], qr[7], qr[8]], cargs=[])
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
backend_b6b2e22325b14d07a22744cbc2e3829f = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_b6b2e22325b14d07a22744cbc2e3829f, shots=5542).result().get_counts(qc)
RESULT = counts
