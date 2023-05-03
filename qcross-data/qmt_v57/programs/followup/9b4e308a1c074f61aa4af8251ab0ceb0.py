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
qc.append(U3Gate(0.25389907280649565, 2.779350782980329, 4.0325416129476945), qargs=[qr[6]], cargs=[])
qc.append(HGate(), qargs=[qr[7]], cargs=[])
qc.append(U1Gate(0.3295500658949094), qargs=[qr[9]], cargs=[])
qc.append(U3Gate(3.6652643129524427, 3.6818876186109124, 2.469344104714078), qargs=[qr[7]], cargs=[])
qc.append(XGate(), qargs=[qr[5]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[3], qr[9]], cargs=[])
qc.append(SwapGate(), qargs=[qr[0], qr[7]], cargs=[])
qc.append(DCXGate(), qargs=[qr[4], qr[3]], cargs=[])
qc.append(CXGate(), qargs=[qr[9], qr[2]], cargs=[])
qc.append(CCXGate(), qargs=[qr[1], qr[6], qr[9]], cargs=[])
qc.append(U1Gate(4.379482838154957), qargs=[qr[0]], cargs=[])
qc.append(DCXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[5], qr[0]], cargs=[])
qc.append(PhaseGate(3.0078842093393288), qargs=[qr[0]], cargs=[])
qc.append(DCXGate(), qargs=[qr[4], qr[6]], cargs=[])
qc.append(CRXGate(4.021310180959978), qargs=[qr[2], qr[3]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(RCCXGate(), qargs=[qr[0], qr[9], qr[8]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(RZZGate(1.6685155387019077), qargs=[qr[4], qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1, coupling_map=None)
# SECTION
# NAME: QASM_CONVERSION
qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_2709c13dc6b14305b1bdfa9223065015 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_2709c13dc6b14305b1bdfa9223065015, shots=5542).result().get_counts(qc)
RESULT = counts
