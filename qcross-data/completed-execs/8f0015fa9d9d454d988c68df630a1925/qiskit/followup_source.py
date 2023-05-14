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
p_b3b922 = Parameter('p_b3b922')
p_a1819b = Parameter('p_a1819b')
p_d7cdb5 = Parameter('p_d7cdb5')
p_b0de03 = Parameter('p_b0de03')
p_744464 = Parameter('p_744464')
p_1b382d = Parameter('p_1b382d')
p_c00892 = Parameter('p_c00892')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(11, name='qr')
cr = ClassicalRegister(11, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(RZXGate(p_a1819b), qargs=[qr[10], qr[7]], cargs=[])
subcircuit.append(CXGate(), qargs=[qr[2], qr[6]], cargs=[])
subcircuit.append(CZGate(), qargs=[qr[7], qr[4]], cargs=[])
subcircuit.append(CU1Gate(p_744464), qargs=[qr[1], qr[8]], cargs=[])
subcircuit.append(CUGate(p_c00892, p_b3b922, 5.631160518436971, p_1b382d),
    qargs=[qr[0], qr[10]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(RZGate(p_d7cdb5), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_b0de03), qargs=[qr[6], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_b3b922: 2.696266694818697,
    p_a1819b: 3.427505621225153,
    p_d7cdb5: 6.163759533339787,
    p_b0de03: 4.2641612072511235,
    p_744464: 4.501598818751339,
    p_1b382d: 2.9151388486514547,
    p_c00892: 4.229610589867865,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_f069fedc7426456689bd9de1a59d0fd2 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_f069fedc7426456689bd9de1a59d0fd2, shots=7838).result().get_counts(qc)
RESULT = counts
