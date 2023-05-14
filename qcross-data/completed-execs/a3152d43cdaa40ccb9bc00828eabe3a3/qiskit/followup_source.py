# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_668799 = Parameter('p_668799')
p_4a9618 = Parameter('p_4a9618')
p_68b975 = Parameter('p_68b975')
p_4dfb76 = Parameter('p_4dfb76')
p_c4dfaf = Parameter('p_c4dfaf')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(6, name='qr')
cr = ClassicalRegister(6, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_c4dfaf), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_68b975), qargs=[qr[2], qr[4]], cargs=[])
qc.append(CUGate(p_4dfb76, p_668799, 2.3864521352475245, p_4a9618), qargs=[qr[2], qr[3]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[4], qr[0], qr[2]], cargs=[])
qc.append(CCXGate(), qargs=[qr[1], qr[5], qr[0]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[4], qr[3], qr[5], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_70c8ce = QuantumRegister(3, name='qr_70c8ce')
qc.add_register(qr_70c8ce)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_668799: 5.897054719225356, p_4a9618: 5.987304452123941, p_68b975: 4.2641612072511235, p_4dfb76: 0.5112149185250571, p_c4dfaf: 6.163759533339787})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_81965e05b619410ea269089e5b2a6e83 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_81965e05b619410ea269089e5b2a6e83, shots=1385).result().get_counts(qc)
RESULT = counts
