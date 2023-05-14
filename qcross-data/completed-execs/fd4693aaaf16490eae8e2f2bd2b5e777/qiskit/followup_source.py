# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(2, name='qr')
cr = ClassicalRegister(2, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZZGate(6.163759533339787), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(ECRGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(1.977559237989846), qargs=[qr[0], qr[1]], cargs=[])
qc.append(TGate(), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[1]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(RZGate(5.870272810031044), qargs=[qr[1]], cargs=[])
subcircuit.append(RXGate(1.350257477660173), qargs=[qr[1]], cargs=[])
subcircuit.append(RXXGate(1.8331092502981063), qargs=[qr[1], qr[0]], cargs=[])
subcircuit.append(CYGate(), qargs=[qr[0], qr[1]], cargs=[])
subcircuit.append(IGate(), qargs=[qr[1]], cargs=[])
subcircuit.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CRXGate(5.987304452123941), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CRZGate(2.2498881927557752), qargs=[qr[0], qr[1]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=['cx', 'h', 's', 't'], optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION
from qiskit import Aer, transpile, execute
backend_a26cf9468b0440359738b3fc85077db2 = Aer.get_backend(
    'aer_simulator_matrix_product_state')
counts = execute(qc, backend=backend_a26cf9468b0440359738b3fc85077db2,
    shots=346).result().get_counts(qc)
RESULT = counts
