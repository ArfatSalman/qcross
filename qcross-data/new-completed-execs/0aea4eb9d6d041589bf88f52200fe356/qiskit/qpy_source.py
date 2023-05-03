# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(2, name='qr')
cr = ClassicalRegister(2, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RYYGate(0.040332757463886044), qargs=[qr[1], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(RZXGate(2.0199977459798464), qargs=[qr[0], qr[1]], cargs=[])
qc.append(RXXGate(3.927829733740478), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CYGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CRZGate(5.451741496819523), qargs=[qr[0], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RXXGate(2.6277753952279403), qargs=[qr[0], qr[1]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(CRZGate(3.555542082325973), qargs=[qr[0], qr[1]], cargs=[])
qc.append(RYYGate(5.488061464125162), qargs=[qr[0], qr[1]], cargs=[])
qc.append(RXGate(3.657037356032689), qargs=[qr[0]], cargs=[])
qc.append(RXGate(4.976946713501052), qargs=[qr[1]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CRYGate(3.142547021000323), qargs=[qr[0], qr[1]], cargs=[])
subcircuit.append(SGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(U1Gate(1.1029693994010046), qargs=[qr[1]], cargs=[])
subcircuit.append(CZGate(), qargs=[qr[1], qr[0]], cargs=[])
subcircuit.append(SGate(), qargs=[qr[1]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(ECRGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[1]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(RGate(5.88245539296814, 5.313337512106651), qargs=[qr[1]], cargs=[])
qc.append(RXGate(3.1801000664195067), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(2.60217238429383), qargs=[qr[1], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(CYGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[1]], cargs=[])
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
qc = transpile(qc, basis_gates=None, optimization_level=1, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_7f8640fa487647fca511dc020a826ee2 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_7f8640fa487647fca511dc020a826ee2, shots=346).result().get_counts(qc)
RESULT = counts
