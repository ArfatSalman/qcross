# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(HGate(), qargs=[qr[1]], cargs=[])
subcircuit.append(RZXGate(0.6833824466861163), qargs=[qr[0], qr[2]], cargs=[])
subcircuit.append(DCXGate(), qargs=[qr[1], qr[4]], cargs=[])
subcircuit.append(CPhaseGate(1.6161683469432118), qargs=[qr[1], qr[4]], cargs=[])
subcircuit.append(RXGate(6.033961191253911), qargs=[qr[1]], cargs=[])
subcircuit.append(ZGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(CXGate(), qargs=[qr[2], qr[3]], cargs=[])
subcircuit.append(UGate(5.01836135520768, 5.190931186022931, 1.2128092629174942), qargs=[qr[3]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: QASM_CONVERSION

qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0,
    1], [0, 2], [1, 0], [1, 3], [1, 4], [2, 0], [3, 1], [4, 1]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_1d82ff79f11e4d4f81970273e715ff32 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_1d82ff79f11e4d4f81970273e715ff32, shots=979).result().get_counts(qc)
RESULT = counts
