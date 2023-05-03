# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(CYGate(), qargs=[qr[4], qr[0]], cargs=[])
qc.append(RYGate(5.393489737839679), qargs=[qr[0]], cargs=[])
qc.append(CXGate(), qargs=[qr[4], qr[2]], cargs=[])
qc.append(CYGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(RVGate(0.2694018871971584, 3.6610185603230327, 1.6717980794833396), qargs=[qr[0]], cargs=[])
qc.append(CXGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(RYGate(3.6367004709817228), qargs=[qr[0]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(RVGate(2.2068682001004865, 0.10969098183159173, 1.8129273219934456), qargs=[qr[3]], cargs=[])
qc.append(RYGate(2.187038626448052), qargs=[qr[4]], cargs=[])
qc.append(CSGate(), qargs=[qr[3], qr[1]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(CZGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CCXGate(), qargs=[qr[4], qr[1], qr[3]], cargs=[])
qc.append(RZGate(4.342933255918919), qargs=[qr[1]], cargs=[])
qc.append(UGate(5.780988845560674, 1.3228348249163877, 4.617489460561287), qargs=[qr[0]], cargs=[])
qc.append(TGate(), qargs=[qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[1], qr[3]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CCZGate(), qargs=[qr[2], qr[3], qr[0]], cargs=[])
subcircuit.append(RXGate(1.3936743262403044), qargs=[qr[0]], cargs=[])
subcircuit.append(XGate(), qargs=[qr[3]], cargs=[])
subcircuit.append(RZXGate(5.062431030267896), qargs=[qr[3], qr[0]], cargs=[])
subcircuit.append(YGate(), qargs=[qr[4]], cargs=[])
subcircuit.append(CZGate(), qargs=[qr[4], qr[2]], cargs=[])
subcircuit.append(CSXGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(RYYGate(4.555588798234122), qargs=[qr[1], qr[2]], cargs=[])
qc.append(RYYGate(4.914511027415462), qargs=[qr[1], qr[2]], cargs=[])
qc.append(CSGate(), qargs=[qr[4], qr[0]], cargs=[])
qc.append(RZGate(3.3907281434225625), qargs=[qr[4]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[4]], cargs=[])
qc.append(DCXGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[4]], cargs=[])
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
backend_79a36ffbc70844dfbb97b301ffa7be98 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_79a36ffbc70844dfbb97b301ffa7be98, shots=979).result().get_counts(qc)
RESULT = counts
