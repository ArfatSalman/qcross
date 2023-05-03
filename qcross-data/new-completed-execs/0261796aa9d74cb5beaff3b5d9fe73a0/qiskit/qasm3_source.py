# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(CSwapGate(), qargs=[qr[0], qr[9], qr[7]], cargs=[])
qc.append(PhaseGate(3.343442682560371), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[3]], cargs=[])
qc.append(HGate(), qargs=[qr[5]], cargs=[])
qc.append(CRZGate(3.2858177251722944), qargs=[qr[9], qr[7]], cargs=[])
qc.append(RVGate(1.6270903792852736, 1.0744526495059412, 3.7558505518080576), qargs=[qr[3]], cargs=[])
qc.append(HGate(), qargs=[qr[0]], cargs=[])
qc.append(U2Gate(0.5159858283914562, 3.092014702746218), qargs=[qr[6]], cargs=[])
qc.append(RVGate(5.944576757265284, 5.021353132730173, 4.714404259070525), qargs=[qr[0]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[0], qr[1], qr[7], qr[2]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CU3Gate(0.6044097350971822, 4.888657590196426, 2.507112428772863), qargs=[qr[9], qr[5]], cargs=[])
subcircuit.append(RZXGate(0.4541176237749392), qargs=[qr[5], qr[3]], cargs=[])
subcircuit.append(CSwapGate(), qargs=[qr[1], qr[9], qr[4]], cargs=[])
subcircuit.append(RVGate(2.6258763463210713, 6.086094132835261, 0.057422744634472736), qargs=[qr[2]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(ZGate(), qargs=[qr[9]], cargs=[])
qc.append(CRXGate(1.0327406277155489), qargs=[qr[4], qr[6]], cargs=[])
qc.append(CRZGate(3.051239290740801), qargs=[qr[1], qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[5], qr[4]], cargs=[])
qc.append(RYGate(5.127275071501011), qargs=[qr[8]], cargs=[])
qc.append(IGate(), qargs=[qr[5]], cargs=[])
qc.append(CSXGate(), qargs=[qr[3], qr[7]], cargs=[])
qc.append(CRZGate(1.6690058311460272), qargs=[qr[7], qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(1.620800307377981), qargs=[qr[1], qr[5]], cargs=[])
qc.append(CU1Gate(0.4967177059820002), qargs=[qr[0], qr[7]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=None)
# SECTION
# NAME: QASM_CONVERSION

from qiskit.qasm3 import loads, dumps
qc = loads(dumps(qc))

# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_fb08e5767f044c8a90a44eefc9e111de = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_fb08e5767f044c8a90a44eefc9e111de, shots=5542).result().get_counts(qc)
RESULT = counts
