# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(2, name='qr')
cr = ClassicalRegister(2, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(CRYGate(4.682220755041814), qargs=[qr[0], qr[1]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(SdgGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(SXdgGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(CSGate(), qargs=[qr[1], qr[0]], cargs=[])
subcircuit.append(PhaseGate(5.507061057045591), qargs=[qr[1]], cargs=[])
subcircuit.append(XGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(TGate(), qargs=[qr[1]], cargs=[])
subcircuit.append(U2Gate(2.3723321578370635,0.23310288505979176), qargs=[qr[1]], cargs=[])
subcircuit.append(CPhaseGate(3.5444640315452953), qargs=[qr[0], qr[1]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CUGate(5.960866266876448, 5.945098421875394, 4.418481228600101, 3.972623244718876), qargs=[qr[1], qr[0]], cargs=[])
qc.append(PhaseGate(2.031442273399285), qargs=[qr[0]], cargs=[])
qc.append(U1Gate(1.1449128292629545), qargs=[qr[1]], cargs=[])
qc.append(CRYGate(1.8638911468677428), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CSdgGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(RVGate(3.2561786456517483, 4.027853623334148, 0.7501118686992972), qargs=[qr[1]], cargs=[])
qc.append(PhaseGate(3.1265936864110326), qargs=[qr[0]], cargs=[])
qc.append(PhaseGate(2.7301494704572584), qargs=[qr[0]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(SdgGate(), qargs=[qr[1]], cargs=[])
qc.append(CRZGate(2.967811594681098), qargs=[qr[1], qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=3, coupling_map=None)
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
backend_a9caf8dee0a94f4fbf577c901caf1441 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_a9caf8dee0a94f4fbf577c901caf1441, shots=346).result().get_counts(qc)
RESULT = counts