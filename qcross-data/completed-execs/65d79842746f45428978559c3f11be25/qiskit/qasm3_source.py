# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_1ee909 = Parameter('p_1ee909')
p_8f01e6 = Parameter('p_8f01e6')
p_c6f972 = Parameter('p_c6f972')
p_924711 = Parameter('p_924711')
p_58a2b5 = Parameter('p_58a2b5')
p_4927d2 = Parameter('p_4927d2')
p_cc3cec = Parameter('p_cc3cec')
p_8e5127 = Parameter('p_8e5127')
p_4616e5 = Parameter('p_4616e5')
p_cc7cb0 = Parameter('p_cc7cb0')
p_1adccb = Parameter('p_1adccb')
p_683702 = Parameter('p_683702')
p_ba4e5e = Parameter('p_ba4e5e')
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(6, name='qr')
cr = ClassicalRegister(6, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_1ee909), qargs=[qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[4]], cargs=[])
qc.append(CRZGate(p_1adccb), qargs=[qr[5], qr[3]], cargs=[])
qc.append(CUGate(p_4616e5, p_924711, p_c6f972, p_ba4e5e), qargs=[qr[5], qr[
    4]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[3], qr[0], qr[5]], cargs=[])
qc.append(CCXGate(), qargs=[qr[1], qr[2], qr[0]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[3], qr[4], qr[2], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[5]], cargs=[])
qc.append(TGate(), qargs=[qr[3]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[2], qr[4], qr[3]], cargs=[])
qc.append(SGate(), qargs=[qr[2]], cargs=[])
qc.append(CRZGate(p_8e5127), qargs=[qr[1], qr[2]], cargs=[])
qc.append(RZGate(p_cc3cec), qargs=[qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[5], qr[1], qr[4]], cargs=[])
qc.append(CU1Gate(p_cc7cb0), qargs=[qr[4], qr[0]], cargs=[])
qc.append(UGate(p_8f01e6, p_4927d2, p_683702), qargs=[qr[2]], cargs=[])
qc.append(RZZGate(p_58a2b5), qargs=[qr[0], qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_1ee909: 6.163759533339787, p_8f01e6: 5.887184334931191, p_c6f972: 2.3864521352475245, p_924711: 5.897054719225356, p_58a2b5: 5.1829934776392745, p_4927d2: 0.07157463504881167, p_cc3cec: 4.229610589867865, p_8e5127: 4.167661441102218, p_4616e5: 0.5112149185250571, p_cc7cb0: 3.2142159669963557, p_1adccb: 4.2641612072511235, p_683702: 1.4112277317699358, p_ba4e5e: 5.987304452123941})
# SECTION
# NAME: QASM_CONVERSION


from qiskit.qasm3 import loads, dumps
qc = loads(dumps(qc))

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_6fb978c685504e31b87025bedf6a5aff = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_6fb978c685504e31b87025bedf6a5aff, shots=1385).result().get_counts(qc)
RESULT = counts
