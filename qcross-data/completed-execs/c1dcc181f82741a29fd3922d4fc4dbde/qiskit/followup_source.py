# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_752feb = Parameter('p_752feb')
p_2ded38 = Parameter('p_2ded38')
p_5fc981 = Parameter('p_5fc981')
p_636ed6 = Parameter('p_636ed6')
p_c6e6fc = Parameter('p_c6e6fc')
p_8e5ab7 = Parameter('p_8e5ab7')
p_68a976 = Parameter('p_68a976')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(6, name='qr')
cr = ClassicalRegister(6, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_752feb), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[2], qr[4]], cargs=[])
qc.append(CUGate(0.5112149185250571, p_636ed6, p_5fc981, 5.987304452123941), qargs=[qr[2], qr[3]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[4], qr[0], qr[2]], cargs=[])
qc.append(CCXGate(), qargs=[qr[1], qr[5], qr[0]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[4], qr[3], qr[5], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[5], qr[3], qr[4]], cargs=[])
qc.append(SGate(), qargs=[qr[5]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[1], qr[5]], cargs=[])
qc.append(RZGate(p_68a976), qargs=[qr[1]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(RCCXGate(), qargs=[qr[4], qr[5], qr[1]], cargs=[])
subcircuit.append(CRYGate(3.1402006997068588), qargs=[qr[3], qr[0]], cargs=[])
subcircuit.append(SXdgGate(), qargs=[qr[4]], cargs=[])
subcircuit.append(DCXGate(), qargs=[qr[1], qr[2]], cargs=[])
subcircuit.append(RYYGate(0.6724371252296606), qargs=[qr[0], qr[5]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(C3SXGate(), qargs=[qr[0], qr[2], qr[1], qr[3]], cargs=[])
qc.append(CU1Gate(3.2142159669963557), qargs=[qr[3], qr[0]], cargs=[])
qc.append(UGate(p_2ded38, p_8e5ab7, 1.4112277317699358), qargs=[qr[5]], cargs=[])
qc.append(RZZGate(p_c6e6fc), qargs=[qr[0], qr[5]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_752feb: 6.163759533339787, p_2ded38: 5.887184334931191, p_5fc981: 2.3864521352475245, p_636ed6: 5.897054719225356, p_c6e6fc: 5.1829934776392745, p_8e5ab7: 0.07157463504881167, p_68a976: 4.229610589867865})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 2], [1, 0], [1, 6], [2, 0], [2, 3], [2, 4], [3, 2], [4, 2], [4, 5], [4, 7], [5, 4], [6, 1], [7, 4]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_c5a7dff0bb7740c9afa92a2ccb8ae8a9 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_c5a7dff0bb7740c9afa92a2ccb8ae8a9, shots=1385).result().get_counts(qc)
RESULT = counts
