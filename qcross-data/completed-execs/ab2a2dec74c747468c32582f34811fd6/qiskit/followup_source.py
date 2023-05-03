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
p_219d62 = Parameter('p_219d62')
p_f67f84 = Parameter('p_f67f84')
p_b9edf2 = Parameter('p_b9edf2')
p_cac0af = Parameter('p_cac0af')
p_c04ae3 = Parameter('p_c04ae3')
p_7ec521 = Parameter('p_7ec521')

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_c04ae3), qargs=[qr[3]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CRXGate(2.0099472182748075), qargs=[qr[4], qr[3]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(CRZGate(1.0296448789776642), qargs=[qr[3], qr[4]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[4]], cargs=[])
qc.append(RYYGate(p_219d62), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CU1Gate(p_cac0af), qargs=[qr[2], qr[4]], cargs=[])
subcircuit.append(CU3Gate(p_b9edf2, 2.6636908506222836, 6.221353754875494),
    qargs=[qr[4], qr[1]], cargs=[])
subcircuit.append(IGate(), qargs=[qr[1]], cargs=[])
subcircuit.append(IGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(ECRGate(), qargs=[qr[3], qr[1]], cargs=[])
subcircuit.append(UGate(p_7ec521, 2.3568871696687452, 6.011900464835247),
    qargs=[qr[2]], cargs=[])
subcircuit.append(CSwapGate(), qargs=[qr[0], qr[4], qr[1]], cargs=[])
subcircuit.append(HGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(CRXGate(p_f67f84), qargs=[qr[2], qr[0]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CSXGate(), qargs=[qr[1], qr[4]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({
    p_219d62: 1.6723037552953224,
    p_f67f84: 5.091930552861214,
    p_b9edf2: 3.865496458458116,
    p_cac0af: 4.501598818751339,
    p_c04ae3: 6.163759533339787,
    p_7ec521: 3.5173414605326783,
})

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_1dc0f243c0124cec8b01873035f80526 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_1dc0f243c0124cec8b01873035f80526, shots=979).result().get_counts(qc)
RESULT = counts
