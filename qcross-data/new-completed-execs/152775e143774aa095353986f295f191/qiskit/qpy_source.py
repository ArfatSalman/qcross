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
qc.append(UGate(1.0932143214299395, 6.100531540039404, 4.859714896792146), qargs=[qr[1]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CYGate(), qargs=[qr[1], qr[0]], cargs=[])
subcircuit.append(RVGate(2.4118372331017857, 4.007316327236995, 4.304922836512128), qargs=[qr[1]], cargs=[])
subcircuit.append(RZXGate(4.840163560981886), qargs=[qr[1], qr[0]], cargs=[])
subcircuit.append(RXGate(2.7792529037894678), qargs=[qr[1]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CYGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(RXGate(4.335996068527454), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[1]], cargs=[])
qc.append(RXGate(6.070601620234646), qargs=[qr[0]], cargs=[])
qc.append(RZXGate(3.9660842997699097), qargs=[qr[0], qr[1]], cargs=[])
qc.append(HGate(), qargs=[qr[1]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1, coupling_map=None)
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
backend_5d6a769fcdcd4d108cb39014668c0094 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_5d6a769fcdcd4d108cb39014668c0094, shots=346).result().get_counts(qc)
RESULT = counts
