# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(3, name='qr')
cr = ClassicalRegister(3, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(SdgGate(), qargs=[qr[2]], cargs=[])
subcircuit.append(IGate(), qargs=[qr[2]], cargs=[])
subcircuit.append(RCCXGate(), qargs=[qr[0], qr[1], qr[2]], cargs=[])
subcircuit.append(SXGate(), qargs=[qr[2]], cargs=[])
subcircuit.append(CU3Gate(6.086884486572108, 3.06538533241841, 
    1.7532443887147882), qargs=[qr[0], qr[1]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(iSwapGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(SdgGate(), qargs=[qr[2]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[1], qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(CCXGate(), qargs=[qr[2], qr[1], qr[0]], cargs=[])
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
backend_b7b24e026dcf4dfa81f2331cde60bb08 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_b7b24e026dcf4dfa81f2331cde60bb08, shots=489).result().get_counts(qc)
RESULT = counts
