# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(7, name='qr')
cr = ClassicalRegister(7, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(U1Gate(5.479758197394313), qargs=[qr[1]], cargs=[])
qc.append(RGate(6.143639644288786, 3.8563981362966246), qargs=[qr[2]], cargs=[])
qc.append(SwapGate(), qargs=[qr[3], qr[5]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CUGate(1.573398276884453, 2.4750711131608187, 2.608178435015891, 0.020264981462429707), qargs=[qr[3], qr[2]], cargs=[])
subcircuit.append(CCXGate(), qargs=[qr[3], qr[6], qr[2]], cargs=[])
subcircuit.append(CXGate(), qargs=[qr[6], qr[4]], cargs=[])
subcircuit.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CU3Gate(0.22167464109509083, 6.012192432688993, 0.4115095208941581), qargs=[qr[5], qr[1]], cargs=[])
qc.append(CCZGate(), qargs=[qr[1], qr[3], qr[0]], cargs=[])
qc.append(U2Gate(0.9648254328971443, 2.9933536728613173), qargs=[qr[4]], cargs=[])
qc.append(RXXGate(2.032522200125169), qargs=[qr[4], qr[1]], cargs=[])
qc.append(CSGate(), qargs=[qr[3], qr[1]], cargs=[])
qc.append(RGate(4.790279244293115, 5.917497614834585), qargs=[qr[1]], cargs=[])
qc.append(RZZGate(1.6645038233620808), qargs=[qr[4], qr[6]], cargs=[])
qc.append(U1Gate(0.07676574518435057), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[4]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: QASM_CONVERSION

from qiskit.qasm3 import loads, dumps
qc = loads(dumps(qc))

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=3, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_e7bf37c75f494e5d836b0389f0c5700e = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_e7bf37c75f494e5d836b0389f0c5700e, shots=1959).result().get_counts(qc)
RESULT = counts
