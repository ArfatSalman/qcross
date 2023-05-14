# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(RZXGate(0.6833824466861163), qargs=[qr[0], qr[6]], cargs=[])
subcircuit.append(UGate(2.6397681660693015,5.320621737498446,3.427505621225153), qargs=[qr[5]], cargs=[])
subcircuit.append(ZGate(), qargs=[qr[2]], cargs=[])
subcircuit.append(UGate(5.01836135520768,5.190931186022931,1.2128092629174942), qargs=[qr[4]], cargs=[])
subcircuit.append(DCXGate(), qargs=[qr[1], qr[8]], cargs=[])
subcircuit.append(CUGate(4.229610589867865,2.696266694818697,5.631160518436971,2.9151388486514547), qargs=[qr[0], qr[9]], cargs=[])
subcircuit.append(ECRGate(), qargs=[qr[9], qr[0]], cargs=[])
subcircuit.append(C3XGate(5.94477504571567), qargs=[qr[6], qr[4], qr[8], qr[9]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CRZGate(4.2641612072511235), qargs=[qr[6], qr[3]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_162816 = QuantumRegister(5, name='qr_162816')
qc.add_register(qr_162816)
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
backend_c0518cc129b040b0baf732f8a47d28ed = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_c0518cc129b040b0baf732f8a47d28ed, shots=5542).result().get_counts(qc)
RESULT = counts
