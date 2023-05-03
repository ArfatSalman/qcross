# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_32432c = Parameter('p_32432c')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(ECRGate(), qargs=[qr[1], qr[0]], cargs=[])
subcircuit.append(HGate(), qargs=[qr[1]], cargs=[])
subcircuit.append(RZXGate(0.6833824466861163), qargs=[qr[0], qr[2]], cargs=[])
subcircuit.append(DCXGate(), qargs=[qr[1], qr[4]], cargs=[])
subcircuit.append(CPhaseGate(1.6161683469432118), qargs=[qr[1], qr[4]], cargs=[])
subcircuit.append(RXGate(p_32432c), qargs=[qr[1]], cargs=[])
subcircuit.append(ZGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(CXGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_32432c: 6.033961191253911})
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=[[0,
    1], [1, 0], [1, 3], [1, 5], [2, 5], [3, 1], [4, 5], [5, 1], [5, 2], [5, 4]]
    )
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_02fe0f3ecdbf4d439326d74549e62995 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_02fe0f3ecdbf4d439326d74549e62995, shots=979).result().get_counts(qc)
RESULT = counts
