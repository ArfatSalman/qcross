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
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(RZGate(6.163759533339787), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[3]], cargs=[])
qc.append(CRXGate(2.0099472182748075), qargs=[qr[2], qr[5]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[6], qr[0], qr[1], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[4], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[2], qr[1], qr[5]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(ECRGate(), qargs=[qr[6], qr[3]], cargs=[])
qc.append(SdgGate(), qargs=[qr[6]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[2], qr[5], qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[1]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[2], qr[1], qr[3]], cargs=[])
qc.append(CU1Gate(3.2142159669963557), qargs=[qr[4], qr[0]], cargs=[])
qc.append(CRXGate(5.94477504571567), qargs=[qr[4], qr[6]], cargs=[])
qc.append(CHGate(), qargs=[qr[4], qr[0]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[0], qr[3], qr[4]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[5]], cargs=[])
qc.append(CRZGate(4.833923139882297), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CU1Gate(4.028174522740928), qargs=[qr[1], qr[4]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[0], qr[5], qr[4]], cargs=[])
qc.append(CRZGate(2.586208953975239), qargs=[qr[6], qr[2]], cargs=[])
qc.append(U2Gate(2.5163050709890156, 2.1276323672732023), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[6]], cargs=[])
qc.append(SdgGate(), qargs=[qr[0]], cargs=[])
qc.append(RZZGate(3.950837470808744), qargs=[qr[3], qr[4]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
qc.append(RYYGate(1.9669252191306448), qargs=[qr[4], qr[2]], cargs=[])
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
qc = transpile(qc, basis_gates=['ccx', 'h'], optimization_level=2,
    coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_43e42e4d89ac447c85d1923d00119dea = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_43e42e4d89ac447c85d1923d00119dea, shots=1959).result().get_counts(qc)
RESULT = counts
