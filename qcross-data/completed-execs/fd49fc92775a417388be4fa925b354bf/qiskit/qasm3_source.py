# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_3c4bb1 = Parameter('p_3c4bb1')
p_5e74b9 = Parameter('p_5e74b9')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_3c4bb1), qargs=[qr[3]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CRXGate(p_5e74b9), qargs=[qr[4], qr[3]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_3c4bb1: 6.163759533339787, p_5e74b9: 2.0099472182748075})
# SECTION
# NAME: QASM_CONVERSION


from qiskit.qasm3 import loads, dumps
qc = loads(dumps(qc))

# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0,
    1], [0, 2], [1, 0], [1, 3], [2, 0], [2, 4], [3, 1], [4, 2]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_6513f4c68d464bc0af40828885cde66d = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_6513f4c68d464bc0af40828885cde66d, shots=979).result().get_counts(qc)
RESULT = counts
