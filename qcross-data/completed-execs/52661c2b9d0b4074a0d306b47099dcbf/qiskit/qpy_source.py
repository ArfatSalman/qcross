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


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
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

assert old_qc == qc
# assert circuit_state_vector_are_equal(
#     old_qc.remove_final_measurements(inplace=False),
#     qc.remove_final_measurements(inplace=False)
# )

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=['rx', 'ry', 'rz', 'p', 'cx'], optimization_level=2, coupling_map=[[0, 1], [0, 7], [0, 10], [1, 0], [1, 3], [1, 5], [1, 9], [2, 5], [3, 1], [4, 5], [5, 1], [5, 2], [5, 4], [5, 8], [6, 8], [7, 0], [8, 5], [8, 6], [9, 1], [10, 0]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_5abc8e8eac194e1f9961499ba610f3a4 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_5abc8e8eac194e1f9961499ba610f3a4, shots=7838).result().get_counts(qc)
RESULT = counts
