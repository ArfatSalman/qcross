# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_d5e26f = Parameter('p_d5e26f')
p_90ec67 = Parameter('p_90ec67')
p_263cbf = Parameter('p_263cbf')
p_3818c9 = Parameter('p_3818c9')
p_5671c2 = Parameter('p_5671c2')
p_3be06b = Parameter('p_3be06b')
p_1d1ce1 = Parameter('p_1d1ce1')
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_d5e26f), qargs=[qr[1]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[4]], cargs=[])
qc.append(CSXGate(), qargs=[qr[3], qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[1], qr[4]], cargs=[])
qc.append(CRXGate(2.0099472182748075), qargs=[qr[2], qr[1]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(CRZGate(1.0296448789776642), qargs=[qr[1], qr[2]], cargs=[])
qc.append(CHGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(RYYGate(p_3818c9), qargs=[qr[0], qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[4]], cargs=[])
qc.append(TGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[2]], cargs=[])
qc.append(CUGate(p_263cbf, 4.167661441102218, 4.623446645668956, 
    3.865496458458116), qargs=[qr[3], qr[2]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[3]], cargs=[])
qc.append(RYYGate(p_90ec67), qargs=[qr[0], qr[4]], cargs=[])
qc.append(CU1Gate(p_1d1ce1), qargs=[qr[1], qr[0]], cargs=[])
qc.append(UGate(5.887184334931191, p_3be06b, p_5671c2), qargs=[qr[2]], cargs=[]
    )
qc.append(CHGate(), qargs=[qr[4], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_d5e26f: 6.163759533339787, p_90ec67: 5.398622178940033, p_263cbf: 5.708725119517347, p_3818c9: 1.6723037552953224, p_5671c2: 1.4112277317699358, p_3be06b: 0.07157463504881167, p_1d1ce1: 3.2142159669963557})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_261e889a659b4e66b742e1702d1c691d = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_261e889a659b4e66b742e1702d1c691d, shots=979).result().get_counts(qc)
RESULT = counts
