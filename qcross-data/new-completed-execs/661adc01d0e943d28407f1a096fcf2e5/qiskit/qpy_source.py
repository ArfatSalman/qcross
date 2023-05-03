# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(C3SXGate(), qargs=[qr[1], qr[7], qr[0], qr[4]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[5], qr[8], qr[4], qr[2]], cargs=[])
qc.append(U3Gate(6.008634238353898, 2.0635146775063, 5.768504254562961), qargs=[qr[0]], cargs=[])
qc.append(U3Gate(1.5087622692163951, 3.321557818375962, 0.6345136241229505), qargs=[qr[2]], cargs=[])
qc.append(C4XGate(), qargs=[qr[9], qr[6], qr[2], qr[0], qr[7]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_627c9c = QuantumRegister(9, name='qr_627c9c')
qc.add_register(qr_627c9c)
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

assert circuit_state_vector_are_equal(
    old_qc.remove_final_measurements(inplace=False),
    qc.remove_final_measurements(inplace=False)
)

# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_605b6b8715fd485cb47e4dd1dbec041e = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_605b6b8715fd485cb47e4dd1dbec041e, shots=5542).result().get_counts(qc)
RESULT = counts
