# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CRXGate(2.0099472182748075), qargs=[qr[4], qr[3]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(TGate(), qargs=[qr[2]], cargs=[])
subcircuit.append(UGate(5.01836135520768,5.190931186022931,1.2128092629174942), qargs=[qr[3]], cargs=[])
subcircuit.append(RC3XGate(), qargs=[qr[4], qr[0], qr[3], qr[1]], cargs=[])
subcircuit.append(DCXGate(), qargs=[qr[2], qr[3]], cargs=[])
subcircuit.append(CZGate(), qargs=[qr[1], qr[0]], cargs=[])
subcircuit.append(CUGate(4.229610589867865,2.696266694818697,5.631160518436971,2.9151388486514547), qargs=[qr[0], qr[1]], cargs=[])
subcircuit.append(CPhaseGate(4.63837786161633), qargs=[qr[0], qr[2]], cargs=[])
subcircuit.append(ECRGate(), qargs=[qr[3], qr[1]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CRZGate(1.0296448789776642), qargs=[qr[3], qr[4]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[4]], cargs=[])
qc.append(RYYGate(1.6723037552953224), qargs=[qr[0], qr[2]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_95bd5e = QuantumRegister(4, name='qr_95bd5e')
qc.add_register(qr_95bd5e)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_4275b153fa444c518cd4f3f64b23532a = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_4275b153fa444c518cd4f3f64b23532a, shots=979).result().get_counts(qc)
RESULT = counts
