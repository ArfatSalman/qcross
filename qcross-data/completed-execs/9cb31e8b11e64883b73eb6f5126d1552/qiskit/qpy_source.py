# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CRXGate(2.0099472182748075), qargs=[qr[4], qr[3]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(CRZGate(1.0296448789776642), qargs=[qr[3], qr[4]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[4]], cargs=[])
qc.append(RYYGate(1.6723037552953224), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[4]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[4]], cargs=[])
qc.append(CUGate(5.708725119517347, 4.167661441102218, 4.623446645668956, 3.865496458458116), qargs=[qr[1], qr[4]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(5.398622178940033), qargs=[qr[0], qr[2]], cargs=[])
qc.append(CU1Gate(3.2142159669963557), qargs=[qr[3], qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=None)
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
backend_321bbe7f1f6f41918c2075899ac64057 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_321bbe7f1f6f41918c2075899ac64057, shots=979).result().get_counts(qc)
RESULT = counts
