# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_feb594 = Parameter('p_feb594')
p_a9cf83 = Parameter('p_a9cf83')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[6]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CU3Gate(1.2827690425732097, 1.3283826543858017, 3.672121211148789), qargs=[qr[2], qr[5]], cargs=[])
subcircuit.append(CZGate(), qargs=[qr[0], qr[1]], cargs=[])
subcircuit.append(U1Gate(6.2047416485134805), qargs=[qr[0]], cargs=[])
subcircuit.append(ECRGate(), qargs=[qr[3], qr[0]], cargs=[])
subcircuit.append(U2Gate(5.887184334931191, 0.07157463504881167), qargs=[qr[6]], cargs=[])
subcircuit.append(CU3Gate(5.1829934776392745, 2.7315239782495464, 3.9984051265341463), qargs=[qr[2], qr[0]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CRXGate(p_feb594), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CRZGate(p_a9cf83), qargs=[qr[1], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[7], qr[6], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_feb594: 5.987304452123941, p_a9cf83: 1.0296448789776642})
# SECTION
# NAME: QASM_CONVERSION
qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=3, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_5113df85399f4b88bce066617248c980 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_5113df85399f4b88bce066617248c980, shots=2771).result().get_counts(qc)
RESULT = counts
