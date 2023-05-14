# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_faecf5 = Parameter('p_faecf5')
p_428d4a = Parameter('p_428d4a')
p_5976d3 = Parameter('p_5976d3')
p_91ad47 = Parameter('p_91ad47')
p_1fff0a = Parameter('p_1fff0a')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(6, name='qr')
cr = ClassicalRegister(6, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[2], qr[4]], cargs=[])
qc.append(CUGate(p_faecf5, 5.897054719225356, p_5976d3, p_91ad47), qargs=[qr[2], qr[3]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[4], qr[0], qr[2]], cargs=[])
qc.append(CCXGate(), qargs=[qr[1], qr[5], qr[0]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[4], qr[3], qr[5], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[5], qr[3], qr[4]], cargs=[])
qc.append(SGate(), qargs=[qr[5]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[1], qr[5]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[2], qr[1], qr[3]], cargs=[])
qc.append(CU1Gate(3.2142159669963557), qargs=[qr[3], qr[0]], cargs=[])
qc.append(UGate(5.887184334931191, 0.07157463504881167, p_1fff0a), qargs=[qr[5]], cargs=[])
qc.append(RZZGate(5.1829934776392745), qargs=[qr[0], qr[5]], cargs=[])
qc.append(SGate(), qargs=[qr[4]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[4]], cargs=[])
qc.append(CRZGate(p_428d4a), qargs=[qr[0], qr[5]], cargs=[])
qc.append(CU1Gate(4.028174522740928), qargs=[qr[1], qr[4]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_faecf5: 0.5112149185250571, p_428d4a: 4.833923139882297, p_5976d3: 2.3864521352475245, p_91ad47: 5.987304452123941, p_1fff0a: 1.4112277317699358})
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1, coupling_map=[[0,
    1], [1, 0], [1, 3], [1, 4], [2, 3], [3, 1], [3, 2], [4, 1], [4, 5], [5, 4]]
    )
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_b03e09faa59546048fdfba17eee9cfee = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_b03e09faa59546048fdfba17eee9cfee, shots=1385).result().get_counts(qc)
RESULT = counts
