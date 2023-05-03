# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_72af2c = Parameter('p_72af2c')
p_5ed9e5 = Parameter('p_5ed9e5')
p_d7cead = Parameter('p_d7cead')
p_6a555a = Parameter('p_6a555a')
p_86b1e1 = Parameter('p_86b1e1')
p_02e598 = Parameter('p_02e598')
p_c6dce3 = Parameter('p_c6dce3')
p_7d8767 = Parameter('p_7d8767')
p_6849dc = Parameter('p_6849dc')
p_84dd61 = Parameter('p_84dd61')
p_7fd6f3 = Parameter('p_7fd6f3')
p_1a3b94 = Parameter('p_1a3b94')
p_2d35e2 = Parameter('p_2d35e2')
p_ba2c5d = Parameter('p_ba2c5d')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(6, name='qr')
cr = ClassicalRegister(6, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_6a555a), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_7fd6f3), qargs=[qr[2], qr[4]], cargs=[])
qc.append(CUGate(p_c6dce3, p_6849dc, p_d7cead, p_7d8767), qargs=[qr[2], qr[3]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[4], qr[0], qr[2]], cargs=[])
qc.append(CCXGate(), qargs=[qr[1], qr[5], qr[0]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[4], qr[3], qr[5], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[5], qr[3], qr[4]], cargs=[])
qc.append(SGate(), qargs=[qr[5]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[1], qr[5]], cargs=[])
qc.append(RZGate(p_2d35e2), qargs=[qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[2], qr[1], qr[3]], cargs=[])
qc.append(CU1Gate(p_02e598), qargs=[qr[3], qr[0]], cargs=[])
qc.append(UGate(p_ba2c5d, p_86b1e1, p_72af2c), qargs=[qr[5]], cargs=[])
qc.append(RZZGate(p_1a3b94), qargs=[qr[0], qr[5]], cargs=[])
qc.append(SGate(), qargs=[qr[4]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[4]], cargs=[])
qc.append(CRZGate(p_5ed9e5), qargs=[qr[0], qr[5]], cargs=[])
qc.append(CU1Gate(p_84dd61), qargs=[qr[1], qr[4]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_72af2c: 1.4112277317699358, p_5ed9e5: 4.833923139882297, p_d7cead: 2.3864521352475245, p_6a555a: 6.163759533339787, p_86b1e1: 0.07157463504881167, p_02e598: 3.2142159669963557, p_c6dce3: 0.5112149185250571, p_7d8767: 5.987304452123941, p_6849dc: 5.897054719225356, p_84dd61: 4.028174522740928, p_7fd6f3: 4.2641612072511235, p_1a3b94: 5.1829934776392745, p_2d35e2: 4.229610589867865, p_ba2c5d: 5.887184334931191})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: QASM_CONVERSION

from qiskit.qasm3 import loads, dumps
qc = loads(dumps(qc))

# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_fa09748c74954be5b3df70d16334bf74 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_fa09748c74954be5b3df70d16334bf74, shots=1385).result().get_counts(qc)
RESULT = counts
