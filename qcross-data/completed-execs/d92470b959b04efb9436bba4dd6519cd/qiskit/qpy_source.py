# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_dd8db9 = Parameter('p_dd8db9')
p_fbfefd = Parameter('p_fbfefd')
p_79e2ca = Parameter('p_79e2ca')
p_d2a644 = Parameter('p_d2a644')
p_803a1f = Parameter('p_803a1f')
p_fd6f6d = Parameter('p_fd6f6d')
p_50a615 = Parameter('p_50a615')
p_bae028 = Parameter('p_bae028')
p_49f1fc = Parameter('p_49f1fc')
p_5b9a9c = Parameter('p_5b9a9c')
p_4a90e8 = Parameter('p_4a90e8')
p_28e9ae = Parameter('p_28e9ae')
p_d68182 = Parameter('p_d68182')
p_f964c1 = Parameter('p_f964c1')
p_02c08d = Parameter('p_02c08d')
p_64828e = Parameter('p_64828e')
p_1ab04f = Parameter('p_1ab04f')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_5b9a9c), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[6]], cargs=[])
qc.append(CRXGate(p_dd8db9), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CRZGate(p_d2a644), qargs=[qr[1], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[7], qr[6], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(p_d68182), qargs=[qr[6], qr[7]], cargs=[])
qc.append(CRZGate(p_50a615), qargs=[qr[1], qr[7]], cargs=[])
qc.append(RZGate(p_fbfefd), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(CU1Gate(p_4a90e8), qargs=[qr[4], qr[0]], cargs=[])
qc.append(CRXGate(p_f964c1), qargs=[qr[6], qr[4]], cargs=[])
qc.append(RZZGate(p_28e9ae), qargs=[qr[7], qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(RZGate(p_02c08d), qargs=[qr[4]], cargs=[])
qc.append(CRXGate(p_bae028), qargs=[qr[0], qr[3]], cargs=[])
qc.append(CUGate(p_1ab04f, p_79e2ca, 3.1562533916051736, p_49f1fc), qargs=[qr[6], qr[2]], cargs=[])
qc.append(U2Gate(p_64828e, p_fd6f6d), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[6]], cargs=[])
qc.append(SdgGate(), qargs=[qr[0]], cargs=[])
qc.append(RZZGate(p_803a1f), qargs=[qr[3], qr[4]], cargs=[])
qc.append(TGate(), qargs=[qr[5]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_dd8db9: 5.987304452123941, p_fbfefd: 4.229610589867865, p_79e2ca: 5.0063780207098425, p_d2a644: 1.0296448789776642, p_803a1f: 3.950837470808744, p_fd6f6d: 2.1276323672732023, p_50a615: 4.167661441102218, p_bae028: 0.7279391018916035, p_49f1fc: 4.940217775579305, p_5b9a9c: 6.163759533339787, p_4a90e8: 3.2142159669963557, p_28e9ae: 5.1829934776392745, p_d68182: 1.740253089260498, p_f964c1: 5.94477504571567, p_02c08d: 3.775592041307464, p_64828e: 2.5163050709890156, p_1ab04f: 5.03147076606842})
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=3, coupling_map=None)
# SECTION
# NAME: QASM_CONVERSION




def circuit_state_vector_are_equal(qc1, qc2):
    from qiskit.quantum_info import Statevector
    return Statevector.from_instruction(qc1).equiv(Statevector.from_instruction(qc2))

def qpy_roundtrip(qiskit_qc):
    from qiskit import qpy
    import os
    import uuid
    qc_id = uuid.uuid4().hex
    with open(f'{qc_id}.qpy', 'wb') as fd:
        qpy.dump(qiskit_qc, fd)

    with open(f'{qc_id}.qpy', 'rb') as fd:
        new_qc = qpy.load(fd)[0]

    os.remove(f'{qc_id}.qpy')
    return new_qc

old_qc = qc
qc = qpy_roundtrip(qc)

assert circuit_state_vector_are_equal(
    old_qc.remove_final_measurements(inplace=False),
    qc.remove_final_measurements(inplace=False)
)

# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_e453ed5ab31d4e3882dc8f7af66070ce = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_e453ed5ab31d4e3882dc8f7af66070ce, shots=2771).result().get_counts(qc)
RESULT = counts
