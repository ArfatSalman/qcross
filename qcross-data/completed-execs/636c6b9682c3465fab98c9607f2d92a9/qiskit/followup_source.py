# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_dcc42c = Parameter('p_dcc42c')
p_e95c81 = Parameter('p_e95c81')
p_aa5610 = Parameter('p_aa5610')
p_68ba36 = Parameter('p_68ba36')
p_a73b08 = Parameter('p_a73b08')
p_22c7ba = Parameter('p_22c7ba')
p_033778 = Parameter('p_033778')
p_69de3c = Parameter('p_69de3c')
p_79b734 = Parameter('p_79b734')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_a73b08), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[6]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CRZGate(p_e95c81), qargs=[qr[1], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[7], qr[6], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(p_033778), qargs=[qr[6], qr[7]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[1], qr[7]], cargs=[])
qc.append(RZGate(p_22c7ba), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(CU1Gate(3.2142159669963557), qargs=[qr[4], qr[0]], cargs=[])
qc.append(CRXGate(5.94477504571567), qargs=[qr[6], qr[4]], cargs=[])
qc.append(RZZGate(5.1829934776392745), qargs=[qr[7], qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(RZGate(p_aa5610), qargs=[qr[4]], cargs=[])
qc.append(CRXGate(p_79b734), qargs=[qr[0], qr[3]], cargs=[])
qc.append(CUGate(5.03147076606842, p_68ba36, 3.1562533916051736, p_69de3c), qargs=[qr[6], qr[2]], cargs=[])
qc.append(U2Gate(2.5163050709890156, 2.1276323672732023), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[6]], cargs=[])
qc.append(SdgGate(), qargs=[qr[0]], cargs=[])
qc.append(RZZGate(3.950837470808744), qargs=[qr[3], qr[4]], cargs=[])
qc.append(TGate(), qargs=[qr[5]], cargs=[])
qc.append(RYYGate(p_dcc42c), qargs=[qr[4], qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[3], qr[2], qr[5]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[7]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_dcc42c: 1.9669252191306448, p_e95c81: 1.0296448789776642, p_aa5610: 3.775592041307464, p_68ba36: 5.0063780207098425, p_a73b08: 6.163759533339787, p_22c7ba: 4.229610589867865, p_033778: 1.740253089260498, p_69de3c: 4.940217775579305, p_79b734: 0.7279391018916035})
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_0d655441f02f4dd4a462ad056d7b25a4 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_0d655441f02f4dd4a462ad056d7b25a4, shots=2771).result().get_counts(qc)
RESULT = counts
