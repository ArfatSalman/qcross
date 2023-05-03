
# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter

# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(6, name='qr')
cr = ClassicalRegister(6, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RXGate(0.6650027350645848), qargs=[qr[5]], cargs=[])
qc.append(SdgGate(), qargs=[qr[0]], cargs=[])
qc.append(CYGate(), qargs=[qr[0], qr[4]], cargs=[])
qc.append(RVGate(4.207878413680952,0.3009231473653096,1.580343691421699), qargs=[qr[4]], cargs=[])
qc.append(CPhaseGate(3.9206722628490542), qargs=[qr[5], qr[2]], cargs=[])
qc.append(CPhaseGate(3.397598873029434), qargs=[qr[2], qr[3]], cargs=[])
qc.append(IGate(), qargs=[qr[4]], cargs=[])
qc.append(U2Gate(4.855299131904333,3.1272609413923482), qargs=[qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(RXXGate(0.7249247820191558), qargs=[qr[3], qr[4]], cargs=[])
qc.append(TdgGate(), qargs=[qr[5]], cargs=[])
qc.append(IGate(), qargs=[qr[1]], cargs=[])
qc.append(CXGate(), qargs=[qr[4], qr[1]], cargs=[])
qc.append(IGate(), qargs=[qr[5]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[5], qr[2], qr[4], qr[3]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[5], qr[2], qr[4], qr[0]], cargs=[])
qc.append(RXXGate(2.6498953828086473), qargs=[qr[2], qr[4]], cargs=[])
qc.append(CYGate(), qargs=[qr[5], qr[2]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(HGate(), qargs=[qr[4]], cargs=[])
qc.append(SdgGate(), qargs=[qr[3]], cargs=[])
qc.append(ECRGate(), qargs=[qr[0], qr[5]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])

# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=3, coupling_map=None)

# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_8bd842256c2a4550bcc42fdd1a98cf5f = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_8bd842256c2a4550bcc42fdd1a98cf5f, shots=1385).result().get_counts(qc)
RESULT = counts