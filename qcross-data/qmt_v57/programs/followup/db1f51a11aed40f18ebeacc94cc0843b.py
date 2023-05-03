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
qc.append(CSGate(), qargs=[qr[1], qr[3]], cargs=[])
qc.append(CU1Gate(2.7516388630934165), qargs=[qr[2], qr[0]], cargs=[])
qc.append(CPhaseGate(4.526280604536298), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CRYGate(2.8957147333760322), qargs=[qr[4], qr[2]], cargs=[])
qc.append(ECRGate(), qargs=[qr[1], qr[3]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[0], qr[5]], cargs=[])
qc.append(RYGate(5.218542100413873), qargs=[qr[0]], cargs=[])
qc.append(CYGate(), qargs=[qr[4], qr[0]], cargs=[])
qc.append(CUGate(4.0589886937440705, 5.489841527329702, 5.349444809703235, 0.0076492699425670645), qargs=[qr[3], qr[5]], cargs=[])
qc.append(CCXGate(), qargs=[qr[1], qr[5], qr[3]], cargs=[])
qc.append(CCXGate(), qargs=[qr[1], qr[4], qr[0]], cargs=[])
qc.append(SdgGate(), qargs=[qr[3]], cargs=[])
qc.append(CCXGate(), qargs=[qr[3], qr[5], qr[4]], cargs=[])
qc.append(CSXGate(), qargs=[qr[4], qr[1]], cargs=[])
qc.append(CRXGate(1.7239239743720898), qargs=[qr[2], qr[0]], cargs=[])
qc.append(CSGate(), qargs=[qr[4], qr[0]], cargs=[])
qc.append(SdgGate(), qargs=[qr[0]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(YGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(RXXGate(5.748731119826895), qargs=[qr[1], qr[4]], cargs=[])
subcircuit.append(XGate(), qargs=[qr[3]], cargs=[])
subcircuit.append(TdgGate(), qargs=[qr[4]], cargs=[])
subcircuit.append(RGate(1.0099433123573884, 3.399529081072497), qargs=[qr[5]], cargs=[])
subcircuit.append(U3Gate(5.953737875506177, 2.168117657673707, 5.952071466550862), qargs=[qr[3]], cargs=[])
subcircuit.append(CU1Gate(4.560443955770688), qargs=[qr[3], qr[1]], cargs=[])
subcircuit.append(CXGate(), qargs=[qr[0], qr[5]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(U1Gate(3.6101582139068564), qargs=[qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=None)
# SECTION
# NAME: QASM_CONVERSION
qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_2cabea3e2ded4f8da25daa1039aea795 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_2cabea3e2ded4f8da25daa1039aea795, shots=1385).result().get_counts(qc)
RESULT = counts
