# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS
# SECTION
# NAME: PARAMETERS
p_697101 = Parameter('p_697101')
p_5a355d = Parameter('p_5a355d')
p_eb0661 = Parameter('p_eb0661')
p_219124 = Parameter('p_219124')
p_31ccf5 = Parameter('p_31ccf5')
p_c0bd09 = Parameter('p_c0bd09')
p_f7209d = Parameter('p_f7209d')
p_c4e7fa = Parameter('p_c4e7fa')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(7, name='qr')
cr = ClassicalRegister(7, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_c0bd09), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[3]], cargs=[])
qc.append(CRXGate(p_697101), qargs=[qr[2], qr[5]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[6], qr[0], qr[1], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[4], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[2], qr[1], qr[5]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(ECRGate(), qargs=[qr[6], qr[3]], cargs=[])
qc.append(SdgGate(), qargs=[qr[6]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[2], qr[5], qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[1]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[2], qr[1], qr[3]], cargs=[])
qc.append(CU1Gate(p_c4e7fa), qargs=[qr[4], qr[0]], cargs=[])
qc.append(CRXGate(p_f7209d), qargs=[qr[4], qr[6]], cargs=[])
qc.append(CHGate(), qargs=[qr[4], qr[0]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[0], qr[3], qr[4]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(iSwapGate(), qargs=[qr[1], qr[6]], cargs=[])
subcircuit.append(CPhaseGate(p_31ccf5), qargs=[qr[0], qr[6]], cargs=[])
subcircuit.append(CU1Gate(2.0685963035149753), qargs=[qr[4], qr[0]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(ZGate(), qargs=[qr[5]], cargs=[])
qc.append(CRZGate(4.833923139882297), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CU1Gate(p_5a355d), qargs=[qr[1], qr[4]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[0], qr[5], qr[4]], cargs=[])
qc.append(CRZGate(p_eb0661), qargs=[qr[6], qr[2]], cargs=[])
qc.append(U2Gate(p_219124, 2.1276323672732023), qargs=[qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_697101: 2.0099472182748075,
    p_5a355d: 4.028174522740928,
    p_eb0661: 2.586208953975239,
    p_219124: 2.5163050709890156,
    p_31ccf5: 3.326780904591333,
    p_c0bd09: 6.163759533339787,
    p_f7209d: 5.94477504571567,
    p_c4e7fa: 3.2142159669963557,
})

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
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_e1175476e8be4523b2b08272a54b83d0 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_e1175476e8be4523b2b08272a54b83d0, shots=1959).result().get_counts(qc)
RESULT = counts
