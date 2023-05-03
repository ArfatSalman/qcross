# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[6]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CRZGate(1.0296448789776642), qargs=[qr[7], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[2], qr[6], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[7]], cargs=[])
# SECTION

# NAME: MEASUREMENT
# Execute the circuit and obtain the unitary matrix
from qiskit import Aer, transpile, execute
result = execute(qc.reverse_bits(), backend=Aer.get_backend('unitary_simulator')).result()
UNITARY = result.get_unitary(qc).data


qc.measure(qr, cr)
# SECTION
# NAME: QASM_CONVERSION

qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [1, 0], [1, 4], [1, 7], [1, 8], [2, 9], [3, 7], [4, 1], [4, 6], [4, 9], [5, 7], [6, 4], [7, 1], [7, 3], [7, 5], [8, 1], [9, 2], [9, 4]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_b20a7d52a53f4fb5856415fb6d560611 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_b20a7d52a53f4fb5856415fb6d560611, shots=2771).result().get_counts(qc)
RESULT = counts
