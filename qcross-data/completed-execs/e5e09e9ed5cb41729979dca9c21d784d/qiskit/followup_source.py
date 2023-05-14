# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_e69891 = Parameter('p_e69891')
p_247eba = Parameter('p_247eba')
p_1b9590 = Parameter('p_1b9590')
p_a00224 = Parameter('p_a00224')
p_1b011b = Parameter('p_1b011b')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_1b011b), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[6]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CRZGate(p_247eba), qargs=[qr[1], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[7], qr[6], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(1.740253089260498), qargs=[qr[6], qr[7]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[1], qr[7]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(CU1Gate(3.2142159669963557), qargs=[qr[4], qr[0]], cargs=[])
qc.append(CRXGate(5.94477504571567), qargs=[qr[6], qr[4]], cargs=[])
qc.append(RZZGate(5.1829934776392745), qargs=[qr[7], qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(RZGate(p_1b9590), qargs=[qr[4]], cargs=[])
qc.append(CRXGate(0.7279391018916035), qargs=[qr[0], qr[3]], cargs=[])
qc.append(CUGate(5.03147076606842, p_a00224, 3.1562533916051736, 4.940217775579305), qargs=[qr[6], qr[2]], cargs=[])
qc.append(U2Gate(2.5163050709890156, 2.1276323672732023), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[6]], cargs=[])
qc.append(SdgGate(), qargs=[qr[0]], cargs=[])
qc.append(RZZGate(3.950837470808744), qargs=[qr[3], qr[4]], cargs=[])
qc.append(TGate(), qargs=[qr[5]], cargs=[])
qc.append(RYYGate(p_e69891), qargs=[qr[4], qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[3], qr[2], qr[5]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[7]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_e69891: 1.9669252191306448, p_247eba: 1.0296448789776642, p_1b9590: 3.775592041307464, p_a00224: 5.0063780207098425, p_1b011b: 6.163759533339787})
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0,
    1], [0, 2], [0, 5], [1, 0], [1, 4], [2, 0], [2, 7], [3, 6], [4, 1], [4,
    6], [5, 0], [6, 3], [6, 4], [7, 2]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_ca08d6aa3f2243939309c7c813e35c2c = Aer.get_backend('aer_simulator_statevector')
counts = execute(qc, backend=backend_ca08d6aa3f2243939309c7c813e35c2c, shots=2771).result().get_counts(qc)
RESULT = counts
