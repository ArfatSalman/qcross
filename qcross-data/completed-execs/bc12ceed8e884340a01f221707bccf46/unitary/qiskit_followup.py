# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CRXGate(2.0099472182748075), qargs=[qr[4], qr[3]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(CRZGate(1.0296448789776642), qargs=[qr[3], qr[4]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[4]], cargs=[])
qc.append(RYYGate(1.6723037552953224), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
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
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0,
    1], [0, 4], [0, 5], [1, 0], [1, 3], [2, 5], [3, 1], [4, 0], [5, 0], [5, 2]]
    )
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_bacd21678ab84cda9d3677679be10d89 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_bacd21678ab84cda9d3677679be10d89, shots=979).result().get_counts(qc)
RESULT = counts
