# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_8a56c7 = Parameter('p_8a56c7')
p_12f990 = Parameter('p_12f990')
p_474773 = Parameter('p_474773')
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_8a56c7), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[2], qr[3]], cargs=[])
qc.append(CRXGate(p_12f990), qargs=[qr[5], qr[1]], cargs=[])
qc.append(CCXGate(), qargs=[qr[7], qr[8], qr[1]], cargs=[])
qc.append(ZGate(), qargs=[qr[4]], cargs=[])
qc.append(TGate(), qargs=[qr[8]], cargs=[])
qc.append(XGate(), qargs=[qr[9]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[5], qr[2]], cargs=[])
qc.append(RZGate(p_474773), qargs=[qr[5]], cargs=[])
qc.append(SXGate(), qargs=[qr[4]], cargs=[])
qc.append(CSXGate(), qargs=[qr[6], qr[9]], cargs=[])
qc.append(CCXGate(), qargs=[qr[6], qr[8], qr[7]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_8a56c7: 6.163759533339787, p_12f990: 5.987304452123941, p_474773: 4.229610589867865})
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
backend_80b8493c44884708ae31c8c071096018 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_80b8493c44884708ae31c8c071096018, shots=5542).result().get_counts(qc)
RESULT = counts
