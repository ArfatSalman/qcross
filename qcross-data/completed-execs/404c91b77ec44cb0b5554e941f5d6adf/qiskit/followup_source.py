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
subcircuit.append(TGate(), qargs=[qr[2]], cargs=[])
subcircuit.append(CZGate(), qargs=[qr[1], qr[0]], cargs=[])
subcircuit.append(CU3Gate(1.2827690425732097,1.3283826543858017,3.672121211148789), qargs=[qr[2], qr[5]], cargs=[])
subcircuit.append(CZGate(), qargs=[qr[0], qr[1]], cargs=[])
subcircuit.append(U1Gate(6.2047416485134805), qargs=[qr[0]], cargs=[])
subcircuit.append(ECRGate(), qargs=[qr[3], qr[0]], cargs=[])
subcircuit.append(U2Gate(5.887184334931191,0.07157463504881167), qargs=[qr[6]], cargs=[])
subcircuit.append(CU3Gate(5.1829934776392745,2.7315239782495464,3.9984051265341463), qargs=[qr[2], qr[0]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CRXGate(5.987304452123941), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CRZGate(1.0296448789776642), qargs=[qr[1], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[7], qr[6], qr[3]], cargs=[])
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
backend_3bc57416d8fc44f98ba8358c998ef2b2 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_3bc57416d8fc44f98ba8358c998ef2b2, shots=2771).result().get_counts(qc)
RESULT = counts
