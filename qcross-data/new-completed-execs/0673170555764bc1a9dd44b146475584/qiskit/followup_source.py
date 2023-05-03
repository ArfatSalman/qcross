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
qc.append(RZZGate(3.138388361681893), qargs=[qr[1], qr[0]], cargs=[])
qc.append(TGate(), qargs=[qr[2]], cargs=[])
qc.append(U1Gate(0.396418175987844), qargs=[qr[9]], cargs=[])
qc.append(CRZGate(5.16452425350899), qargs=[qr[1], qr[4]], cargs=[])
qc.append(CRXGate(3.0664993083734644), qargs=[qr[6], qr[2]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[4], qr[1], qr[8]], cargs=[])
qc.append(CSGate(), qargs=[qr[8], qr[6]], cargs=[])
qc.append(CCZGate(), qargs=[qr[3], qr[7], qr[9]], cargs=[])
qc.append(CU3Gate(2.8185804779007992, 5.261790461945118, 2.326141806696294), qargs=[qr[1], qr[4]], cargs=[])
qc.append(CZGate(), qargs=[qr[3], qr[8]], cargs=[])
qc.append(CSdgGate(), qargs=[qr[3], qr[4]], cargs=[])
qc.append(CUGate(3.522950755972168, 4.8949869688966565, 1.528172084251171, 3.5827113474296604), qargs=[qr[8], qr[5]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[3], qr[5], qr[7]], cargs=[])
qc.append(CSXGate(), qargs=[qr[6], qr[8]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[6], qr[4], qr[7]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CRYGate(0.18861614070395222), qargs=[qr[8], qr[4]], cargs=[])
subcircuit.append(SwapGate(), qargs=[qr[9], qr[2]], cargs=[])
subcircuit.append(CSXGate(), qargs=[qr[3], qr[9]], cargs=[])
subcircuit.append(UGate(2.29898529136329,2.602581019015746,3.608523225163746), qargs=[qr[8]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(RYYGate(4.484588825647207), qargs=[qr[4], qr[5]], cargs=[])
qc.append(U1Gate(6.019643147584277), qargs=[qr[0]], cargs=[])
qc.append(PhaseGate(5.38252061225771), qargs=[qr[7]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: QASM_CONVERSION

qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_0ed90cc123b54fdea02e304c9a083831 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_0ed90cc123b54fdea02e304c9a083831, shots=5542).result().get_counts(qc)
RESULT = counts
