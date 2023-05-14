# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_01ce9b = Parameter('p_01ce9b')
p_4f7ff2 = Parameter('p_4f7ff2')
p_17defe = Parameter('p_17defe')
p_e7ae71 = Parameter('p_e7ae71')
p_17befe = Parameter('p_17befe')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(6, name='qr')
cr = ClassicalRegister(6, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_4f7ff2), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_17defe), qargs=[qr[2], qr[4]], cargs=[])
qc.append(CUGate(p_e7ae71, p_17befe, 2.3864521352475245, p_01ce9b), qargs=[qr[2], qr[3]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[4], qr[0], qr[2]], cargs=[])
qc.append(CCXGate(), qargs=[qr[1], qr[5], qr[0]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[4], qr[3], qr[5], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(U1Gate(6.2047416485134805), qargs=[qr[0]], cargs=[])
subcircuit.append(CPhaseGate(4.63837786161633), qargs=[qr[0], qr[2]], cargs=[])
subcircuit.append(RZXGate(4.563562108824195), qargs=[qr[4], qr[0]], cargs=[])
subcircuit.append(C3XGate(5.94477504571567), qargs=[qr[4], qr[5], qr[2], qr[1]], cargs=[])
subcircuit.append(XGate(), qargs=[qr[4]], cargs=[])
subcircuit.append(CYGate(), qargs=[qr[2], qr[0]], cargs=[])
subcircuit.append(SXGate(), qargs=[qr[0]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_01ce9b: 5.987304452123941, p_4f7ff2: 6.163759533339787, p_17defe: 4.2641612072511235, p_e7ae71: 0.5112149185250571, p_17befe: 5.897054719225356})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 5], [2, 0], [3, 0], [4, 0], [4, 6], [5, 1], [6, 4]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_de1d66c5fcb34297a5e9ef8cab75e78d = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_de1d66c5fcb34297a5e9ef8cab75e78d, shots=1385).result().get_counts(qc)
RESULT = counts
