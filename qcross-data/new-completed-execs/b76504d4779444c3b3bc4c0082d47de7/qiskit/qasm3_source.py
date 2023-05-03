# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(6, name='qr')
cr = ClassicalRegister(6, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RXGate(0.6650027350645848), qargs=[qr[5]], cargs=[])
qc.append(SdgGate(), qargs=[qr[0]], cargs=[])
qc.append(CYGate(), qargs=[qr[0], qr[4]], cargs=[])
qc.append(RVGate(4.207878413680952, 0.3009231473653096, 1.580343691421699), qargs=[qr[4]], cargs=[])
qc.append(CPhaseGate(3.9206722628490542), qargs=[qr[5], qr[2]], cargs=[])
qc.append(CPhaseGate(3.397598873029434), qargs=[qr[2], qr[3]], cargs=[])
qc.append(IGate(), qargs=[qr[4]], cargs=[])
qc.append(U2Gate(4.855299131904333, 3.1272609413923482), qargs=[qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(RXXGate(0.7249247820191558), qargs=[qr[3], qr[4]], cargs=[])
qc.append(TdgGate(), qargs=[qr[5]], cargs=[])
qc.append(IGate(), qargs=[qr[1]], cargs=[])
qc.append(CXGate(), qargs=[qr[4], qr[1]], cargs=[])
qc.append(IGate(), qargs=[qr[5]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[5], qr[2], qr[4], qr[3]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[5], qr[2], qr[4], qr[0]], cargs=[])
qc.append(RXXGate(2.6498953828086473), qargs=[qr[2], qr[4]], cargs=[])
qc.append(CYGate(), qargs=[qr[5], qr[2]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(HGate(), qargs=[qr[4]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(SwapGate(), qargs=[qr[1], qr[0]], cargs=[])
subcircuit.append(CYGate(), qargs=[qr[0], qr[5]], cargs=[])
subcircuit.append(CCZGate(), qargs=[qr[4], qr[3], qr[5]], cargs=[])
subcircuit.append(DCXGate(), qargs=[qr[0], qr[2]], cargs=[])
subcircuit.append(RXGate(5.981830878165426), qargs=[qr[2]], cargs=[])
subcircuit.append(U3Gate(2.693422775984842, 0.5067499290735414, 2.096989391777038), qargs=[qr[5]], cargs=[])
subcircuit.append(SwapGate(), qargs=[qr[0], qr[3]], cargs=[])
subcircuit.append(CU3Gate(2.0053149876729552, 5.072178584377088, 2.2962625668816754), qargs=[qr[1], qr[3]], cargs=[])
subcircuit.append(RXXGate(4.1874527696058825), qargs=[qr[0], qr[4]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(SdgGate(), qargs=[qr[3]], cargs=[])
qc.append(ECRGate(), qargs=[qr[0], qr[5]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
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
backend_8bd842256c2a4550bcc42fdd1a98cf5f = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_8bd842256c2a4550bcc42fdd1a98cf5f, shots=1385).result().get_counts(qc)
RESULT = counts
