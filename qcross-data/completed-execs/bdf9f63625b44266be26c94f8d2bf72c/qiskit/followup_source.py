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
p_d40aec = Parameter('p_d40aec')
p_10c631 = Parameter('p_10c631')
p_a7734b = Parameter('p_a7734b')
p_c8b7aa = Parameter('p_c8b7aa')
p_8f9e53 = Parameter('p_8f9e53')
p_da6dd8 = Parameter('p_da6dd8')
p_7f634a = Parameter('p_7f634a')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(7, name='qr')
cr = ClassicalRegister(7, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_da6dd8), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[3]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CYGate(), qargs=[qr[2], qr[0]], cargs=[])
subcircuit.append(SXGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(CRZGate(p_7f634a), qargs=[qr[0], qr[5]], cargs=[])
subcircuit.append(CSXGate(), qargs=[qr[4], qr[0]], cargs=[])
subcircuit.append(SwapGate(), qargs=[qr[1], qr[4]], cargs=[])
subcircuit.append(RYYGate(p_a7734b), qargs=[qr[2], qr[0]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CRXGate(p_c8b7aa), qargs=[qr[2], qr[5]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[6], qr[0], qr[1], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[4], qr[6]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[2], qr[1], qr[5]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(ECRGate(), qargs=[qr[6], qr[3]], cargs=[])
qc.append(SdgGate(), qargs=[qr[6]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[2], qr[5], qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[1]], cargs=[])
qc.append(RZGate(p_10c631), qargs=[qr[1]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[0], qr[2], qr[1], qr[3]], cargs=[])
qc.append(CU1Gate(p_d40aec), qargs=[qr[4], qr[0]], cargs=[])
qc.append(CRXGate(p_8f9e53), qargs=[qr[4], qr[6]], cargs=[])
qc.append(CHGate(), qargs=[qr[4], qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_d40aec: 3.2142159669963557,
    p_10c631: 4.229610589867865,
    p_a7734b: 0.5501056885328758,
    p_c8b7aa: 2.0099472182748075,
    p_8f9e53: 5.94477504571567,
    p_da6dd8: 6.163759533339787,
    p_7f634a: 2.008796895454228,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_7d22843efb8b41a881049caee64182ec = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_7d22843efb8b41a881049caee64182ec, shots=1959).result().get_counts(qc)
RESULT = counts
