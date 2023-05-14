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
p_549fef = Parameter('p_549fef')
p_6e5194 = Parameter('p_6e5194')
p_afd57c = Parameter('p_afd57c')
p_78f5ff = Parameter('p_78f5ff')
p_2d015c = Parameter('p_2d015c')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(4, name='qr')
cr = ClassicalRegister(4, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[1]], cargs=[])
qc.append(RZZGate(4.066449154047175), qargs=[qr[2], qr[3]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(CUGate(p_549fef, p_78f5ff, p_2d015c, p_6e5194), qargs=[qr[0], qr[
    2]], cargs=[])
qc.append(CU1Gate(p_afd57c), qargs=[qr[3], qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[3], qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_549fef: 0.5112149185250571,
    p_6e5194: 5.987304452123941,
    p_afd57c: 5.154187354656876,
    p_78f5ff: 5.897054719225356,
    p_2d015c: 2.3864521352475245,
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
qc = transpile(qc, basis_gates=None, optimization_level=1, coupling_map=[[0, 1], [0, 4], [1, 0], [1, 2], [2, 1], [2, 5], [3, 4], [4, 0], [4, 3], [5, 2]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_9fc87029c9f549d9aa94ee32d6ad5040 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_9fc87029c9f549d9aa94ee32d6ad5040, shots=692).result().get_counts(qc)
RESULT = counts
