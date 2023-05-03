
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
qc.append(CYGate(), qargs=[qr[9], qr[3]], cargs=[])
qc.append(CRXGate(3.006996712679364), qargs=[qr[0], qr[9]], cargs=[])
qc.append(RXXGate(6.231728094077643), qargs=[qr[0], qr[1]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(CUGate(5.402681630107685,5.7320803489582755,1.5504227913558584,6.117533666092848), qargs=[qr[1], qr[4]], cargs=[])
qc.append(CZGate(), qargs=[qr[0], qr[8]], cargs=[])
qc.append(C3XGate(), qargs=[qr[7], qr[5], qr[0], qr[1]], cargs=[])
qc.append(CYGate(), qargs=[qr[6], qr[9]], cargs=[])
qc.append(CUGate(1.9776456095905999,2.7856733477756688,2.3725791317893616,4.281289624237246), qargs=[qr[4], qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[5], qr[3], qr[8], qr[2]], cargs=[])
qc.append(SGate(), qargs=[qr[4]], cargs=[])
qc.append(DCXGate(), qargs=[qr[6], qr[1]], cargs=[])
qc.append(RXGate(2.7622901582617536), qargs=[qr[2]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[7], qr[0], qr[4]], cargs=[])
qc.append(UGate(5.093998211740766,4.1763972388782795,1.3446658688471513), qargs=[qr[1]], cargs=[])
qc.append(CYGate(), qargs=[qr[5], qr[6]], cargs=[])
qc.append(UGate(3.2780013517483826,1.092359559443437,2.5802478164404428), qargs=[qr[0]], cargs=[])
qc.append(CUGate(5.627192099540417,2.1947268632429866,5.888372357253659,1.16349884234323), qargs=[qr[3], qr[4]], cargs=[])
qc.append(CYGate(), qargs=[qr[0], qr[5]], cargs=[])
qc.append(SdgGate(), qargs=[qr[7]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[4], qr[0], qr[1]], cargs=[])

# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1, coupling_map=None)

# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_41d70c1fc88242818fd4e4f19328dbc1 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_41d70c1fc88242818fd4e4f19328dbc1, shots=5542).result().get_counts(qc)
RESULT = counts