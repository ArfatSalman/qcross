# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(6, name='qr')
cr = ClassicalRegister(6, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[5], qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 2], [0, 3], [1, 0], [2, 0], [2, 6], [3, 0], [3, 4], [3, 5], [4, 3], [5, 3], [5, 7], [6, 2], [7, 5]])
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
backend_6235bb2c4a97450aa749e6187f953205 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_6235bb2c4a97450aa749e6187f953205, shots=1385).result().get_counts(qc)
RESULT = counts
