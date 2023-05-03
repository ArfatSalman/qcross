# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(7, name='qr')
cr = ClassicalRegister(7, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(CRXGate(4.540485128061974), qargs=[qr[2], qr[0]], cargs=[])
qc.append(CSwapGate(), qargs=[qr[3], qr[1], qr[2]], cargs=[])
qc.append(CSwapGate(), qargs=[qr[5], qr[1], qr[2]], cargs=[])
qc.append(RYYGate(4.463823258920204), qargs=[qr[1], qr[3]], cargs=[])
qc.append(CPhaseGate(3.371946193609531), qargs=[qr[6], qr[2]], cargs=[])
qc.append(RYYGate(3.3281963864143704), qargs=[qr[2], qr[0]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[3], qr[5], qr[1], qr[6]], cargs=[])
qc.append(RYGate(4.644790991147617), qargs=[qr[0]], cargs=[])
qc.append(CPhaseGate(0.3126995978940275), qargs=[qr[2], qr[5]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(RYYGate(6.048921809752355), qargs=[qr[5], qr[2]], cargs=[])
qc.append(U3Gate(3.2280333223438684, 1.6763403778979529, 1.308375256732971), qargs=[qr[4]], cargs=[])
qc.append(UGate(3.300493821011834, 2.7595037431292786, 0.0456041163048407), qargs=[qr[1]], cargs=[])
qc.append(CSwapGate(), qargs=[qr[2], qr[1], qr[6]], cargs=[])
qc.append(C3XGate(), qargs=[qr[3], qr[6], qr[4], qr[1]], cargs=[])
qc.append(UGate(4.005766554739231, 3.562181008920026, 1.1726853359197904), qargs=[qr[2]], cargs=[])
qc.append(C3XGate(), qargs=[qr[2], qr[5], qr[1], qr[6]], cargs=[])
qc.append(DCXGate(), qargs=[qr[5], qr[4]], cargs=[])
qc.append(RXXGate(1.0617494142412416), qargs=[qr[4], qr[0]], cargs=[])
qc.append(CZGate(), qargs=[qr[4], qr[2]], cargs=[])
qc.append(C3XGate(), qargs=[qr[4], qr[5], qr[1], qr[6]], cargs=[])
qc.append(CPhaseGate(3.64559874218163), qargs=[qr[0], qr[5]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[5], qr[6], qr[1], qr[2]], cargs=[])
qc.append(TdgGate(), qargs=[qr[6]], cargs=[])
qc.append(RZGate(3.7376045176206487), qargs=[qr[3]], cargs=[])
qc.append(RZZGate(0.353928536272812), qargs=[qr[1], qr[5]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: QASM_CONVERSION


from qiskit.qasm3 import loads, dumps
qc = loads(dumps(qc))

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 3], [1, 0], [1, 5], [1, 6], [2, 3], [2, 4], [3, 0], [3, 2], [4, 2], [5, 1], [6, 1]])
# SECTION
# NAME: EXECUTION
from qiskit import Aer, transpile, execute
backend_d08738fd158941bc93ac5373f943d222 = Aer.get_backend('aer_simulator_statevector')
counts = execute(qc, backend=backend_d08738fd158941bc93ac5373f943d222, shots=1959).result().get_counts(qc)
RESULT = counts