# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS
# SECTION
# NAME: PARAMETERS
p_e49507 = Parameter('p_e49507')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(CRYGate(p_e49507), qargs=[qr[6], qr[8]], cargs=[])
qc.append(IGate(), qargs=[qr[3]], cargs=[])
qc.append(CSwapGate(), qargs=[qr[1], qr[9], qr[5]], cargs=[])
qc.append(CCXGate(), qargs=[qr[4], qr[5], qr[9]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(CCXGate(), qargs=[qr[3], qr[7], qr[5]], cargs=[])
qc.append(CHGate(), qargs=[qr[5], qr[6]], cargs=[])
qc.append(CCXGate(), qargs=[qr[2], qr[9], qr[3]], cargs=[])
qc.append(RXXGate(2.538800093380569), qargs=[qr[3], qr[5]], cargs=[])
qc.append(CCZGate(), qargs=[qr[1], qr[2], qr[6]], cargs=[])
qc.append(CRYGate(0.4048520184170855), qargs=[qr[6], qr[3]], cargs=[])
qc.append(ECRGate(), qargs=[qr[4], qr[5]], cargs=[])
qc.append(CCZGate(), qargs=[qr[3], qr[8], qr[5]], cargs=[])
qc.append(CXGate(), qargs=[qr[9], qr[7]], cargs=[])# SECTION
# NAME: USELESS_ENTITIES

qr_a1931a = QuantumRegister(5, name='qr_a1931a')
qc.add_register(qr_a1931a)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_e49507: 3.2352192519602734,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=['ccx', 'h'], optimization_level=0, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_3678e0c4d511416ab466d145715d3746 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_3678e0c4d511416ab466d145715d3746, shots=5542).result().get_counts(qc)
RESULT = counts
