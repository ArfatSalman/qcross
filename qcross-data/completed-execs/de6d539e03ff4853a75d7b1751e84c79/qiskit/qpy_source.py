# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(DCXGate(), qargs=[qr[7], qr[1]], cargs=[])
qc.append(CRZGate(3.5837947443419367), qargs=[qr[7], qr[3]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CRYGate(4.123021946449677), qargs=[qr[5], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[4], qr[7]], cargs=[])
qc.append(RZXGate(4.811413391581055), qargs=[qr[5], qr[0]], cargs=[])
qc.append(CU1Gate(3.648178050626694), qargs=[qr[6], qr[4]], cargs=[])
qc.append(RYGate(5.8216640063628375), qargs=[qr[1]], cargs=[])
qc.append(CU1Gate(0.7038286154091901), qargs=[qr[7], qr[1]], cargs=[])
qc.append(DCXGate(), qargs=[qr[2], qr[5]], cargs=[])
qc.append(CYGate(), qargs=[qr[6], qr[5]], cargs=[])
qc.append(SGate(), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(0.18001367059010623), qargs=[qr[1], qr[6]], cargs=[])
qc.append(ZGate(), qargs=[qr[4]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[6]], cargs=[])
qc.append(PhaseGate(5.414747327887186), qargs=[qr[1]], cargs=[])
qc.append(CRYGate(4.001439863248854), qargs=[qr[1], qr[5]], cargs=[])
qc.append(SXGate(), qargs=[qr[2]], cargs=[])
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
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_0a9efd66126540d6a0d2f7c2d79ee854 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_0a9efd66126540d6a0d2f7c2d79ee854, shots=2771).result().get_counts(qc)
RESULT = counts
