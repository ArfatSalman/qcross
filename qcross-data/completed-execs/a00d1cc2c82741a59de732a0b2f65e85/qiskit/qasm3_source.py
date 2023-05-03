# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_1b0063 = Parameter('p_1b0063')
p_43b9a6 = Parameter('p_43b9a6')
p_831b02 = Parameter('p_831b02')
p_0584aa = Parameter('p_0584aa')
p_40c0da = Parameter('p_40c0da')
p_d34f58 = Parameter('p_d34f58')
p_aed827 = Parameter('p_aed827')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_831b02), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_0584aa), qargs=[qr[6], qr[3]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(RZXGate(1.1412693567569159), qargs=[qr[1], qr[8]], cargs=[])
subcircuit.append(SwapGate(), qargs=[qr[1], qr[7]], cargs=[])
subcircuit.append(iSwapGate(), qargs=[qr[2], qr[7]], cargs=[])
subcircuit.append(RCCXGate(), qargs=[qr[2], qr[0], qr[5]], cargs=[])
subcircuit.append(CUGate(2.862865991712737,6.0504088665633065,1.7203758404994713,2.8704483107274004), qargs=[qr[3], qr[1]], cargs=[])
subcircuit.append(CXGate(), qargs=[qr[8], qr[9]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CRXGate(p_d34f58), qargs=[qr[1], qr[7]], cargs=[])
qc.append(CCXGate(), qargs=[qr[5], qr[9], qr[7]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[9]], cargs=[])
qc.append(XGate(), qargs=[qr[8]], cargs=[])
qc.append(CRZGate(4.167661441102218), qargs=[qr[1], qr[6]], cargs=[])
qc.append(RZGate(p_43b9a6), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[4], qr[8]], cargs=[])
qc.append(CCXGate(), qargs=[qr[4], qr[9], qr[5]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[4], qr[0], qr[9]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[7], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(CRZGate(p_1b0063), qargs=[qr[1], qr[2]], cargs=[])
qc.append(U2Gate(p_aed827, p_40c0da), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[0]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[9]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_1b0063: 2.586208953975239, p_43b9a6: 4.229610589867865, p_831b02: 6.163759533339787, p_0584aa: 4.2641612072511235, p_40c0da: 2.1276323672732023, p_d34f58: 5.987304452123941, p_aed827: 2.5163050709890156})
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
backend_98d1cbf483f54991a09b8f68d5f632ed = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_98d1cbf483f54991a09b8f68d5f632ed, shots=5542).result().get_counts(qc)
RESULT = counts
