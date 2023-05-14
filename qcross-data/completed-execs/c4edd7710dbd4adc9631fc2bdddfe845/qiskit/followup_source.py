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
p_2c5a30 = Parameter('p_2c5a30')
p_d8aa57 = Parameter('p_d8aa57')
p_90c25c = Parameter('p_90c25c')
p_b36eca = Parameter('p_b36eca')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(4, name='qr')
cr = ClassicalRegister(4, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[1]], cargs=[])
qc.append(RZZGate(p_2c5a30), qargs=[qr[2], qr[3]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(CUGate(0.5112149185250571, 5.897054719225356, p_d8aa57, p_90c25c),
    qargs=[qr[0], qr[2]], cargs=[])
qc.append(CU1Gate(p_b36eca), qargs=[qr[3], qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[3], qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_2c5a30: 4.066449154047175,
    p_d8aa57: 2.3864521352475245,
    p_90c25c: 5.987304452123941,
    p_b36eca: 5.154187354656876,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_90ae195f45514735a64b02abbad8de1d = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_90ae195f45514735a64b02abbad8de1d, shots=692).result().get_counts(qc)
RESULT = counts
