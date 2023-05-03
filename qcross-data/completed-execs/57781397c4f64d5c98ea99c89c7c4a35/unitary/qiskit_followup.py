# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(7, name='qr')
cr = ClassicalRegister(7, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(CRXGate(2.0099472182748075), qargs=[qr[3], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[5], qr[4], qr[3]], cargs=[])
qc.append(CHGate(), qargs=[qr[2], qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[5], qr[3], qr[4], qr[6]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(ECRGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(SdgGate(), qargs=[qr[1]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[3], qr[6], qr[5]], cargs=[])
qc.append(SGate(), qargs=[qr[4]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[4]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[5], qr[3], qr[4], qr[0]], cargs=[])
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
backend_7a95f9e25bcd4dc4a6dbb5b7e287daf0 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_7a95f9e25bcd4dc4a6dbb5b7e287daf0, shots=1959).result().get_counts(qc)
RESULT = counts
