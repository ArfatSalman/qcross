# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_a7d066 = Parameter('p_a7d066')
p_3e420c = Parameter('p_3e420c')
p_4dde90 = Parameter('p_4dde90')
p_e123c8 = Parameter('p_e123c8')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_a7d066), qargs=[qr[3]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CRXGate(p_e123c8), qargs=[qr[4], qr[3]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(CRZGate(p_3e420c), qargs=[qr[3], qr[4]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[4]], cargs=[])
qc.append(RYYGate(p_4dde90), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[4]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_a7d066: 6.163759533339787, p_3e420c: 1.0296448789776642, p_4dde90: 1.6723037552953224, p_e123c8: 2.0099472182748075})
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1, coupling_map=[[0,
    1], [0, 3], [0, 4], [1, 0], [2, 4], [2, 5], [3, 0], [4, 0], [4, 2], [5, 2]]
    )
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_18ffc99e17dd4748afc312a04fdcbb15 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_18ffc99e17dd4748afc312a04fdcbb15, shots=979).result().get_counts(qc)
RESULT = counts
