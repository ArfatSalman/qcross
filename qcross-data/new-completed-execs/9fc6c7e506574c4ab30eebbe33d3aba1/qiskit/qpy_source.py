# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(11, name='qr')
cr = ClassicalRegister(11, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(XGate(), qargs=[qr[3]], cargs=[])
qc.append(CRYGate(2.4498821250483043), qargs=[qr[10], qr[9]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CPhaseGate(5.94833048963124), qargs=[qr[6], qr[3]], cargs=[])
subcircuit.append(RCCXGate(), qargs=[qr[2], qr[9], qr[4]], cargs=[])
subcircuit.append(CCZGate(), qargs=[qr[2], qr[9], qr[5]], cargs=[])
subcircuit.append(SXdgGate(), qargs=[qr[4]], cargs=[])
subcircuit.append(iSwapGate(), qargs=[qr[0], qr[6]], cargs=[])
subcircuit.append(U1Gate(4.170850588142773), qargs=[qr[6]], cargs=[])
subcircuit.append(CUGate(3.6349610195058815, 3.819623549514622, 1.4862870686636986, 3.4327806393198337), qargs=[qr[3], qr[6]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(HGate(), qargs=[qr[1]], cargs=[])
qc.append(HGate(), qargs=[qr[2]], cargs=[])
qc.append(CPhaseGate(3.3516599839543195), qargs=[qr[4], qr[3]], cargs=[])
qc.append(ECRGate(), qargs=[qr[5], qr[8]], cargs=[])
qc.append(CU3Gate(5.423661738344168, 1.2257558063112008, 4.146906161622092), qargs=[qr[1], qr[8]], cargs=[])
qc.append(RXXGate(0.4988271119481185), qargs=[qr[7], qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=None)
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
backend_b680b5720a554baeb0bf35fe02b097a3 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_b680b5720a554baeb0bf35fe02b097a3, shots=7838).result().get_counts(qc)
RESULT = counts
