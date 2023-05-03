# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_143887 = Parameter('p_143887')
p_72a534 = Parameter('p_72a534')
p_082ec3 = Parameter('p_082ec3')
p_fd33bb = Parameter('p_fd33bb')
p_c40958 = Parameter('p_c40958')
p_106180 = Parameter('p_106180')
p_083e1c = Parameter('p_083e1c')
p_36e2fe = Parameter('p_36e2fe')
p_f20bd4 = Parameter('p_f20bd4')
p_ec90c9 = Parameter('p_ec90c9')
p_2bbfa0 = Parameter('p_2bbfa0')
p_bb3cbe = Parameter('p_bb3cbe')
p_8baad8 = Parameter('p_8baad8')
p_057fbf = Parameter('p_057fbf')
p_0927f4 = Parameter('p_0927f4')
p_b8acf2 = Parameter('p_b8acf2')
p_1e860b = Parameter('p_1e860b')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_72a534), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[6]], cargs=[])
qc.append(CRXGate(p_36e2fe), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CRZGate(p_bb3cbe), qargs=[qr[1], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[7], qr[6], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(p_057fbf), qargs=[qr[6], qr[7]], cargs=[])
qc.append(CRZGate(p_0927f4), qargs=[qr[1], qr[7]], cargs=[])
qc.append(RZGate(p_b8acf2), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(CU1Gate(p_143887), qargs=[qr[4], qr[0]], cargs=[])
qc.append(CRXGate(p_ec90c9), qargs=[qr[6], qr[4]], cargs=[])
qc.append(RZZGate(p_fd33bb), qargs=[qr[7], qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(RZGate(p_082ec3), qargs=[qr[4]], cargs=[])
qc.append(CRXGate(p_106180), qargs=[qr[0], qr[3]], cargs=[])
qc.append(CUGate(p_8baad8, p_2bbfa0, p_c40958, p_1e860b), qargs=[qr[6], qr[2]], cargs=[])
qc.append(U2Gate(p_f20bd4, p_083e1c), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[6]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_143887: 3.2142159669963557, p_72a534: 6.163759533339787, p_082ec3: 3.775592041307464, p_fd33bb: 5.1829934776392745, p_c40958: 3.1562533916051736, p_106180: 0.7279391018916035, p_083e1c: 2.1276323672732023, p_36e2fe: 5.987304452123941, p_f20bd4: 2.5163050709890156, p_ec90c9: 5.94477504571567, p_2bbfa0: 5.0063780207098425, p_bb3cbe: 1.0296448789776642, p_8baad8: 5.03147076606842, p_057fbf: 1.740253089260498, p_0927f4: 4.167661441102218, p_b8acf2: 4.229610589867865, p_1e860b: 4.940217775579305})
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
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=['ccx', 'h'], optimization_level=3,
    coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_f0d4ad38700c4387bca297948d54ec2e = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_f0d4ad38700c4387bca297948d54ec2e, shots=2771).result().get_counts(qc)
RESULT = counts
