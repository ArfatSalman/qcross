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


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(DCXGate(), qargs=[qr[1], qr[6]], cargs=[])
subcircuit.append(CUGate(4.229610589867865,2.696266694818697,5.631160518436971,2.9151388486514547), qargs=[qr[0], qr[6]], cargs=[])
subcircuit.append(ECRGate(), qargs=[qr[3], qr[0]], cargs=[])
subcircuit.append(U2Gate(5.887184334931191,0.07157463504881167), qargs=[qr[6]], cargs=[])
subcircuit.append(CU3Gate(5.1829934776392745,2.7315239782495464,3.9984051265341463), qargs=[qr[2], qr[0]], cargs=[])
subcircuit.append(SXGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(CRZGate(2.008796895454228), qargs=[qr[0], qr[5]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CRXGate(5.987304452123941), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CRZGate(1.0296448789776642), qargs=[qr[1], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[7], qr[6], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(1.740253089260498), qargs=[qr[6], qr[7]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_c427c706518744e59e4347406af19c2e = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_c427c706518744e59e4347406af19c2e, shots=2771).result().get_counts(qc)
RESULT = counts
