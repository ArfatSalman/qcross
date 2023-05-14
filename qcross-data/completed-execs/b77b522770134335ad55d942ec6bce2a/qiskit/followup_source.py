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
p_d5d30f = Parameter('p_d5d30f')
p_483362 = Parameter('p_483362')
p_c08e15 = Parameter('p_c08e15')
p_304ede = Parameter('p_304ede')
p_3c2ca3 = Parameter('p_3c2ca3')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(3, name='qr')
cr = ClassicalRegister(3, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_304ede), qargs=[qr[1]], cargs=[])
qc.append(CHGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[2], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(SGate(), qargs=[qr[2]], cargs=[])
qc.append(SdgGate(), qargs=[qr[1]], cargs=[])
qc.append(CRXGate(p_d5d30f), qargs=[qr[0], qr[2]], cargs=[])
qc.append(SGate(), qargs=[qr[2]], cargs=[])
qc.append(CCXGate(), qargs=[qr[1], qr[0], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(RYYGate(p_483362), qargs=[qr[1], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(SGate(), qargs=[qr[2]], cargs=[])
qc.append(ECRGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[1], qr[0], qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(SdgGate(), qargs=[qr[2]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[0], qr[2], qr[1]], cargs=[])
qc.append(CRZGate(p_c08e15), qargs=[qr[2], qr[1]], cargs=[])
qc.append(SGate(), qargs=[qr[2]], cargs=[])
qc.append(CRZGate(p_3c2ca3), qargs=[qr[2], qr[1]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_a899a5 = QuantumRegister(3, name='qr_a899a5')
qc.add_register(qr_a899a5)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_d5d30f: 5.987304452123941,
    p_483362: 1.6723037552953224,
    p_c08e15: 4.167661441102218,
    p_304ede: 6.163759533339787,
    p_3c2ca3: 0.05525155902669336,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=3, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_0060e0dd6e7945db95a7fde9161ecc7c = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_0060e0dd6e7945db95a7fde9161ecc7c, shots=489).result().get_counts(qc)
RESULT = counts
