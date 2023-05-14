# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_e4a82b = Parameter('p_e4a82b')
p_897fa0 = Parameter('p_897fa0')
p_4c8c10 = Parameter('p_4c8c10')
p_42a1d4 = Parameter('p_42a1d4')
p_b41b47 = Parameter('p_b41b47')
p_f7f517 = Parameter('p_f7f517')
p_3d4bf9 = Parameter('p_3d4bf9')
p_258753 = Parameter('p_258753')
p_a5e20b = Parameter('p_a5e20b')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_42a1d4), qargs=[qr[6], qr[3]], cargs=[])
qc.append(CRXGate(p_258753), qargs=[qr[1], qr[7]], cargs=[])
qc.append(CCXGate(), qargs=[qr[5], qr[9], qr[7]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[9]], cargs=[])
qc.append(XGate(), qargs=[qr[8]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[1], qr[6]], cargs=[])
qc.append(RZGate(p_a5e20b), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[4], qr[8]], cargs=[])
qc.append(CCXGate(), qargs=[qr[4], qr[9], qr[5]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[4], qr[0], qr[9]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[7], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(CRZGate(p_f7f517), qargs=[qr[1], qr[2]], cargs=[])
qc.append(U2Gate(p_b41b47, p_4c8c10), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[9]], cargs=[])
qc.append(TGate(), qargs=[qr[8]], cargs=[])
qc.append(RZGate(p_e4a82b), qargs=[qr[1]], cargs=[])
qc.append(CRXGate(5.970852306777193), qargs=[qr[7], qr[1]], cargs=[])
qc.append(UGate(p_897fa0, p_3d4bf9, 2.271164628944128), qargs=[qr[2]], cargs=[])
qc.append(ECRGate(), qargs=[qr[4], qr[8]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[8]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[7]], cargs=[])
qc.append(RZGate(3.6614081973587154), qargs=[qr[5]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_078017 = QuantumRegister(2, name='qr_078017')
qc.add_register(qr_078017)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_e4a82b: 5.014941143947427, p_897fa0: 5.080799300534071, p_4c8c10: 2.1276323672732023, p_42a1d4: 4.2641612072511235, p_b41b47: 2.5163050709890156, p_f7f517: 2.586208953975239, p_3d4bf9: 5.023617931957853, p_258753: 5.987304452123941, p_a5e20b: 4.229610589867865})
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
backend_381d76e4facb40538c75b0e5fa5dc050 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_381d76e4facb40538c75b0e5fa5dc050, shots=5542).result().get_counts(qc)
RESULT = counts
