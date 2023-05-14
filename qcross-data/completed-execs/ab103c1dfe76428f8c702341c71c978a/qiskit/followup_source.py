# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_44bd2b = Parameter('p_44bd2b')
p_2e218a = Parameter('p_2e218a')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(3, name='qr')
cr = ClassicalRegister(3, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(U1Gate(p_2e218a), qargs=[qr[2]], cargs=[])
subcircuit.append(SwapGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(RZGate(p_44bd2b), qargs=[qr[1]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_44bd2b: 6.163759533339787,
    p_2e218a: 6.225782237242023,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 2], [1, 0], [2, 0]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_cb052c29b20043a5a0d9d2cf18c974c3 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_cb052c29b20043a5a0d9d2cf18c974c3, shots=489).result().get_counts(qc)
RESULT = counts
