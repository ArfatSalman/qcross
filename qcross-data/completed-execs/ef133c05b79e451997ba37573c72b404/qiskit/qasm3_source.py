# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_37851b = Parameter('p_37851b')
p_771172 = Parameter('p_771172')
p_e59639 = Parameter('p_e59639')
p_432785 = Parameter('p_432785')
p_0f1b6d = Parameter('p_0f1b6d')
p_f2cc7e = Parameter('p_f2cc7e')
p_2c778f = Parameter('p_2c778f')
p_0c9124 = Parameter('p_0c9124')
p_a04195 = Parameter('p_a04195')
p_2361ce = Parameter('p_2361ce')
p_3f48eb = Parameter('p_3f48eb')
p_acd647 = Parameter('p_acd647')
p_609841 = Parameter('p_609841')
p_fc560c = Parameter('p_fc560c')
p_1a7816 = Parameter('p_1a7816')
p_981c1e = Parameter('p_981c1e')
p_484055 = Parameter('p_484055')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_3f48eb), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[6]], cargs=[])
qc.append(CRXGate(p_2361ce), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CRZGate(1.0296448789776642), qargs=[qr[1], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[7], qr[6], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(1.740253089260498), qargs=[qr[6], qr[7]], cargs=[])
qc.append(CRZGate(p_771172), qargs=[qr[1], qr[7]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(CU1Gate(3.2142159669963557), qargs=[qr[4], qr[0]], cargs=[])
qc.append(CRXGate(p_0f1b6d), qargs=[qr[6], qr[4]], cargs=[])
qc.append(RZZGate(5.1829934776392745), qargs=[qr[7], qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CUGate(4.722103101046168, 5.3924725338944945, 
    4.88987246261121, p_609841), qargs=[qr[2], qr[0]], cargs=[])
subcircuit.append(CUGate(2.862865991712737, 6.0504088665633065, p_e59639,
    p_0c9124), qargs=[qr[3], qr[6]], cargs=[])
subcircuit.append(RXGate(3.698825211554417), qargs=[qr[3]], cargs=[])
subcircuit.append(CHGate(), qargs=[qr[1], qr[6]], cargs=[])
subcircuit.append(U2Gate(p_a04195, 1.0052392769301404), qargs=[qr[4]], cargs=[]
    )
subcircuit.append(RZGate(3.2374432046466546), qargs=[qr[7]], cargs=[])
subcircuit.append(SXdgGate(), qargs=[qr[7]], cargs=[])
subcircuit.append(CPhaseGate(p_acd647), qargs=[qr[7], qr[6]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(RZGate(p_f2cc7e), qargs=[qr[4]], cargs=[])
qc.append(CRXGate(p_484055), qargs=[qr[0], qr[3]], cargs=[])
qc.append(CUGate(5.03147076606842, p_fc560c, p_1a7816, p_37851b), qargs=[qr
    [6], qr[2]], cargs=[])
qc.append(U2Gate(p_981c1e, p_2c778f), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[6]], cargs=[])
qc.append(SdgGate(), qargs=[qr[0]], cargs=[])
qc.append(RZZGate(p_432785), qargs=[qr[3], qr[4]], cargs=[])
qc.append(TGate(), qargs=[qr[5]], cargs=[])
qc.append(RYYGate(1.9669252191306448), qargs=[qr[4], qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[3], qr[2], qr[5]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[7]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_37851b: 4.940217775579305, p_771172: 4.167661441102218, p_e59639: 1.7203758404994713, p_432785: 3.950837470808744, p_0f1b6d: 5.94477504571567, p_f2cc7e: 3.775592041307464, p_2c778f: 2.1276323672732023, p_0c9124: 2.8704483107274004, p_a04195: 0.25812405723927917,
    p_2361ce: 5.987304452123941,
    p_3f48eb: 6.163759533339787,
    p_acd647: 1.672427069032094,
    p_609841: 1.2497571638956968,
    p_fc560c: 5.0063780207098425,
    p_1a7816: 3.1562533916051736,
    p_981c1e: 2.5163050709890156,
    p_484055: 0.7279391018916035,
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
backend_94350856d2bf45dc9a96d51dc2e3db4a = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_94350856d2bf45dc9a96d51dc2e3db4a, shots=2771).result().get_counts(qc)
RESULT = counts
