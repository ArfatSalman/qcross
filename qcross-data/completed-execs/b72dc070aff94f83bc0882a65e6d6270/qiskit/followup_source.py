# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS
# SECTION
# NAME: PARAMETERS
p_78601e = Parameter('p_78601e')
p_91bcc8 = Parameter('p_91bcc8')
p_0a0a4b = Parameter('p_0a0a4b')
p_0ecc7a = Parameter('p_0ecc7a')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(3, name='qr')
cr = ClassicalRegister(3, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_0ecc7a), qargs=[qr[1]], cargs=[])
qc.append(CHGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[2], qr[1]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(UGate(2.9790366726895714, p_0a0a4b, 3.2287759437031154),
    qargs=[qr[1]], cargs=[])
subcircuit.append(SdgGate(), qargs=[qr[1]], cargs=[])
subcircuit.append(RYYGate(0.2906326206587185), qargs=[qr[2], qr[0]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(SGate(), qargs=[qr[2]], cargs=[])
qc.append(SdgGate(), qargs=[qr[1]], cargs=[])
qc.append(CRXGate(p_91bcc8), qargs=[qr[0], qr[2]], cargs=[])
qc.append(SGate(), qargs=[qr[2]], cargs=[])
qc.append(CCXGate(), qargs=[qr[1], qr[0], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(RYYGate(1.6723037552953224), qargs=[qr[1], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(SGate(), qargs=[qr[2]], cargs=[])
qc.append(ECRGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[1], qr[0], qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(SdgGate(), qargs=[qr[2]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[0], qr[2], qr[1]], cargs=[])
qc.append(CRZGate(p_78601e), qargs=[qr[2], qr[1]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_78601e: 4.167661441102218,
    p_91bcc8: 5.987304452123941,
    p_0a0a4b: 5.974354952564585,
    p_0ecc7a: 6.163759533339787,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_4b8e76487fe3446ba0c7671be8e26a50 = Aer.get_backend('aer_simulator')
counts = execute(qc, backend=backend_4b8e76487fe3446ba0c7671be8e26a50, shots=489).result().get_counts(qc)
RESULT = counts
