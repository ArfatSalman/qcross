# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(TdgGate(), qargs=[qr[1]], cargs=[])
qc.append(CRYGate(0.8476513988624245), qargs=[qr[4], qr[0]], cargs=[])
qc.append(CU1Gate(1.5710197357755318), qargs=[qr[3], qr[2]], cargs=[])
qc.append(TdgGate(), qargs=[qr[2]], cargs=[])
qc.append(TdgGate(), qargs=[qr[1]], cargs=[])
qc.append(CCZGate(), qargs=[qr[2], qr[1], qr[3]], cargs=[])
qc.append(UGate(0.708502006099043, 2.97765669736744, 5.6444063351584415), qargs=[qr[2]], cargs=[])
qc.append(CPhaseGate(5.597667172921795), qargs=[qr[3], qr[4]], cargs=[])
qc.append(SXGate(), qargs=[qr[2]], cargs=[])
qc.append(CRYGate(0.3177314062860099), qargs=[qr[4], qr[1]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CSGate(), qargs=[qr[3], qr[0]], cargs=[])
subcircuit.append(SdgGate(), qargs=[qr[3]], cargs=[])
subcircuit.append(CRYGate(2.8571614999629205), qargs=[qr[1], qr[0]], cargs=[])
subcircuit.append(RZXGate(1.1653856966610614), qargs=[qr[2], qr[1]], cargs=[])
subcircuit.append(RXGate(5.646774609269053), qargs=[qr[4]], cargs=[])
subcircuit.append(CXGate(), qargs=[qr[2], qr[1]], cargs=[])
subcircuit.append(ZGate(), qargs=[qr[4]], cargs=[])
subcircuit.append(YGate(), qargs=[qr[2]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CU1Gate(1.9730677082046415), qargs=[qr[4], qr[2]], cargs=[])
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
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [1, 0], [1, 2], [1, 5], [1, 6], [2, 1], [2, 4], [3, 6], [4, 2], [5, 1], [6, 1], [6, 3]])# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_b1df125757c44a908a68e42ab2f8cb56 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_b1df125757c44a908a68e42ab2f8cb56, shots=979).result().get_counts(qc)
RESULT = counts
