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


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CRXGate(6.189367290017951), qargs=[qr[6], qr[0]], cargs=[])
subcircuit.append(HGate(), qargs=[qr[1]], cargs=[])
subcircuit.append(CU3Gate(3.795093132245643,5.482804960064541,3.392543408251406), qargs=[qr[0], qr[6]], cargs=[])
subcircuit.append(RXGate(2.870607397554538), qargs=[qr[4]], cargs=[])
subcircuit.append(CPhaseGate(4.002346068007423), qargs=[qr[3], qr[0]], cargs=[])
subcircuit.append(RVGate(4.068029717857408,0.567304873816878,3.215798805925656), qargs=[qr[6]], cargs=[])
subcircuit.append(RZZGate(3.9665175003040227), qargs=[qr[0], qr[3]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
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

assert circuit_state_vector_are_equal(
    old_qc.remove_final_measurements(inplace=False),
    qc.remove_final_measurements(inplace=False)
)

# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_d3882c4efb404e14af6d7f718730ea05 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_d3882c4efb404e14af6d7f718730ea05, shots=1959).result().get_counts(qc)
RESULT = counts
