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
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(DCXGate(), qargs=[qr[1], qr[4]], cargs=[])
subcircuit.append(CPhaseGate(1.6161683469432118), qargs=[qr[1], qr[4]], cargs=[])
subcircuit.append(RXGate(6.033961191253911), qargs=[qr[1]], cargs=[])
subcircuit.append(ZGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(CXGate(), qargs=[qr[2], qr[3]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(ECRGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CRXGate(2.0099472182748075), qargs=[qr[4], qr[3]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_fe7412bb4896402d953105458b85780b = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_fe7412bb4896402d953105458b85780b, shots=979).result().get_counts(qc)
RESULT = counts
