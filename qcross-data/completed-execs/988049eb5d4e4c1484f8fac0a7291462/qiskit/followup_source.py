# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_384a3b = Parameter('p_384a3b')
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(6, name='qr')
cr = ClassicalRegister(6, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[1]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[2], qr[1]], cargs=[])
qc.append(CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245,
    5.987304452123941), qargs=[qr[2], qr[0]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[5], qr[1], qr[4], qr[2]], cargs=[])
qc.append(CCXGate(), qargs=[qr[5], qr[3], qr[4]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[0], qr[3], qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[1]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[3], qr[0], qr[1]], cargs=[])
qc.append(SGate(), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[5], qr[3]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[5]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(RC3XGate(), qargs=[qr[3], qr[1], qr[4], qr[5]], cargs=[])
subcircuit.append(RXXGate(1.1349349609188835), qargs=[qr[5], qr[2]], cargs=[])
subcircuit.append(RYYGate(0.6724371252296606), qargs=[qr[4], qr[3]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(C3SXGate(), qargs=[qr[4], qr[2], qr[5], qr[0]], cargs=[])
qc.append(CU1Gate(3.2142159669963557), qargs=[qr[0], qr[4]], cargs=[])
qc.append(UGate(p_384a3b, 0.07157463504881167, 1.4112277317699358), qargs=[
    qr[3]], cargs=[])
qc.append(RZZGate(5.1829934776392745), qargs=[qr[4], qr[3]], cargs=[])
qc.append(SGate(), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(CRZGate(4.833923139882297), qargs=[qr[4], qr[3]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_384a3b: 5.887184334931191})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_8e16338cb11c4ba3b410e43a3822017d = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_8e16338cb11c4ba3b410e43a3822017d, shots=1385).result().get_counts(qc)
RESULT = counts
