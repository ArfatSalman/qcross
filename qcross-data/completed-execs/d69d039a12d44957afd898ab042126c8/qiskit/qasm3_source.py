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
qc.append(RZGate(6.163759533339787), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[3]], cargs=[])
qc.append(CRXGate(2.0099472182748075), qargs=[qr[2], qr[5]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[6], qr[0], qr[1], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[4], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[2], qr[1], qr[5]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CU3Gate(1.2827690425732097,1.3283826543858017,3.672121211148789), qargs=[qr[2], qr[6]], cargs=[])
subcircuit.append(CU3Gate(3.865496458458116,2.6636908506222836,6.221353754875494), qargs=[qr[5], qr[0]], cargs=[])
subcircuit.append(U1Gate(6.2047416485134805), qargs=[qr[0]], cargs=[])
subcircuit.append(TGate(), qargs=[qr[6]], cargs=[])
subcircuit.append(SXGate(), qargs=[qr[4]], cargs=[])
subcircuit.append(C3XGate(5.94477504571567), qargs=[qr[4], qr[6], qr[2], qr[1]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(ECRGate(), qargs=[qr[6], qr[3]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: QASM_CONVERSION


from qiskit.qasm3 import loads, dumps
qc = loads(dumps(qc))

# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_87f34e08fa084b6691a6737731175e48 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_87f34e08fa084b6691a6737731175e48, shots=1959).result().get_counts(qc)
RESULT = counts
