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
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[6], qr[3]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[1], qr[7]], cargs=[])
qc.append(CCXGate(), qargs=[qr[5], qr[9], qr[7]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(TGate(), qargs=[qr[1]], cargs=[])
subcircuit.append(U1Gate(6.171674001528992), qargs=[qr[7]], cargs=[])
subcircuit.append(UGate(3.5173414605326783, 2.3568871696687452, 6.011900464835247), qargs=[qr[8]], cargs=[])
subcircuit.append(CU3Gate(5.1829934776392745, 2.7315239782495464, 3.9984051265341463), qargs=[qr[2], qr[4]], cargs=[])
subcircuit.append(SXGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(CRZGate(2.008796895454228), qargs=[qr[0], qr[5]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=['rx', 'ry', 'rz', 'p', 'cx'],
    optimization_level=2, coupling_map=[[0, 1], [0, 2], [0, 5], [0, 6], [0,
    10], [1, 0], [1, 3], [1, 9], [2, 0], [3, 1], [4, 5], [4, 6], [5, 0], [5,
    4], [5, 11], [6, 0], [6, 4], [6, 8], [7, 9], [8, 6], [9, 1], [9, 7], [
    10, 0], [11, 5]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_2987871ee0324e2f8e6da8fd99d93efa = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_2987871ee0324e2f8e6da8fd99d93efa, shots=5542).result().get_counts(qc)
RESULT = counts
