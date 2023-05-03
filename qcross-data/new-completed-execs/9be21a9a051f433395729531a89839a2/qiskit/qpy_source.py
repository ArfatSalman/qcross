# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(7, name='qr')
cr = ClassicalRegister(7, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RVGate(5.730485179497036, 5.1815317617582535, 4.954506343035782), qargs=[qr[0]], cargs=[])
qc.append(U1Gate(5.5351729304729), qargs=[qr[6]], cargs=[])
qc.append(IGate(), qargs=[qr[1]], cargs=[])
qc.append(RXXGate(1.620673138384231), qargs=[qr[1], qr[4]], cargs=[])
qc.append(SwapGate(), qargs=[qr[0], qr[3]], cargs=[])
qc.append(CUGate(2.5179284740661867, 4.218025714484969, 5.538801185807778, 0.2277932967359332), qargs=[qr[4], qr[5]], cargs=[])
qc.append(SXGate(), qargs=[qr[3]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(RGate(2.373112537407949, 2.0806292204834302), qargs=[qr[1]], cargs=[])
qc.append(CCZGate(), qargs=[qr[4], qr[1], qr[5]], cargs=[])
qc.append(YGate(), qargs=[qr[4]], cargs=[])
qc.append(RGate(1.3139288690051985, 5.834685188574328), qargs=[qr[6]], cargs=[])
qc.append(CCZGate(), qargs=[qr[2], qr[5], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(U1Gate(0.5163920678872455), qargs=[qr[5]], cargs=[])
qc.append(SGate(), qargs=[qr[2]], cargs=[])
qc.append(CCXGate(), qargs=[qr[4], qr[0], qr[5]], cargs=[])
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
backend_ef6876beba5a463fb121304325f2a5fb = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_ef6876beba5a463fb121304325f2a5fb, shots=1959).result().get_counts(qc)
RESULT = counts
