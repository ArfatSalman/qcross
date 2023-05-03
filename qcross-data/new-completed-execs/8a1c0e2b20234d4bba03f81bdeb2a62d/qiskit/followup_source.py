# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS
# SECTION
# NAME: PARAMETERS
p_435d0d = Parameter('p_435d0d')
p_3c07ca = Parameter('p_3c07ca')
p_ccc6de = Parameter('p_ccc6de')
p_f9d2fd = Parameter('p_f9d2fd')
p_6b41c3 = Parameter('p_6b41c3')
p_8c914c = Parameter('p_8c914c')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(3, name='qr')
cr = ClassicalRegister(3, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(CPhaseGate(p_6b41c3), qargs=[qr[1], qr[2]], cargs=[])
qc.append(U1Gate(p_3c07ca), qargs=[qr[2]], cargs=[])
qc.append(UGate(p_f9d2fd, p_435d0d, p_ccc6de), qargs=[qr[2]], cargs=[])
qc.append(PhaseGate(p_8c914c), qargs=[qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[0]], cargs=[])# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_435d0d: 1.2201500361327853,
    p_3c07ca: 5.072633818750175,
    p_ccc6de: 4.276690396183425,
    p_f9d2fd: 3.8090985869250003,
    p_6b41c3: 1.7910282654595102,
    p_8c914c: 2.482034489972267,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=3, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_a08aa04906704b39985f20fd74bced81 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_a08aa04906704b39985f20fd74bced81, shots=489).result().get_counts(qc)
RESULT = counts
