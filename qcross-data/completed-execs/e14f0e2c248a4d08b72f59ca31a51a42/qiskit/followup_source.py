# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_51dc20 = Parameter('p_51dc20')
p_f1ce6e = Parameter('p_f1ce6e')
p_f92e4f = Parameter('p_f92e4f')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_f1ce6e), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_51dc20), qargs=[qr[6], qr[3]], cargs=[])
qc.append(CRXGate(p_f92e4f), qargs=[qr[1], qr[7]], cargs=[])
qc.append(CCXGate(), qargs=[qr[5], qr[9], qr[7]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[9]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_51dc20: 4.2641612072511235, p_f1ce6e: 6.163759533339787,
    p_f92e4f: 5.987304452123941,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=['cx', 'h', 's', 't'], optimization_level=2, coupling_map=[[0, 1], [0, 8], [1, 0], [1, 3], [2, 10], [2, 11], [3, 1], [3, 7], [3, 9], [4, 8], [5, 10], [6, 7], [7, 3], [7, 6], [7, 10], [8, 0], [8, 4], [9, 3], [10, 2], [10, 5], [10, 7], [11, 2]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_299a42bedf0347fd9da6c5e68726f729 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_299a42bedf0347fd9da6c5e68726f729, shots=5542).result().get_counts(qc)
RESULT = counts
