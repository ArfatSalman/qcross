# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(3, name='qr')
cr = ClassicalRegister(3, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(CCZGate(), qargs=[qr[2], qr[1], qr[0]], cargs=[])
qc.append(CU3Gate(2.6781418933705265, 5.033873892484971, 0.8205539045157343), qargs=[qr[0], qr[2]], cargs=[])
qc.append(CSGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(CSdgGate(), qargs=[qr[2], qr[1]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CYGate(), qargs=[qr[1], qr[2]], cargs=[])
subcircuit.append(CRZGate(2.0238721057673663), qargs=[qr[0], qr[2]], cargs=[])
subcircuit.append(U2Gate(4.584479443719739,1.724423394919128), qargs=[qr[0]], cargs=[])
subcircuit.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
subcircuit.append(CRYGate(0.8712775153371473), qargs=[qr[0], qr[1]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CRYGate(1.4158427363998418), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CU3Gate(3.033025708292916, 4.882023158927633, 2.498989202347216), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CSGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(U2Gate(1.2920361589137734, 0.11522677196421838), qargs=[qr[2]], cargs=[])
qc.append(CUGate(0.5771195062234611, 6.03105941204732, 5.250698623145584, 4.055221339124102), qargs=[qr[1], qr[2]], cargs=[])
qc.append(CU3Gate(1.40128081782857, 0.22745116565007226, 1.0942942714535664), qargs=[qr[2], qr[1]], cargs=[])
qc.append(CU3Gate(5.272901276657899, 4.665266516802061, 4.874107923353778), qargs=[qr[0], qr[2]], cargs=[])
qc.append(CXGate(), qargs=[qr[1], qr[2]], cargs=[])
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
backend_3f0e52f587954fc4bdbadd08ba784f27 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_3f0e52f587954fc4bdbadd08ba784f27, shots=489).result().get_counts(qc)
RESULT = counts
