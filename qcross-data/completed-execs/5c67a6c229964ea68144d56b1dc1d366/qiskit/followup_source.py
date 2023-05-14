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
p_c22ee3 = Parameter('p_c22ee3')
p_1477d5 = Parameter('p_1477d5')
p_dd3917 = Parameter('p_dd3917')
p_d41fd7 = Parameter('p_d41fd7')
p_ef9572 = Parameter('p_ef9572')
p_1fb36c = Parameter('p_1fb36c')
p_42a4f3 = Parameter('p_42a4f3')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(7, name='qr')
cr = ClassicalRegister(7, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_1477d5), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[3]], cargs=[])
qc.append(CRXGate(p_42a4f3), qargs=[qr[2], qr[5]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[6], qr[0], qr[1], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[4], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[2], qr[1], qr[5]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(ECRGate(), qargs=[qr[6], qr[3]], cargs=[])
qc.append(SdgGate(), qargs=[qr[6]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[2], qr[5], qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[1]], cargs=[])
qc.append(RZGate(p_c22ee3), qargs=[qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[2], qr[1], qr[3]], cargs=[])
qc.append(CU1Gate(p_ef9572), qargs=[qr[4], qr[0]], cargs=[])
qc.append(CRXGate(p_d41fd7), qargs=[qr[4], qr[6]], cargs=[])
qc.append(CHGate(), qargs=[qr[4], qr[0]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[0], qr[3], qr[4]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[5]], cargs=[])
qc.append(CRZGate(p_dd3917), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CU1Gate(p_1fb36c), qargs=[qr[1], qr[4]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_bf1373 = QuantumRegister(1, name='qr_bf1373')
qc.add_register(qr_bf1373)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_c22ee3: 4.229610589867865,
    p_1477d5: 6.163759533339787,
    p_dd3917: 4.833923139882297,
    p_d41fd7: 5.94477504571567,
    p_ef9572: 3.2142159669963557,
    p_1fb36c: 4.028174522740928,
    p_42a4f3: 2.0099472182748075,
})

# SECTION
# NAME: QASM_CONVERSION

qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=['ccx', 'h'], optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_a5274485ebce4862b6d17c2e6ba56f8c = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_a5274485ebce4862b6d17c2e6ba56f8c, shots=1959).result().get_counts(qc)
RESULT = counts
