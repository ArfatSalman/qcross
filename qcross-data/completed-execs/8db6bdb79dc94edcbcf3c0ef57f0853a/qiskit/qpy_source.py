# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(7, name='qr')
cr = ClassicalRegister(7, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(TGate(), qargs=[qr[2]], cargs=[])
subcircuit.append(CZGate(), qargs=[qr[1], qr[4]], cargs=[])
subcircuit.append(CU3Gate(1.2827690425732097, 1.3283826543858017, 3.672121211148789), qargs=[qr[2], qr[6]], cargs=[])
subcircuit.append(CU3Gate(3.865496458458116, 2.6636908506222836, 6.221353754875494), qargs=[qr[5], qr[0]], cargs=[])
subcircuit.append(U1Gate(6.2047416485134805), qargs=[qr[0]], cargs=[])
subcircuit.append(TGate(), qargs=[qr[6]], cargs=[])
subcircuit.append(SXGate(), qargs=[qr[4]], cargs=[])
subcircuit.append(C3XGate(5.94477504571567), qargs=[qr[4], qr[6], qr[2], qr[1]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(XGate(), qargs=[qr[3]], cargs=[])
qc.append(CRXGate(2.0099472182748075), qargs=[qr[2], qr[5]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[6], qr[0], qr[1], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[4], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[2], qr[1], qr[5]], cargs=[])
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
backend_0e4c880fe7ce49c7b3d54faede436795 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_0e4c880fe7ce49c7b3d54faede436795, shots=1959).result().get_counts(qc)
RESULT = counts
