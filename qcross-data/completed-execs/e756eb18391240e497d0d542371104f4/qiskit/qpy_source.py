# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_63d6aa = Parameter('p_63d6aa')
p_92b6fe = Parameter('p_92b6fe')
p_db8eb2 = Parameter('p_db8eb2')
p_b138c0 = Parameter('p_b138c0')
p_2f176b = Parameter('p_2f176b')
p_4a9935 = Parameter('p_4a9935')
p_b2e764 = Parameter('p_b2e764')
p_bfb580 = Parameter('p_bfb580')
p_dfd8ce = Parameter('p_dfd8ce')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(4, name='qr')
cr = ClassicalRegister(4, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_92b6fe), qargs=[qr[1]], cargs=[])
qc.append(RZZGate(p_4a9935), qargs=[qr[2], qr[3]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(CUGate(p_dfd8ce, p_db8eb2, 2.3864521352475245, p_bfb580), qargs=[qr[0], qr[2]], cargs=[])
qc.append(CU1Gate(p_b2e764), qargs=[qr[3], qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[3], qr[0], qr[1], qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[3], qr[1], qr[0], qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[2]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[1], qr[0], qr[3]], cargs=[])
qc.append(RYYGate(p_2f176b), qargs=[qr[2], qr[0]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[2], qr[3], qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_b138c0), qargs=[qr[0], qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[2], qr[0], qr[3]], cargs=[])
qc.append(RYYGate(p_63d6aa), qargs=[qr[2], qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_c7cdf6 = QuantumRegister(8, name='qr_c7cdf6')
qc.add_register(qr_c7cdf6)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_63d6aa: 5.398622178940033, p_92b6fe: 6.163759533339787, p_db8eb2: 5.897054719225356, p_b138c0: 2.9790366726895714, p_2f176b: 1.740253089260498, p_4a9935: 4.066449154047175, p_b2e764: 5.154187354656876, p_bfb580: 5.987304452123941, p_dfd8ce: 0.5112149185250571})
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
qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_99c240589ce24ddbb4bcb09f5103eefe = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_99c240589ce24ddbb4bcb09f5103eefe, shots=692).result().get_counts(qc)
RESULT = counts
