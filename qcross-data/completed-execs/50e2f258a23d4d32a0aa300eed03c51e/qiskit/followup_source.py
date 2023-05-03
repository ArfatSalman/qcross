# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_7268fa = Parameter('p_7268fa')
p_1ced18 = Parameter('p_1ced18')
p_943f31 = Parameter('p_943f31')
p_7168a9 = Parameter('p_7168a9')
p_d46b4e = Parameter('p_d46b4e')
p_cc0d68 = Parameter('p_cc0d68')
p_a7ec6e = Parameter('p_a7ec6e')
p_a346be = Parameter('p_a346be')
p_165b3b = Parameter('p_165b3b')
p_ea9bf0 = Parameter('p_ea9bf0')
p_e30407 = Parameter('p_e30407')
p_29d856 = Parameter('p_29d856')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_7268fa), qargs=[qr[3]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(SwapGate(), qargs=[qr[4], qr[0]], cargs=[])
subcircuit.append(CRYGate(3.1402006997068588), qargs=[qr[2], qr[0]], cargs=[])
subcircuit.append(CUGate(5.0063780207098425, 3.1562533916051736, 4.940217775579305, 2.419481683937988), qargs=[qr[2], qr[1]], cargs=[])
subcircuit.append(C3XGate(2.6687018103754414), qargs=[qr[3], qr[4], qr[2], qr[0]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(ECRGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CRXGate(p_cc0d68), qargs=[qr[4], qr[3]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(CRZGate(p_d46b4e), qargs=[qr[3], qr[4]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[4]], cargs=[])
qc.append(RYYGate(p_165b3b), qargs=[qr[0], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[4]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[4]], cargs=[])
qc.append(CUGate(p_943f31, p_1ced18, p_a7ec6e, p_e30407), qargs=[qr[1], qr[4]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(p_29d856), qargs=[qr[0], qr[2]], cargs=[])
qc.append(CU1Gate(p_7168a9), qargs=[qr[3], qr[0]], cargs=[])
qc.append(UGate(p_ea9bf0, p_a346be, 1.4112277317699358), qargs=[qr[4]], cargs=[])
qc.append(CHGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_7268fa: 6.163759533339787, p_1ced18: 4.167661441102218, p_943f31: 5.708725119517347, p_7168a9: 3.2142159669963557, p_d46b4e: 1.0296448789776642, p_cc0d68: 2.0099472182748075, p_a7ec6e: 4.623446645668956, p_a346be: 0.07157463504881167, p_165b3b: 1.6723037552953224, p_ea9bf0: 5.887184334931191, p_e30407: 3.865496458458116, p_29d856: 5.398622178940033})
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0,
    1], [0, 2], [0, 4], [1, 0], [1, 3], [2, 0], [3, 1], [4, 0]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_21fdd4b5f157429da75d614c0efb55ad = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_21fdd4b5f157429da75d614c0efb55ad, shots=979).result().get_counts(qc)
RESULT = counts
