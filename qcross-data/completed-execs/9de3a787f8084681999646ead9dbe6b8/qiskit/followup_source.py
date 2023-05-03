# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_13fb63 = Parameter('p_13fb63')
p_431cb7 = Parameter('p_431cb7')
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(11, name='qr')
cr = ClassicalRegister(11, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_431cb7), qargs=[qr[2]], cargs=[])
qc.append(CRZGate(p_13fb63), qargs=[qr[5], qr[8]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(CCXGate(), qargs=[qr[9], qr[7], qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[8]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_13fb63: 4.2641612072511235, p_431cb7: 6.163759533339787})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_45bee13940c44593a8d84c0649511df7 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_45bee13940c44593a8d84c0649511df7, shots=7838).result().get_counts(qc)
RESULT = counts
