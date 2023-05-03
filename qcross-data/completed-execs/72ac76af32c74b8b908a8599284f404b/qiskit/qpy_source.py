# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[9]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[0], qr[9]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[4], qr[6]], cargs=[])
qc.append(CCXGate(), qargs=[qr[2], qr[3], qr[6]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_26cb71 = QuantumRegister(9, name='qr_26cb71')
qc.add_register(qr_26cb71)
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

assert circuit_state_vector_are_equal(
    old_qc.remove_final_measurements(inplace=False),
    qc.remove_final_measurements(inplace=False)
)

# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_c2c6ed8b1ebc4256baf2409fdde35508 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_c2c6ed8b1ebc4256baf2409fdde35508, shots=5542).result().get_counts(qc)
RESULT = counts
