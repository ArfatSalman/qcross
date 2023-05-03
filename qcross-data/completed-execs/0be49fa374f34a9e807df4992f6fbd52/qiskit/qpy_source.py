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
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
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
qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=[[0,
    1], [0, 7], [0, 13], [1, 0], [1, 2], [1, 9], [1, 11], [2, 1], [3, 12],
    [4, 11], [5, 9], [6, 9], [7, 0], [8, 13], [9, 1], [9, 5], [9, 6], [10, 
    11], [11, 1], [11, 4], [11, 10], [12, 3], [12, 13], [13, 0], [13, 8], [
    13, 12]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_367f6888697b4b8b87d0e48cbac666a2 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_367f6888697b4b8b87d0e48cbac666a2, shots=7838).result().get_counts(qc)
RESULT = counts
