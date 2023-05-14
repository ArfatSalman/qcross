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
p_4534a2 = Parameter('p_4534a2')
p_c28457 = Parameter('p_c28457')
p_88080a = Parameter('p_88080a')
p_089fca = Parameter('p_089fca')
p_0aa97a = Parameter('p_0aa97a')
p_f1630e = Parameter('p_f1630e')
p_a25c71 = Parameter('p_a25c71')
p_63f494 = Parameter('p_63f494')
p_4537df = Parameter('p_4537df')
p_cab727 = Parameter('p_cab727')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_88080a), qargs=[qr[3]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(RZXGate(p_cab727), qargs=[qr[0], qr[6]], cargs=[])
subcircuit.append(UGate(p_4534a2, p_0aa97a, p_c28457), qargs=[qr[5]], cargs=[])
subcircuit.append(ZGate(), qargs=[qr[2]], cargs=[])
subcircuit.append(UGate(p_63f494, 5.190931186022931, p_4537df), qargs=[qr[4
    ]], cargs=[])
subcircuit.append(DCXGate(), qargs=[qr[1], qr[8]], cargs=[])
subcircuit.append(CUGate(p_f1630e, p_a25c71, 5.631160518436971, 
    2.9151388486514547), qargs=[qr[0], qr[9]], cargs=[])
subcircuit.append(ECRGate(), qargs=[qr[9], qr[0]], cargs=[])
subcircuit.append(C3XGate(p_089fca), qargs=[qr[6], qr[4], qr[8], qr[9]],
    cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CRZGate(4.2641612072511235), qargs=[qr[6], qr[3]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_4534a2: 2.6397681660693015,
    p_c28457: 3.427505621225153,
    p_88080a: 6.163759533339787,
    p_089fca: 5.94477504571567,
    p_0aa97a: 5.320621737498446,
    p_f1630e: 4.229610589867865,
    p_a25c71: 2.696266694818697,
    p_63f494: 5.01836135520768,
    p_4537df: 1.2128092629174942,
    p_cab727: 0.6833824466861163,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_24db24df9f5a4680971b65bea56c88a0 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_24db24df9f5a4680971b65bea56c88a0, shots=5542).result().get_counts(qc)
RESULT = counts
