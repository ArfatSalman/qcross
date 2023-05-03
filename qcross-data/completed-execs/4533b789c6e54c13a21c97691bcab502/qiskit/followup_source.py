# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(2, name='qr')
cr = ClassicalRegister(2, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZZGate(6.163759533339787), qargs=[qr[0], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(XGate(), qargs=[qr[1]], cargs=[])
subcircuit.append(CHGate(), qargs=[qr[0], qr[1]], cargs=[])
subcircuit.append(SXdgGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(CPhaseGate(1.7280044377928914), qargs=[qr[0], qr[1]],
    cargs=[])
subcircuit.append(RXXGate(0.5112149185250571), qargs=[qr[0], qr[1]], cargs=[])
subcircuit.append(SGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(UGate(5.987304452123941, 1.847916451195972, 
    4.094867647151279), qargs=[qr[1]], cargs=[])
subcircuit.append(YGate(), qargs=[qr[1]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(ECRGate(), qargs=[qr[0], qr[1]], cargs=[])
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
backend_f0d58cc8603e430e9fef80ac132c1e1f = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_f0d58cc8603e430e9fef80ac132c1e1f, shots=346).result().get_counts(qc)
RESULT = counts
