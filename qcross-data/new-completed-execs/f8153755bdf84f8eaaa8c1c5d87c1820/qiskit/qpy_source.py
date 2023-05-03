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
qc.append(CRXGate(4.905634676582973), qargs=[qr[4], qr[1]], cargs=[])
qc.append(RGate(4.591350839465064, 1.2679876620814976), qargs=[qr[5]], cargs=[])
qc.append(CZGate(), qargs=[qr[4], qr[10]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(SGate(), qargs=[qr[6]], cargs=[])
subcircuit.append(CPhaseGate(0.8912299955175988), qargs=[qr[10], qr[9]], cargs=[])
subcircuit.append(RXXGate(6.202385428323795), qargs=[qr[9], qr[2]], cargs=[])
subcircuit.append(CU3Gate(0.17275929115190944,3.979025542935018,1.5894459673585912), qargs=[qr[2], qr[8]], cargs=[])
subcircuit.append(RZGate(5.22819431699873), qargs=[qr[3]], cargs=[])
subcircuit.append(IGate(), qargs=[qr[4]], cargs=[])
subcircuit.append(RYGate(5.90619537594574), qargs=[qr[6]], cargs=[])
subcircuit.append(CU3Gate(3.688151163878286,4.727514924286728,4.075756946750543), qargs=[qr[7], qr[6]], cargs=[])
subcircuit.append(U1Gate(5.472976168291315), qargs=[qr[3]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(U3Gate(4.438175883374682, 5.014778227242978, 0.395105964485411), qargs=[qr[9]], cargs=[])
qc.append(IGate(), qargs=[qr[10]], cargs=[])
qc.append(CRXGate(2.8176864996575204), qargs=[qr[3], qr[4]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(IGate(), qargs=[qr[4]], cargs=[])
qc.append(SGate(), qargs=[qr[9]], cargs=[])
qc.append(CRXGate(6.06720431582227), qargs=[qr[0], qr[8]], cargs=[])
qc.append(U2Gate(3.8396484521920486, 5.389605086705323), qargs=[qr[0]], cargs=[])
qc.append(CYGate(), qargs=[qr[0], qr[9]], cargs=[])
qc.append(CRXGate(0.6410834959357722), qargs=[qr[1], qr[2]], cargs=[])
qc.append(CRXGate(3.152773209785367), qargs=[qr[5], qr[2]], cargs=[])
qc.append(CSGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[0], qr[8], qr[6], qr[4]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[3], qr[6]], cargs=[])
qc.append(CRYGate(3.8184925395522673), qargs=[qr[7], qr[1]], cargs=[])
qc.append(RZXGate(5.0844543693921445), qargs=[qr[9], qr[0]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[4], qr[3], qr[2]], cargs=[])
qc.append(U2Gate(0.5232088988285076, 1.5882644602699434), qargs=[qr[7]], cargs=[])
qc.append(CCZGate(), qargs=[qr[5], qr[2], qr[6]], cargs=[])
qc.append(IGate(), qargs=[qr[10]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[6], qr[10]], cargs=[])
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
backend_ab59878383fc4156b5150c5c856312ec = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_ab59878383fc4156b5150c5c856312ec, shots=7838).result().get_counts(qc)
RESULT = counts
