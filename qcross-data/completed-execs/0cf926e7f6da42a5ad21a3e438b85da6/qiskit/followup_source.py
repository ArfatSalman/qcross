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
p_5e62ad = Parameter('p_5e62ad')
p_c72551 = Parameter('p_c72551')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(11, name='qr')
cr = ClassicalRegister(11, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_c72551), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_5e62ad), qargs=[qr[6], qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_5e62ad: 4.2641612072511235,
    p_c72551: 6.163759533339787,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_e87efcf8879f49b09f7770b3a4eac110 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_e87efcf8879f49b09f7770b3a4eac110, shots=7838).result().get_counts(qc)
RESULT = counts
