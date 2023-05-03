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
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CU3Gate(6.086884486572108, 3.06538533241841, 1.7532443887147882), qargs=[qr[2], qr[0]], cargs=[])
subcircuit.append(U3Gate(5.01836135520768, 5.190931186022931, 1.2128092629174942), qargs=[qr[1]], cargs=[])
subcircuit.append(CYGate(), qargs=[qr[0], qr[1]], cargs=[])
subcircuit.append(RYGate(6.1292830756636185), qargs=[qr[2]], cargs=[])
subcircuit.append(CPhaseGate(4.167661441102218), qargs=[qr[2], qr[1]], cargs=[])
subcircuit.append(IGate(), qargs=[qr[0]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(iSwapGate(), qargs=[qr[2], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(SGate(), qargs=[qr[2]], cargs=[])
qc.append(SdgGate(), qargs=[qr[1]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[0], qr[2]], cargs=[])
qc.append(SGate(), qargs=[qr[2]], cargs=[])
qc.append(CCXGate(), qargs=[qr[1], qr[0], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=['ccx', 'h'], optimization_level=2, coupling_map=[[0, 1], [0, 3], [1, 0], [2, 3], [3, 0], [3, 2]])
# SECTION
# NAME: EXECUTION
from qiskit import Aer, transpile, execute
backend_784ef40797a9445bb17c2dbf4c80293c = Aer.get_backend(
    'aer_simulator_matrix_product_state')
counts = execute(qc, backend=backend_784ef40797a9445bb17c2dbf4c80293c,
    shots=489).result().get_counts(qc)
RESULT = counts
