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
p_4891c3 = Parameter('p_4891c3')
p_4d6844 = Parameter('p_4d6844')
p_72b19d = Parameter('p_72b19d')
p_1dbd94 = Parameter('p_1dbd94')
p_ab8a7b = Parameter('p_ab8a7b')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(4, name='qr')
cr = ClassicalRegister(4, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(SdgGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(2.10593478876119), qargs=[qr[2], qr[1]], cargs=[])
qc.append(IGate(), qargs=[qr[1]], cargs=[])
qc.append(CZGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(CZGate(), qargs=[qr[0], qr[3]], cargs=[])
qc.append(CZGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(CU3Gate(p_72b19d, p_4891c3, p_4d6844), qargs=[qr[2], qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(CPhaseGate(p_1dbd94), qargs=[qr[2], qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(C3XGate(), qargs=[qr[3], qr[1], qr[2], qr[0]], cargs=[])
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_4891c3: 3.7847055340640803,
    p_4d6844: 5.596894918056728,
    p_72b19d: 5.177552214723695,
    p_1dbd94: 5.982058731459433,
    p_ab8a7b: 0.45470685223891605,
})

# SECTION
# NAME: QASM_CONVERSION

qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_175df900d2fe417bb4ef66ecf8261790 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_175df900d2fe417bb4ef66ecf8261790, shots=692).result().get_counts(qc)
RESULT = counts
