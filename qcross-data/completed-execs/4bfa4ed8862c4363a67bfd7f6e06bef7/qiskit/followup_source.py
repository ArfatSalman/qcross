# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[6], qr[3]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[1], qr[7]], cargs=[])
qc.append(CCXGate(), qargs=[qr[5], qr[9], qr[7]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(DCXGate(), qargs=[qr[1], qr[8]], cargs=[])
subcircuit.append(CUGate(4.229610589867865, 2.696266694818697, 5.631160518436971, 2.9151388486514547), qargs=[qr[0], qr[9]], cargs=[])
subcircuit.append(ECRGate(), qargs=[qr[9], qr[0]], cargs=[])
subcircuit.append(C3XGate(5.94477504571567), qargs=[qr[6], qr[4], qr[8], qr[9]], cargs=[])
subcircuit.append(HGate(), qargs=[qr[2]], cargs=[])
subcircuit.append(SXGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(CRZGate(2.008796895454228), qargs=[qr[0], qr[5]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[9]], cargs=[])
qc.append(XGate(), qargs=[qr[8]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0,
    1], [0, 3], [1, 0], [1, 10], [1, 12], [2, 9], [3, 0], [3, 7], [3, 13],
    [4, 8], [5, 9], [5, 11], [6, 12], [7, 3], [8, 4], [8, 12], [9, 2], [9, 
    5], [9, 12], [10, 1], [11, 5], [12, 1], [12, 6], [12, 8], [12, 9], [13, 3]]
    )
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_131d0337e56f49de9cca0d6a030ac022 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_131d0337e56f49de9cca0d6a030ac022, shots=5542).result().get_counts(qc)
RESULT = counts
