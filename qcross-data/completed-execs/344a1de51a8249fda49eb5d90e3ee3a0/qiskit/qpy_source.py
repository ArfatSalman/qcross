# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_2e68f3 = Parameter('p_2e68f3')
p_f3b6b3 = Parameter('p_f3b6b3')
p_02e0d1 = Parameter('p_02e0d1')
p_bdd144 = Parameter('p_bdd144')
p_031c73 = Parameter('p_031c73')
p_9bff3f = Parameter('p_9bff3f')
p_d48307 = Parameter('p_d48307')
p_cbf48f = Parameter('p_cbf48f')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(7, name='qr')
cr = ClassicalRegister(7, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_02e0d1), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[3]], cargs=[])
qc.append(CRXGate(2.0099472182748075), qargs=[qr[2], qr[5]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[6], qr[0], qr[1], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[4], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[2], qr[1], qr[5]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(ECRGate(), qargs=[qr[6], qr[3]], cargs=[])
qc.append(SdgGate(), qargs=[qr[6]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[2], qr[5], qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[1]], cargs=[])
qc.append(RZGate(p_2e68f3), qargs=[qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[2], qr[1], qr[3]], cargs=[])
qc.append(CU1Gate(p_d48307), qargs=[qr[4], qr[0]], cargs=[])
qc.append(CRXGate(5.94477504571567), qargs=[qr[4], qr[6]], cargs=[])
qc.append(CHGate(), qargs=[qr[4], qr[0]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[0], qr[3], qr[4]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[5]], cargs=[])
qc.append(CRZGate(p_bdd144), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CU1Gate(p_9bff3f), qargs=[qr[1], qr[4]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[0], qr[5], qr[4]], cargs=[])
qc.append(CRZGate(p_f3b6b3), qargs=[qr[6], qr[2]], cargs=[])
qc.append(U2Gate(2.5163050709890156, p_cbf48f), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[6]], cargs=[])
qc.append(SdgGate(), qargs=[qr[0]], cargs=[])
qc.append(RZZGate(3.950837470808744), qargs=[qr[3], qr[4]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
qc.append(RYYGate(p_031c73), qargs=[qr[4], qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_2e68f3: 4.229610589867865, p_f3b6b3: 2.586208953975239, p_02e0d1: 6.163759533339787, p_bdd144: 4.833923139882297, p_031c73: 1.9669252191306448, p_9bff3f: 4.028174522740928, p_d48307: 3.2142159669963557, p_cbf48f: 2.1276323672732023})
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
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=[[0,
    1], [0, 2], [0, 3], [1, 0], [2, 0], [2, 5], [2, 6], [3, 0], [3, 4], [4,
    3], [5, 2], [6, 2]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_9d75398e92914bef9eba69bf326075ff = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_9d75398e92914bef9eba69bf326075ff, shots=1959).result().get_counts(qc)
RESULT = counts
