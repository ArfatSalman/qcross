# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(11, name='qr')
cr = ClassicalRegister(11, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[0]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[4], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[10]], cargs=[])
qc.append(CCXGate(), qargs=[qr[3], qr[1], qr[8]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[8]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[5], qr[4], qr[9]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[6]], cargs=[])
qc.append(CCXGate(), qargs=[qr[8], qr[5], qr[2]], cargs=[])
qc.append(SdgGate(), qargs=[qr[8]], cargs=[])
qc.append(U2Gate(4.214504315296764, 4.6235667602042065), qargs=[qr[5]],
    cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[6], qr[8]], cargs=[])
qc.append(CU1Gate(4.028174522740928), qargs=[qr[1], qr[6]], cargs=[])
qc.append(RZGate(5.0063780207098425), qargs=[qr[4]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
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
backend_5d5bee78483446b49333c13359bec321 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_5d5bee78483446b49333c13359bec321, shots=7838).result().get_counts(qc)
RESULT = counts
