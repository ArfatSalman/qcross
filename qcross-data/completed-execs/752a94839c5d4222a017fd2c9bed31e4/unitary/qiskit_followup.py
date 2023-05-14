# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(4, name='qr')
cr = ClassicalRegister(4, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(IGate(), qargs=[qr[1]], cargs=[])
subcircuit.append(RYYGate(2.3864521352475245), qargs=[qr[0], qr[3]], cargs=[])
subcircuit.append(RXGate(3.8629766967365606), qargs=[qr[0]], cargs=[])
subcircuit.append(U1Gate(2.6397681660693015), qargs=[qr[3]], cargs=[])
subcircuit.append(YGate(), qargs=[qr[1]], cargs=[])
subcircuit.append(RXXGate(6.033961191253911), qargs=[qr[1], qr[3]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(RZGate(6.163759533339787), qargs=[qr[1]], cargs=[])
qc.append(RZZGate(4.066449154047175), qargs=[qr[2], qr[3]], cargs=[])
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
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [1, 0], [1, 2], [2, 1], [2, 3], [2, 4], [3, 2], [4, 2]])
# SECTION
# NAME: QASM_CONVERSION

qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_8f52ffbc2b7d46be9970c4a57966b98f = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_8f52ffbc2b7d46be9970c4a57966b98f, shots=692).result().get_counts(qc)
RESULT = counts
