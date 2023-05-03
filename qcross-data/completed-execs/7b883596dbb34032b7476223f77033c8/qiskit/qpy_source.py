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
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(CSwapGate(), qargs=[qr[7], qr[6], qr[3]], cargs=[])
qc.append(ECRGate(), qargs=[qr[3], qr[1]], cargs=[])
qc.append(RXGate(4.0941649085780565), qargs=[qr[5]], cargs=[])
qc.append(PhaseGate(1.8301283012499292), qargs=[qr[1]], cargs=[])
qc.append(CPhaseGate(1.547393669354307), qargs=[qr[2], qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[4]], cargs=[])
qc.append(SGate(), qargs=[qr[3]], cargs=[])
qc.append(CPhaseGate(3.6025830866934596), qargs=[qr[7], qr[0]], cargs=[])
qc.append(SwapGate(), qargs=[qr[6], qr[3]], cargs=[])
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
qc = transpile(qc, basis_gates=['ccx', 'h'], optimization_level=1, coupling_map=None)# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_dbb0d8c2e5c043bc9402bf9efa8cf282 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_dbb0d8c2e5c043bc9402bf9efa8cf282, shots=2771).result().get_counts(qc)
RESULT = counts
