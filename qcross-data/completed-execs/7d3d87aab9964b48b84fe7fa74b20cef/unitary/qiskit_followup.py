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
qc.append(RZGate(6.163759533339787), qargs=[qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[2], qr[1]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(SGate(), qargs=[qr[2]], cargs=[])
qc.append(SdgGate(), qargs=[qr[0]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[1], qr[2]], cargs=[])
qc.append(SGate(), qargs=[qr[2]], cargs=[])
qc.append(CCXGate(), qargs=[qr[0], qr[1], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[2], qr[1]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(RYYGate(1.6723037552953224), qargs=[qr[0], qr[1]], cargs=[])
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
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 2], [1, 0], [2, 0]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_1dd893eab78d437f8aa9f1a4273c96e5 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_1dd893eab78d437f8aa9f1a4273c96e5, shots=489).result().get_counts(qc)
RESULT = counts
