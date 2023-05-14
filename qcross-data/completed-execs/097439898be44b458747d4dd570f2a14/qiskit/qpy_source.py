# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_38d9cb = Parameter('p_38d9cb')
p_6fbfe4 = Parameter('p_6fbfe4')
p_6b711e = Parameter('p_6b711e')
p_bb0c9a = Parameter('p_bb0c9a')
p_afbfa9 = Parameter('p_afbfa9')
p_985fe0 = Parameter('p_985fe0')
p_f413fb = Parameter('p_f413fb')
p_dc4e0f = Parameter('p_dc4e0f')
p_7ac4d4 = Parameter('p_7ac4d4')
p_559ba5 = Parameter('p_559ba5')
p_6b4cf2 = Parameter('p_6b4cf2')
p_30bc99 = Parameter('p_30bc99')
p_3e628e = Parameter('p_3e628e')
p_e762e6 = Parameter('p_e762e6')
p_f754b8 = Parameter('p_f754b8')
p_a9c7f4 = Parameter('p_a9c7f4')
p_01c9cb = Parameter('p_01c9cb')
p_ae29cc = Parameter('p_ae29cc')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_559ba5), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[6]], cargs=[])
qc.append(CRXGate(p_38d9cb), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CRZGate(p_bb0c9a), qargs=[qr[1], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[7], qr[6], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(p_3e628e), qargs=[qr[6], qr[7]], cargs=[])
qc.append(CRZGate(p_f413fb), qargs=[qr[1], qr[7]], cargs=[])
qc.append(RZGate(p_6fbfe4), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(CU1Gate(p_6b4cf2), qargs=[qr[4], qr[0]], cargs=[])
qc.append(CRXGate(p_e762e6), qargs=[qr[6], qr[4]], cargs=[])
qc.append(RZZGate(p_30bc99), qargs=[qr[7], qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(RZGate(p_f754b8), qargs=[qr[4]], cargs=[])
qc.append(CRXGate(p_dc4e0f), qargs=[qr[0], qr[3]], cargs=[])
qc.append(CUGate(p_01c9cb, p_6b711e, p_ae29cc, p_7ac4d4), qargs=[qr[6], qr[2]], cargs=[])
qc.append(U2Gate(p_a9c7f4, p_985fe0), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[6]], cargs=[])
qc.append(SdgGate(), qargs=[qr[0]], cargs=[])
qc.append(RZZGate(p_afbfa9), qargs=[qr[3], qr[4]], cargs=[])
qc.append(TGate(), qargs=[qr[5]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_38d9cb: 5.987304452123941, p_6fbfe4: 4.229610589867865, p_6b711e: 5.0063780207098425, p_bb0c9a: 1.0296448789776642, p_afbfa9: 3.950837470808744, p_985fe0: 2.1276323672732023, p_f413fb: 4.167661441102218, p_dc4e0f: 0.7279391018916035, p_7ac4d4: 4.940217775579305, p_559ba5: 6.163759533339787, p_6b4cf2: 3.2142159669963557, p_30bc99: 5.1829934776392745, p_3e628e: 1.740253089260498, p_e762e6: 5.94477504571567, p_f754b8: 3.775592041307464, p_a9c7f4: 2.5163050709890156, p_01c9cb: 5.03147076606842, p_ae29cc: 3.1562533916051736})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=['rx', 'ry', 'rz', 'p', 'cx'], optimization_level=2, coupling_map=None)
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

assert old_qc == qc
# assert circuit_state_vector_are_equal(
#     old_qc.remove_final_measurements(inplace=False),
#     qc.remove_final_measurements(inplace=False)
# )

# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_be4d9a20eeaf468385f18b36833160a9 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_be4d9a20eeaf468385f18b36833160a9, shots=2771).result().get_counts(qc)
RESULT = counts
