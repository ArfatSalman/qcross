# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr_1 = QuantumRegister(5, name='qr_1')
cr_1 = ClassicalRegister(5, name='cr_1')
qc_1 = QuantumCircuit(qr_1, cr_1, name='qc_1')


qc_1.append(RZGate(6.163759533339787), qargs=[qr_1[1]], cargs=[])
qc_1.append(CRZGate(4.2641612072511235), qargs=[qr_1[0], qr_1[1]], cargs=[])


qr_2 = QuantumRegister(1, name='qr_2')
cr_2 = ClassicalRegister(1, name='cr_2')
qc_2 = QuantumCircuit(qr_2, cr_2, name='qc_2')


qc_2.append(ZGate(), qargs=[qr_2[0]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_d44553 = QuantumRegister(9, name='qr_d44553')
qc_1.add_register(qr_d44553)
# SECTION
# NAME: MEASUREMENT

qc_1.measure(qr_1, cr_1)
qc_2.measure(qr_2, cr_2)
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

old_qc_1 = qc_1

qc_1 = qpy_roundtrip(qc_1)
assert circuit_state_vector_are_equal(
    old_qc_1.remove_final_measurements(inplace=False),
    qc_1.remove_final_measurements(inplace=False)
)


old_qc_2 = qc_2
qc_2 = qpy_roundtrip(qc_2)

assert circuit_state_vector_are_equal(
    old_qc_2.remove_final_measurements(inplace=False),
    qc_2.remove_final_measurements(inplace=False)
)

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc_1 = transpile(qc_1, basis_gates=None, optimization_level=2, coupling_map=None)
qc_2 = transpile(qc_2, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_d96d476d4d4446a895056925955e58f8 = Aer.get_backend('qasm_simulator')
counts_1 = execute(qc_1, backend=backend_d96d476d4d4446a895056925955e58f8, shots=1385).result().get_counts(qc_1)
counts_2 = execute(qc_2, backend=backend_d96d476d4d4446a895056925955e58f8, shots=1385).result().get_counts(qc_2)
RESULT = [counts_1, counts_2]
