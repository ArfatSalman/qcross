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
p_697c3f = Parameter('p_697c3f')
p_961765 = Parameter('p_961765')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(4, name='qr')
cr = ClassicalRegister(4, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_697c3f), qargs=[qr[1]], cargs=[])
qc.append(RZZGate(p_961765), qargs=[qr[2], qr[3]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_697c3f: 6.163759533339787,
    p_961765: 4.066449154047175,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_b154b0c0112d48febfef954438378e67 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_b154b0c0112d48febfef954438378e67, shots=692).result().get_counts(qc)
RESULT = counts
