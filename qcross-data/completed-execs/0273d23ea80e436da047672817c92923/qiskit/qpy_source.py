# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(11, name='qr')
cr = ClassicalRegister(11, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[6], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(U3Gate(0.5150078127444868,5.017245588344839,2.936349225876477), qargs=[qr[3]], cargs=[])
subcircuit.append(XGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(RCCXGate(), qargs=[qr[8], qr[10], qr[6]], cargs=[])
subcircuit.append(CUGate(5.0063780207098425,3.1562533916051736,4.940217775579305,2.419481683937988), qargs=[qr[2], qr[1]], cargs=[])
subcircuit.append(CSwapGate(), qargs=[qr[10], qr[0], qr[7]], cargs=[])
subcircuit.append(PhaseGate(5.5146057452272546), qargs=[qr[0]], cargs=[])
subcircuit.append(ECRGate(), qargs=[qr[3], qr[0]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CCXGate(), qargs=[qr[5], qr[9], qr[7]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[7]], cargs=[])
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
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 3], [0, 6], [0, 8], [0, 11], [0, 12], [1, 0], [1, 6], [1, 7], [1, 9], [2, 9], [3, 0], [3, 7], [3, 10], [3, 12], [4, 7], [5, 7], [6, 0], [6, 1], [6, 13], [7, 1], [7, 3], [7, 4], [7, 5], [7, 9], [8, 0], [9, 1], [9, 2], [9, 7], [10, 3], [10, 12], [11, 0], [11, 13], [12, 0], [12, 3], [12, 10], [13, 6], [13, 11]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_d675e63e834a4c079cdbe07a503cc4c8 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_d675e63e834a4c079cdbe07a503cc4c8, shots=7838).result().get_counts(qc)
RESULT = counts
