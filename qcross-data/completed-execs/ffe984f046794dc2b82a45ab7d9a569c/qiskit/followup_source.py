# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS
# SECTION
# NAME: PARAMETERS
p_fa5922 = Parameter('p_fa5922')
p_1464bc = Parameter('p_1464bc')
p_03ad92 = Parameter('p_03ad92')
p_d5daad = Parameter('p_d5daad')
p_72766f = Parameter('p_72766f')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(7, name='qr')
cr = ClassicalRegister(7, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[3]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(HGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(RZZGate(p_03ad92), qargs=[qr[0], qr[5]], cargs=[])
subcircuit.append(CRZGate(p_1464bc), qargs=[qr[0], qr[5]], cargs=[])
subcircuit.append(CSXGate(), qargs=[qr[4], qr[0]], cargs=[])
subcircuit.append(SwapGate(), qargs=[qr[1], qr[4]], cargs=[])
subcircuit.append(RYYGate(0.5501056885328758), qargs=[qr[2], qr[0]], cargs=[])
subcircuit.append(SXdgGate(), qargs=[qr[5]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CRXGate(p_d5daad), qargs=[qr[2], qr[5]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[6], qr[0], qr[1], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[4], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[2], qr[1], qr[5]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(ECRGate(), qargs=[qr[6], qr[3]], cargs=[])
qc.append(SdgGate(), qargs=[qr[6]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[2], qr[5], qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[1]], cargs=[])
qc.append(RZGate(p_fa5922), qargs=[qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[2], qr[1], qr[3]], cargs=[])
qc.append(CU1Gate(p_72766f), qargs=[qr[4], qr[0]], cargs=[])
qc.append(CRXGate(5.94477504571567), qargs=[qr[4], qr[6]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_fa5922: 4.229610589867865,
    p_1464bc: 2.008796895454228,
    p_03ad92: 5.017245588344839,
    p_d5daad: 2.0099472182748075,
    p_72766f: 3.2142159669963557,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_1a35c34e979e47aaa732a6c862480815 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_1a35c34e979e47aaa732a6c862480815, shots=1959).result().get_counts(qc)
RESULT = counts
