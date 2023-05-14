# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_80e8e5 = Parameter('p_80e8e5')
p_d391ad = Parameter('p_d391ad')
p_58cdd0 = Parameter('p_58cdd0')
p_899200 = Parameter('p_899200')
p_ff62da = Parameter('p_ff62da')
p_5b5ed2 = Parameter('p_5b5ed2')
p_4c1552 = Parameter('p_4c1552')
p_118d87 = Parameter('p_118d87')
p_683b64 = Parameter('p_683b64')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_683b64), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_58cdd0), qargs=[qr[6], qr[3]], cargs=[])
qc.append(CRXGate(p_5b5ed2), qargs=[qr[1], qr[7]], cargs=[])
qc.append(CCXGate(), qargs=[qr[5], qr[9], qr[7]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[9]], cargs=[])
qc.append(XGate(), qargs=[qr[8]], cargs=[])
qc.append(CRZGate(p_d391ad), qargs=[qr[1], qr[6]], cargs=[])
qc.append(RZGate(p_4c1552), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[4], qr[8]], cargs=[])
qc.append(CCXGate(), qargs=[qr[4], qr[9], qr[5]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[4], qr[0], qr[9]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[7], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(CRZGate(p_899200), qargs=[qr[1], qr[2]], cargs=[])
qc.append(U2Gate(p_118d87, p_ff62da), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[9]], cargs=[])
qc.append(TGate(), qargs=[qr[8]], cargs=[])
qc.append(RZGate(p_80e8e5), qargs=[qr[1]], cargs=[])
# SECTION

# NAME: MEASUREMENT
# Execute the circuit and obtain the unitary matrix
from qiskit import Aer, transpile, execute
result = execute(qc.reverse_bits(), backend=Aer.get_backend('unitary_simulator')).result()
UNITARY = result.get_unitary(qc).data


qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_80e8e5: 5.014941143947427, p_d391ad: 4.167661441102218, p_58cdd0: 4.2641612072511235, p_899200: 2.586208953975239, p_ff62da: 2.1276323672732023,
    p_5b5ed2: 5.987304452123941,
    p_4c1552: 4.229610589867865,
    p_118d87: 2.5163050709890156,
    p_683b64: 6.163759533339787,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_7e9c919475464d2893148d6fc8b7ae7e = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_7e9c919475464d2893148d6fc8b7ae7e, shots=5542).result().get_counts(qc)
RESULT = counts
