# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_59c694 = Parameter('p_59c694')
p_4da120 = Parameter('p_4da120')
p_bfc32f = Parameter('p_bfc32f')
p_080b1a = Parameter('p_080b1a')
p_6db7be = Parameter('p_6db7be')
p_d86b30 = Parameter('p_d86b30')
p_fdfc00 = Parameter('p_fdfc00')
p_63b789 = Parameter('p_63b789')
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(2, name='qr')
cr = ClassicalRegister(2, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZZGate(p_d86b30), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(ECRGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(p_bfc32f), qargs=[qr[0], qr[1]], cargs=[])
qc.append(TGate(), qargs=[qr[1]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(SXGate(), qargs=[qr[1]], cargs=[])
qc.append(CRXGate(p_59c694), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CRZGate(p_63b789), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[1]], cargs=[])
qc.append(RZGate(p_080b1a), qargs=[qr[1]], cargs=[])
qc.append(RZGate(p_fdfc00), qargs=[qr[1]], cargs=[])
qc.append(CU1Gate(p_4da120), qargs=[qr[0], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RZZGate(p_6db7be), qargs=[qr[0], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_59c694: 5.987304452123941, p_4da120: 1.6723037552953224, p_bfc32f: 1.977559237989846, p_080b1a: 5.320621737498446, p_6db7be: 6.086884486572108, p_d86b30: 6.163759533339787, p_fdfc00: 5.512260524440591, p_63b789: 2.2498881927557752})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_988aef23023749119aa36f9018df8a92 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_988aef23023749119aa36f9018df8a92, shots=346).result().get_counts(qc)
RESULT = counts
