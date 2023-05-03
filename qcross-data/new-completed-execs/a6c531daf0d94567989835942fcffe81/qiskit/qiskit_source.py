
# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter

# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(7, name='qr')
cr = ClassicalRegister(7, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(U3Gate(1.2333979366062962,0.8994966515664887,3.0003132360957094), qargs=[qr[1]], cargs=[])
qc.append(SwapGate(), qargs=[qr[5], qr[0]], cargs=[])
qc.append(CU1Gate(5.8809885406034885), qargs=[qr[4], qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[3]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(CPhaseGate(4.661904537785083), qargs=[qr[4], qr[6]], cargs=[])
qc.append(U3Gate(6.161570642375718,0.7126827811277849,1.428988687288719), qargs=[qr[5]], cargs=[])
qc.append(CRZGate(2.777640838880794), qargs=[qr[0], qr[3]], cargs=[])
qc.append(SwapGate(), qargs=[qr[0], qr[4]], cargs=[])
qc.append(SXGate(), qargs=[qr[2]], cargs=[])
qc.append(U2Gate(1.9012707343238924,6.017351377795965), qargs=[qr[3]], cargs=[])
qc.append(U2Gate(1.3178440304272925,3.434672943879739), qargs=[qr[3]], cargs=[])
qc.append(DCXGate(), qargs=[qr[1], qr[6]], cargs=[])
qc.append(U3Gate(2.0260584085672413,5.46425242678673,4.443597328220221), qargs=[qr[5]], cargs=[])
qc.append(DCXGate(), qargs=[qr[4], qr[1]], cargs=[])
qc.append(CXGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(CRXGate(0.47168664474085104), qargs=[qr[4], qr[2]], cargs=[])
qc.append(PhaseGate(5.273838382452584), qargs=[qr[3]], cargs=[])
qc.append(PhaseGate(0.6110285192622922), qargs=[qr[5]], cargs=[])

# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=None)

# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_9eb69bb03b544e7181436be83fc8548f = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_9eb69bb03b544e7181436be83fc8548f, shots=1959).result().get_counts(qc)
RESULT = counts