# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(4, name='qr')
cr = ClassicalRegister(4, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[1]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CHGate(), qargs=[qr[2], qr[0]], cargs=[])
subcircuit.append(CSXGate(), qargs=[qr[0], qr[1]], cargs=[])
subcircuit.append(CXGate(), qargs=[qr[2], qr[0]], cargs=[])
subcircuit.append(CYGate(), qargs=[qr[0], qr[1]], cargs=[])
subcircuit.append(RYGate(1.256213604505652), qargs=[qr[2]], cargs=[])
subcircuit.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(RZZGate(4.066449154047175), qargs=[qr[2], qr[3]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245, 5.987304452123941), qargs=[qr[0], qr[2]], cargs=[])
qc.append(CU1Gate(5.154187354656876), qargs=[qr[3], qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[3], qr[0], qr[1], qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[3], qr[1], qr[0], qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[2]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[1], qr[0], qr[3]], cargs=[])
qc.append(RYYGate(1.740253089260498), qargs=[qr[2], qr[0]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[2], qr[3], qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(2.9790366726895714), qargs=[qr[0], qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[2], qr[0], qr[3]], cargs=[])
qc.append(RYYGate(5.398622178940033), qargs=[qr[2], qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(CU1Gate(3.2142159669963557), qargs=[qr[0], qr[3]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[1], qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=['rx', 'ry', 'rz', 'p', 'cx'], optimization_level=2, coupling_map=None)
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
backend_dfcddd6654484afa878736806410713b = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_dfcddd6654484afa878736806410713b, shots=692).result().get_counts(qc)
RESULT = counts
