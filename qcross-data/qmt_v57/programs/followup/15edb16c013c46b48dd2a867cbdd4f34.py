# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RGate(1.3462943863788401, 2.0625679674283215), qargs=[qr[2]], cargs=[])
qc.append(RYGate(3.7263733381135333), qargs=[qr[4]], cargs=[])
qc.append(CRZGate(3.624574776344154), qargs=[qr[7], qr[3]], cargs=[])
qc.append(CUGate(2.7575077791457248, 2.0665317573057798, 5.876304122002991, 5.455724865836178), qargs=[qr[3], qr[0]], cargs=[])
qc.append(RZZGate(6.059622421697095), qargs=[qr[2], qr[6]], cargs=[])
qc.append(C4XGate(), qargs=[qr[0], qr[4], qr[1], qr[5], qr[6]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(ECRGate(), qargs=[qr[2], qr[4]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[6]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[1]], cargs=[])
qc.append(CRZGate(3.472333959218345), qargs=[qr[7], qr[3]], cargs=[])
qc.append(CRYGate(2.364247849527231), qargs=[qr[7], qr[1]], cargs=[])
qc.append(CRZGate(0.8522442036798011), qargs=[qr[6], qr[4]], cargs=[])
qc.append(RGate(0.44671874703610037, 4.595620654661833), qargs=[qr[3]], cargs=[])
qc.append(SXGate(), qargs=[qr[3]], cargs=[])
qc.append(DCXGate(), qargs=[qr[1], qr[5]], cargs=[])
qc.append(CUGate(2.010079880074799, 3.570167881942785, 3.7199764092307213, 0.8777762419082662), qargs=[qr[6], qr[4]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[1]], cargs=[])
qc.append(CRXGate(5.895791450120457), qargs=[qr[0], qr[5]], cargs=[])
qc.append(CU3Gate(2.3777076314685166, 0.2787777190001789, 6.013755670278601), qargs=[qr[5], qr[6]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=[[0, 1], [0, 8], [1, 0], [1, 2], [1, 9], [2, 1], [3, 11], [4, 9], [5, 10], [5, 11], [6, 8], [6, 11], [7, 9], [8, 0], [8, 6], [9, 1], [9, 4], [9, 7], [10, 5], [11, 3], [11, 5], [11, 6]])# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_4b378c5f450143fb827e1d94b4233aff = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_4b378c5f450143fb827e1d94b4233aff, shots=2771).result().get_counts(qc)
RESULT = counts
