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
p_a097d1 = Parameter('p_a097d1')
p_fbe730 = Parameter('p_fbe730')
p_e16421 = Parameter('p_e16421')
p_136200 = Parameter('p_136200')
p_2941ca = Parameter('p_2941ca')
p_00d3fa = Parameter('p_00d3fa')
p_2c8bf5 = Parameter('p_2c8bf5')
p_61b250 = Parameter('p_61b250')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_a097d1), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[6]], cargs=[])
qc.append(CRXGate(p_61b250), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CRZGate(p_2c8bf5), qargs=[qr[1], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[7], qr[6], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(p_00d3fa), qargs=[qr[6], qr[7]], cargs=[])
qc.append(CRZGate(p_136200), qargs=[qr[1], qr[7]], cargs=[])
qc.append(RZGate(p_2941ca), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(CU1Gate(3.2142159669963557), qargs=[qr[4], qr[0]], cargs=[])
qc.append(CRXGate(p_fbe730), qargs=[qr[6], qr[4]], cargs=[])
qc.append(RZZGate(p_e16421), qargs=[qr[7], qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_a097d1: 6.163759533339787,
    p_fbe730: 5.94477504571567,
    p_e16421: 5.1829934776392745,
    p_136200: 4.167661441102218,
    p_2941ca: 4.229610589867865,
    p_00d3fa: 1.740253089260498,
    p_2c8bf5: 1.0296448789776642,
    p_61b250: 5.987304452123941,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_76b7deb775b045a59cd089215196cc53 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_76b7deb775b045a59cd089215196cc53, shots=2771).result().get_counts(qc)
RESULT = counts
