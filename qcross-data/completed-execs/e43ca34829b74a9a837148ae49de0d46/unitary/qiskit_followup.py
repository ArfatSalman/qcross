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
# SECTION
# NAME: USELESS_ENTITIES

qr_698c1b = QuantumRegister(5, name='qr_698c1b')
qc.add_register(qr_698c1b)
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
backend_f5dbab87f5f942e891b9e407fc025d9f = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_f5dbab87f5f942e891b9e407fc025d9f, shots=346).result().get_counts(qc)
RESULT = counts
