# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(3, name='qr')
cr = ClassicalRegister(3, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(DCXGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(RXGate(6.0811696452339525), qargs=[qr[0]], cargs=[])
qc.append(TdgGate(), qargs=[qr[1]], cargs=[])
qc.append(DCXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(SwapGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(RXGate(0.6094072051955249), qargs=[qr[2]], cargs=[])
qc.append(TdgGate(), qargs=[qr[0]], cargs=[])
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
qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_08903a2209e44ba6bfd01ee7e104dca9 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_08903a2209e44ba6bfd01ee7e104dca9, shots=489).result().get_counts(qc)
RESULT = counts
