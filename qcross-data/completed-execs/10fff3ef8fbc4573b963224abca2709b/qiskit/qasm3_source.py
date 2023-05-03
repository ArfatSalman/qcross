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
p_c1c477 = Parameter('p_c1c477')
p_4266cb = Parameter('p_4266cb')
p_8c222d = Parameter('p_8c222d')
p_af0e12 = Parameter('p_af0e12')
p_6f466e = Parameter('p_6f466e')
p_ef2512 = Parameter('p_ef2512')
p_961b75 = Parameter('p_961b75')
p_aa5f2d = Parameter('p_aa5f2d')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(6, name='qr')
cr = ClassicalRegister(6, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_961b75), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_af0e12), qargs=[qr[2], qr[4]], cargs=[])
qc.append(CUGate(p_6f466e, 5.897054719225356, p_aa5f2d, 5.987304452123941),
    qargs=[qr[2], qr[3]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[4], qr[0], qr[2]], cargs=[])
qc.append(CCXGate(), qargs=[qr[1], qr[5], qr[0]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[4], qr[3], qr[5], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[5], qr[3], qr[4]], cargs=[])
qc.append(SGate(), qargs=[qr[5]], cargs=[])
qc.append(CRZGate(p_c1c477), qargs=[qr[1], qr[5]], cargs=[])
qc.append(RZGate(p_8c222d), qargs=[qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[2], qr[1], qr[3]], cargs=[])
qc.append(CU1Gate(p_4266cb), qargs=[qr[3], qr[0]], cargs=[])
qc.append(UGate(5.887184334931191, 0.07157463504881167, 1.4112277317699358),
    qargs=[qr[5]], cargs=[])
qc.append(RZZGate(p_ef2512), qargs=[qr[0], qr[5]], cargs=[])
qc.append(SGate(), qargs=[qr[4]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[4]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_c1c477: 4.167661441102218,
    p_4266cb: 3.2142159669963557,
    p_8c222d: 4.229610589867865,
    p_af0e12: 4.2641612072511235,
    p_6f466e: 0.5112149185250571,
    p_ef2512: 5.1829934776392745,
    p_961b75: 6.163759533339787,
    p_aa5f2d: 2.3864521352475245,
})

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
backend_d96df4435c9a42fb906a4663409a3ddd = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_d96df4435c9a42fb906a4663409a3ddd, shots=1385).result().get_counts(qc)
RESULT = counts
