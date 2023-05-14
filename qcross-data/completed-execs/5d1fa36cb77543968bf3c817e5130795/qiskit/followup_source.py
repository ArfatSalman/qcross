# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_bba60a = Parameter('p_bba60a')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(7, name='qr')
cr = ClassicalRegister(7, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(RYYGate(0.9356897707598831), qargs=[qr[4], qr[1]], cargs=[])
subcircuit.append(TdgGate(), qargs=[qr[6]], cargs=[])
subcircuit.append(HGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(RZZGate(5.017245588344839), qargs=[qr[0], qr[5]], cargs=[])
subcircuit.append(CRZGate(2.008796895454228), qargs=[qr[0], qr[5]], cargs=[])
subcircuit.append(CSXGate(), qargs=[qr[4], qr[0]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(RZGate(p_bba60a), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[3]], cargs=[])
qc.append(CRXGate(2.0099472182748075), qargs=[qr[2], qr[5]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[6], qr[0], qr[1], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[4], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[2], qr[1], qr[5]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(ECRGate(), qargs=[qr[6], qr[3]], cargs=[])
qc.append(SdgGate(), qargs=[qr[6]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[2], qr[5], qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[1]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_bba60a: 6.163759533339787})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 7], [1, 0], [1, 6], [2, 3], [3, 2], [3, 5], [4, 6], [5, 3], [5, 6], [6, 1], [6, 4], [6, 5], [7, 0]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_af59ca7941eb48eaa0f13bc12178a458 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_af59ca7941eb48eaa0f13bc12178a458, shots=1959).result().get_counts(qc)
RESULT = counts
