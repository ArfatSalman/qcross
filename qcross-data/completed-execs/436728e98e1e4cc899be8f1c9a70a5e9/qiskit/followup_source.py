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
p_f36ce2 = Parameter('p_f36ce2')
p_3c5b38 = Parameter('p_3c5b38')
p_2be356 = Parameter('p_2be356')
p_a02e63 = Parameter('p_a02e63')
p_230af2 = Parameter('p_230af2')
p_e694fd = Parameter('p_e694fd')
p_6036fe = Parameter('p_6036fe')
p_feb03e = Parameter('p_feb03e')
p_8056eb = Parameter('p_8056eb')
p_02880f = Parameter('p_02880f')
p_2ba9cb = Parameter('p_2ba9cb')
p_383aef = Parameter('p_383aef')
p_22cd76 = Parameter('p_22cd76')
p_13a733 = Parameter('p_13a733')
p_4c6189 = Parameter('p_4c6189')
p_4e6bd3 = Parameter('p_4e6bd3')
p_872d56 = Parameter('p_872d56')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_02880f), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[6]], cargs=[])
qc.append(CRXGate(p_f36ce2), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CRZGate(p_a02e63), qargs=[qr[1], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[7], qr[6], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(p_22cd76), qargs=[qr[6], qr[7]], cargs=[])
qc.append(CRZGate(p_6036fe), qargs=[qr[1], qr[7]], cargs=[])
qc.append(RZGate(p_3c5b38), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(CU1Gate(p_2ba9cb), qargs=[qr[4], qr[0]], cargs=[])
qc.append(CRXGate(p_13a733), qargs=[qr[6], qr[4]], cargs=[])
qc.append(RZZGate(p_383aef), qargs=[qr[7], qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(RZGate(p_4c6189), qargs=[qr[4]], cargs=[])
qc.append(CRXGate(p_feb03e), qargs=[qr[0], qr[3]], cargs=[])
qc.append(CUGate(p_872d56, p_2be356, 3.1562533916051736, p_8056eb), qargs=[
    qr[6], qr[2]], cargs=[])
qc.append(U2Gate(p_4e6bd3, p_e694fd), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[6]], cargs=[])
qc.append(SdgGate(), qargs=[qr[0]], cargs=[])
qc.append(RZZGate(p_230af2), qargs=[qr[3], qr[4]], cargs=[])
qc.append(TGate(), qargs=[qr[5]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_f36ce2: 5.987304452123941,
    p_3c5b38: 4.229610589867865,
    p_2be356: 5.0063780207098425,
    p_a02e63: 1.0296448789776642,
    p_230af2: 3.950837470808744,
    p_e694fd: 2.1276323672732023,
    p_6036fe: 4.167661441102218,
    p_feb03e: 0.7279391018916035,
    p_8056eb: 4.940217775579305,
    p_02880f: 6.163759533339787,
    p_2ba9cb: 3.2142159669963557,
    p_383aef: 5.1829934776392745,
    p_22cd76: 1.740253089260498,
    p_13a733: 5.94477504571567,
    p_4c6189: 3.775592041307464,
    p_4e6bd3: 2.5163050709890156,
    p_872d56: 5.03147076606842,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_c78a6c58a57a44468de6b555aa24defd = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_c78a6c58a57a44468de6b555aa24defd, shots=2771).result().get_counts(qc)
RESULT = counts
