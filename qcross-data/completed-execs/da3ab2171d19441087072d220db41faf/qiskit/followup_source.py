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
p_28ea63 = Parameter('p_28ea63')
p_651c14 = Parameter('p_651c14')
p_3602d5 = Parameter('p_3602d5')
p_72aff8 = Parameter('p_72aff8')
p_169af4 = Parameter('p_169af4')
p_0a613b = Parameter('p_0a613b')
p_9cbb9b = Parameter('p_9cbb9b')
p_5bab06 = Parameter('p_5bab06')
p_878acf = Parameter('p_878acf')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(11, name='qr')
cr = ClassicalRegister(11, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_9cbb9b), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_28ea63), qargs=[qr[6], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(CCXGate(), qargs=[qr[5], qr[9], qr[7]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[7]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[10], qr[6], qr[8]], cargs=[])
qc.append(RZGate(p_651c14), qargs=[qr[0]], cargs=[])
qc.append(CCXGate(), qargs=[qr[7], qr[10], qr[2]], cargs=[])
qc.append(SdgGate(), qargs=[qr[7]], cargs=[])
qc.append(U2Gate(4.214504315296764, p_169af4), qargs=[qr[10]], cargs=[])
qc.append(CSXGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[7]], cargs=[])
qc.append(CU1Gate(p_72aff8), qargs=[qr[9], qr[0]], cargs=[])
qc.append(RZGate(p_5bab06), qargs=[qr[6]], cargs=[])
qc.append(U2Gate(p_0a613b, p_878acf), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[0]], cargs=[])
qc.append(RZZGate(p_3602d5), qargs=[qr[4], qr[0]], cargs=[])
qc.append(TGate(), qargs=[qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_28ea63: 4.2641612072511235,
    p_651c14: 4.229610589867865,
    p_3602d5: 3.950837470808744,
    p_72aff8: 4.028174522740928,
    p_169af4: 4.6235667602042065,
    p_0a613b: 2.5163050709890156,
    p_9cbb9b: 6.163759533339787,
    p_5bab06: 5.0063780207098425,
    p_878acf: 2.1276323672732023,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_60b98d4e806a4c728df124c2abb84958 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_60b98d4e806a4c728df124c2abb84958, shots=7838).result().get_counts(qc)
RESULT = counts
