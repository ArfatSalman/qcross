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
p_6d9df8 = Parameter('p_6d9df8')
p_f1ed17 = Parameter('p_f1ed17')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[6], qr[3]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[1], qr[7]], cargs=[])
qc.append(CCXGate(), qargs=[qr[5], qr[9], qr[7]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[9]], cargs=[])
qc.append(XGate(), qargs=[qr[8]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[1], qr[6]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[4], qr[8]], cargs=[])
qc.append(CCXGate(), qargs=[qr[4], qr[9], qr[5]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[4], qr[0], qr[9]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[7], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(CRZGate(p_f1ed17), qargs=[qr[1], qr[2]], cargs=[])
qc.append(U2Gate(p_6d9df8, 2.1276323672732023), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[9]], cargs=[])
qc.append(TGate(), qargs=[qr[8]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_6d9df8: 2.5163050709890156,
    p_f1ed17: 2.586208953975239,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_1e3e0e5848e8433093018b41da4b045d = Aer.get_backend('aer_simulator_density_matrix')
counts = execute(qc, backend=backend_1e3e0e5848e8433093018b41da4b045d, shots=5542).result().get_counts(qc)
RESULT = counts
