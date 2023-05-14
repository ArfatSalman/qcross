# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_023a7d = Parameter('p_023a7d')
p_21ba07 = Parameter('p_21ba07')
p_4a69b2 = Parameter('p_4a69b2')
p_b96fd4 = Parameter('p_b96fd4')
p_1c6cdf = Parameter('p_1c6cdf')
p_7d7c65 = Parameter('p_7d7c65')
p_66e932 = Parameter('p_66e932')
p_8b6baf = Parameter('p_8b6baf')
p_9ec620 = Parameter('p_9ec620')
p_628297 = Parameter('p_628297')
p_4c04c2 = Parameter('p_4c04c2')
p_f3b666 = Parameter('p_f3b666')
p_edb705 = Parameter('p_edb705')
p_1a21da = Parameter('p_1a21da')
p_52c99c = Parameter('p_52c99c')
p_7fc368 = Parameter('p_7fc368')
p_ad4dbb = Parameter('p_ad4dbb')
p_d7b9ee = Parameter('p_d7b9ee')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_7fc368), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[6]], cargs=[])
qc.append(CRXGate(p_1a21da), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CRZGate(p_52c99c), qargs=[qr[1], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[7], qr[6], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(p_d7b9ee), qargs=[qr[6], qr[7]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[1], qr[7]], cargs=[])
qc.append(RZGate(p_1c6cdf), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(CU1Gate(p_7d7c65), qargs=[qr[4], qr[0]], cargs=[])
qc.append(CRXGate(p_4a69b2), qargs=[qr[6], qr[4]], cargs=[])
qc.append(RZZGate(p_f3b666), qargs=[qr[7], qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(RZGate(p_66e932), qargs=[qr[4]], cargs=[])
qc.append(CRXGate(p_edb705), qargs=[qr[0], qr[3]], cargs=[])
qc.append(CUGate(p_21ba07, p_628297, p_8b6baf, p_023a7d), qargs=[qr[6], qr[2]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CU3Gate(5.583322729510212, 4.773422973876057, 0.8960434543694032), qargs=[qr[4], qr[3]], cargs=[])
subcircuit.append(RCCXGate(), qargs=[qr[1], qr[6], qr[7]], cargs=[])
subcircuit.append(RXGate(1.723121374211541), qargs=[qr[1]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(U2Gate(p_b96fd4, p_ad4dbb), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[6]], cargs=[])
qc.append(SdgGate(), qargs=[qr[0]], cargs=[])
qc.append(RZZGate(p_9ec620), qargs=[qr[3], qr[4]], cargs=[])
qc.append(TGate(), qargs=[qr[5]], cargs=[])
qc.append(RYYGate(p_4c04c2), qargs=[qr[4], qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[3], qr[2], qr[5]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_b7d75d = QuantumRegister(4, name='qr_b7d75d')
qc.add_register(qr_b7d75d)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_023a7d: 4.940217775579305, p_21ba07: 5.03147076606842, p_4a69b2: 5.94477504571567, p_b96fd4: 2.5163050709890156, p_1c6cdf: 4.229610589867865, p_7d7c65: 3.2142159669963557, p_66e932: 3.775592041307464, p_8b6baf: 3.1562533916051736, p_9ec620: 3.950837470808744, p_628297: 5.0063780207098425, p_4c04c2: 1.9669252191306448, p_f3b666: 5.1829934776392745, p_edb705: 0.7279391018916035, p_1a21da: 5.987304452123941, p_52c99c: 1.0296448789776642, p_7fc368: 6.163759533339787, p_ad4dbb: 2.1276323672732023, p_d7b9ee: 1.740253089260498})
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
backend_75d5bb77dec94eadaefdb66a6a88bcb3 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_75d5bb77dec94eadaefdb66a6a88bcb3, shots=2771).result().get_counts(qc)
RESULT = counts
