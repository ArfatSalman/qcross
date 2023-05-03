# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(4, name='qr')
cr = ClassicalRegister(4, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(YGate(), qargs=[qr[3]], cargs=[])
qc.append(CUGate(4.742596091504256, 5.602098424672528, 4.320385518485325, 3.3796506020234154), qargs=[qr[1], qr[2]], cargs=[])
qc.append(DCXGate(), qargs=[qr[1], qr[3]], cargs=[])
qc.append(CHGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[3]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[3]], cargs=[])
qc.append(YGate(), qargs=[qr[0]], cargs=[])
qc.append(CUGate(0.4698264522024645, 5.497223780656133, 0.6973970453004443, 4.135242097973106), qargs=[qr[2], qr[3]], cargs=[])
qc.append(DCXGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(CZGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(SGate(), qargs=[qr[2]], cargs=[])
qc.append(RZXGate(3.1312684847539773), qargs=[qr[3], qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[1]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(RXGate(2.6717356275928497), qargs=[qr[0]], cargs=[])
qc.append(CZGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[2], qr[1]], cargs=[])
qc.append(RYYGate(5.131718958124352), qargs=[qr[1], qr[3]], cargs=[])
qc.append(RYYGate(2.939587764936891), qargs=[qr[1], qr[3]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1, coupling_map=None)
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
backend_587c0eac3f694742924032f1fa2063ca = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_587c0eac3f694742924032f1fa2063ca, shots=692).result().get_counts(qc)
RESULT = counts
