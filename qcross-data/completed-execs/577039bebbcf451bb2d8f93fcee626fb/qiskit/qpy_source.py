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
qc.append(CZGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(CCXGate(), qargs=[qr[2], qr[1], qr[0]], cargs=[])
qc.append(CU3Gate(0.02974191542848892, 1.097684714540871, 0.5523925010367368), qargs=[qr[1], qr[0]], cargs=[])
qc.append(HGate(), qargs=[qr[0]], cargs=[])
qc.append(U1Gate(4.64787760789041), qargs=[qr[0]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(YGate(), qargs=[qr[2]], cargs=[])
qc.append(CZGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(YGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(2.3941143994200504), qargs=[qr[1], qr[0]], cargs=[])
qc.append(TdgGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[2]], cargs=[])
qc.append(RXGate(5.932085825305516), qargs=[qr[2]], cargs=[])
qc.append(CSwapGate(), qargs=[qr[2], qr[0], qr[1]], cargs=[])
qc.append(SdgGate(), qargs=[qr[2]], cargs=[])
qc.append(U3Gate(0.20490217819899895, 0.2844754781181525, 4.8984947281198385), qargs=[qr[2]], cargs=[])
qc.append(CYGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(RYGate(4.64391690767843), qargs=[qr[1]], cargs=[])
qc.append(SGate(), qargs=[qr[1]], cargs=[])
qc.append(IGate(), qargs=[qr[0]], cargs=[])
qc.append(U1Gate(3.4582628336664856), qargs=[qr[0]], cargs=[])
qc.append(IGate(), qargs=[qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(CU1Gate(3.1245965108163056), qargs=[qr[1], qr[2]], cargs=[])
qc.append(RXGate(0.16532103311248328), qargs=[qr[1]], cargs=[])
qc.append(TdgGate(), qargs=[qr[2]], cargs=[])
qc.append(RYGate(2.5451656062496135), qargs=[qr[1]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=['ccx', 'h'], optimization_level=0, coupling_map=None)# SECTION
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
backend_d650849c1a8841998ff20a08d6bc8cf5 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_d650849c1a8841998ff20a08d6bc8cf5, shots=489).result().get_counts(qc)
RESULT = counts
