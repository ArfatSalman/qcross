# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr_1 = QuantumRegister(9, name='qr_1')
cr_1 = ClassicalRegister(9, name='cr_1')
qc_1 = QuantumCircuit(qr_1, cr_1, name='qc_1')


qc_1.append(RZGate(6.163759533339787), qargs=[qr_1[1]], cargs=[])
qc_1.append(CRZGate(4.2641612072511235), qargs=[qr_1[3], qr_1[1]], cargs=[])
qc_1.append(CRXGate(5.987304452123941), qargs=[qr_1[0], qr_1[4]], cargs=[])
qc_1.append(CCXGate(), qargs=[qr_1[2], qr_1[5], qr_1[4]], cargs=[])
qc_1.append(ZGate(), qargs=[qr_1[6]], cargs=[])
qc_1.append(TGate(), qargs=[qr_1[5]], cargs=[])
qc_1.append(CRZGate(4.167661441102218), qargs=[qr_1[0], qr_1[3]], cargs=[])


qr_2 = QuantumRegister(1, name='qr_2')
cr_2 = ClassicalRegister(1, name='cr_2')
qc_2 = QuantumCircuit(qr_2, cr_2, name='qc_2')


qc_2.append(XGate(), qargs=[qr_2[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc_1.measure(qr_1, cr_1)
qc_2.measure(qr_2, cr_2)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc_1 = transpile(qc_1, basis_gates=None, optimization_level=2, coupling_map=None)
qc_2 = transpile(qc_2, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: QASM_CONVERSION

qc_1 = QuantumCircuit.from_qasm_str(qc_1.qasm())
qc_2 = QuantumCircuit.from_qasm_str(qc_2.qasm())
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_160f881c0edb47018d932cdc83988e2f = Aer.get_backend('aer_simulator_density_matrix')
counts_1 = execute(qc_1, backend=backend_160f881c0edb47018d932cdc83988e2f, shots=5542).result().get_counts(qc_1)
counts_2 = execute(qc_2, backend=backend_160f881c0edb47018d932cdc83988e2f, shots=5542).result().get_counts(qc_2)
RESULT = [counts_1, counts_2]
