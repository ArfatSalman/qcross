# causes  24860 killed     python interesting/ae3bbf48e2c44b47b7dacd5ce3f1ea86.py

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
qc.append(SdgGate(), qargs=[qr[1]], cargs=[])
qc.append(CXGate(), qargs=[qr[2], qr[4]], cargs=[])
qc.append(C4XGate(), qargs=[qr[9], qr[0], qr[1], qr[5], qr[3]], cargs=[])
qc.append(RXXGate(1.8718085894812062), qargs=[qr[7], qr[0]], cargs=[])
qc.append(RZGate(1.1747090939221867), qargs=[qr[6]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[7], qr[9]], cargs=[])
qc.append(CSXGate(), qargs=[qr[8], qr[9]], cargs=[])
qc.append(RXGate(5.64723807205144), qargs=[qr[7]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[1]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[4]], cargs=[])
qc.append(CU3Gate(2.9846688970319306, 2.3539266945387127, 2.1465216482422327), qargs=[qr[1], qr[5]], cargs=[])
qc.append(RZGate(5.795533948358621), qargs=[qr[2]], cargs=[])
qc.append(C4XGate(), qargs=[qr[9], qr[0], qr[2], qr[1], qr[5]], cargs=[])
qc.append(SdgGate(), qargs=[qr[7]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[8], qr[6], qr[5]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[4]], cargs=[])
qc.append(RZZGate(2.448274041662876), qargs=[qr[4], qr[1]], cargs=[])
qc.append(UGate(2.4953780994927763, 1.1059725815581287, 1.9582393259862767), qargs=[qr[3]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: QASM_CONVERSION
qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_4d49e45fa32e4f45bd00514d21b1a4ff = Aer.get_backend('aer_simulator_density_matrix')
counts = execute(qc, backend=backend_4d49e45fa32e4f45bd00514d21b1a4ff, shots=5542).result().get_counts(qc)
RESULT = counts
