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
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(RXGate(6.033961191253911), qargs=[qr[4]], cargs=[])
subcircuit.append(UGate(5.01836135520768, 5.190931186022931, 
    1.2128092629174942), qargs=[qr[5]], cargs=[])
subcircuit.append(DCXGate(), qargs=[qr[9], qr[6]], cargs=[])
subcircuit.append(CUGate(4.229610589867865, 2.696266694818697, 
    5.631160518436971, 2.9151388486514547), qargs=[qr[0], qr[2]], cargs=[])
subcircuit.append(ECRGate(), qargs=[qr[2], qr[0]], cargs=[])
subcircuit.append(C3XGate(5.94477504571567), qargs=[qr[8], qr[5], qr[6], qr
    [2]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 2], [0, 3], [0, 5], [0, 7], [0, 8], [0, 10], [1, 0], [1, 4], [2, 0], [2, 5], [3, 0], [4, 1], [5, 0], [5, 2], [6, 10], [7, 0], [8, 0], [9, 10], [10, 0], [10, 6], [10, 9]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_fe417d93146a4de18b941427da9c7712 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_fe417d93146a4de18b941427da9c7712, shots=5542).result().get_counts(qc)
RESULT = counts
