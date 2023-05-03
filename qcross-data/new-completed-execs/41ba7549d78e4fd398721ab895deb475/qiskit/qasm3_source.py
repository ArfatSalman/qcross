# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(3, name='qr')
cr = ClassicalRegister(3, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(PhaseGate(5.010091518352677), qargs=[qr[2]], cargs=[])
subcircuit.append(CSwapGate(), qargs=[qr[1], qr[2], qr[0]], cargs=[])
subcircuit.append(CSwapGate(), qargs=[qr[0], qr[2], qr[1]], cargs=[])
subcircuit.append(RGate(0.2790475427948373, 2.0520628548884505), qargs=[qr[2]], cargs=[])
subcircuit.append(RXGate(3.7527661762502977), qargs=[qr[2]], cargs=[])
subcircuit.append(SXdgGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(ZGate(), qargs=[qr[2]], cargs=[])
subcircuit.append(RZZGate(5.975361677668773), qargs=[qr[1], qr[2]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(iSwapGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(RZZGate(2.061149362743449), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CZGate(), qargs=[qr[2], qr[1]], cargs=[])
qc.append(CZGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(TGate(), qargs=[qr[2]], cargs=[])
qc.append(IGate(), qargs=[qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(YGate(), qargs=[qr[1]], cargs=[])
qc.append(CCZGate(), qargs=[qr[2], qr[1], qr[0]], cargs=[])
qc.append(CSwapGate(), qargs=[qr[2], qr[1], qr[0]], cargs=[])
qc.append(IGate(), qargs=[qr[1]], cargs=[])
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
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_10fbd0a61ba148b4864caff27922c2b9 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_10fbd0a61ba148b4864caff27922c2b9, shots=489).result().get_counts(qc)
RESULT = counts
