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
qc.append(CRZGate(4.2641612072511235), qargs=[qr[8], qr[3]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[9], qr[7]], cargs=[])
qc.append(CCXGate(), qargs=[qr[1], qr[2], qr[7]], cargs=[])
qc.append(ZGate(), qargs=[qr[4]], cargs=[])
qc.append(TGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[6]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[9], qr[8]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[9]], cargs=[])
qc.append(SXGate(), qargs=[qr[4]], cargs=[])
qc.append(CSXGate(), qargs=[qr[5], qr[6]], cargs=[])
qc.append(CCXGate(), qargs=[qr[5], qr[2], qr[1]], cargs=[])
# SECTION

# NAME: MEASUREMENT
# Execute the circuit and obtain the unitary matrix
from qiskit import Aer, transpile, execute
result = execute(qc.reverse_bits(), backend=Aer.get_backend('unitary_simulator')).result()
UNITARY = result.get_unitary(qc).data


qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_8d5de13ef8c24e1995dc8df3d25c5c00 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_8d5de13ef8c24e1995dc8df3d25c5c00, shots=5542).result().get_counts(qc)
RESULT = counts
