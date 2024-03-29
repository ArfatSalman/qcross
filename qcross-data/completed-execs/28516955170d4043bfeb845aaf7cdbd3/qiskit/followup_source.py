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
p_665093 = Parameter('p_665093')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CRXGate(p_665093), qargs=[qr[4], qr[3]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_665093: 2.0099472182748075,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 4], [0, 5], [1, 0], [1, 6], [2, 4], [3, 6], [4, 0], [4, 2], [5, 0], [6, 1], [6, 3]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_eaae1efd72c242a29cbaed93edae8a36 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_eaae1efd72c242a29cbaed93edae8a36, shots=979).result().get_counts(qc)
RESULT = counts
