# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_d13af9 = Parameter('p_d13af9')
p_baa0bd = Parameter('p_baa0bd')
p_feab72 = Parameter('p_feab72')
p_536ad5 = Parameter('p_536ad5')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(4, name='qr')
cr = ClassicalRegister(4, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_d13af9), qargs=[qr[1]], cargs=[])
qc.append(RZZGate(p_feab72), qargs=[qr[2], qr[3]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(CUGate(p_536ad5, 5.897054719225356, 2.3864521352475245, p_baa0bd), qargs=[qr[0], qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_d13af9: 6.163759533339787, p_baa0bd: 5.987304452123941, p_feab72: 4.066449154047175, p_536ad5: 0.5112149185250571})
# SECTION
# NAME: QASM_CONVERSION

from qiskit.qasm3 import loads, dumps
qc = loads(dumps(qc))

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_6f8b555e6ace46dda1b78431cf308fe0 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_6f8b555e6ace46dda1b78431cf308fe0, shots=692).result().get_counts(qc)
RESULT = counts
