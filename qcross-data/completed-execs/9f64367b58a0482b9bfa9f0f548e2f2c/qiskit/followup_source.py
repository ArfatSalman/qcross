# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_d09701 = Parameter('p_d09701')
p_8dd582 = Parameter('p_8dd582')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(p_d09701), qargs=[qr[3]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[2]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CRXGate(p_8dd582), qargs=[qr[4], qr[3]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(TGate(), qargs=[qr[2]], cargs=[])
subcircuit.append(UGate(5.01836135520768,5.190931186022931,1.2128092629174942), qargs=[qr[3]], cargs=[])
subcircuit.append(RC3XGate(), qargs=[qr[4], qr[0], qr[3], qr[1]], cargs=[])
subcircuit.append(DCXGate(), qargs=[qr[2], qr[3]], cargs=[])
subcircuit.append(CZGate(), qargs=[qr[1], qr[0]], cargs=[])
subcircuit.append(CUGate(4.229610589867865,2.696266694818697,5.631160518436971,2.9151388486514547), qargs=[qr[0], qr[1]], cargs=[])
subcircuit.append(CPhaseGate(4.63837786161633), qargs=[qr[0], qr[2]], cargs=[])
subcircuit.append(ECRGate(), qargs=[qr[3], qr[1]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CRZGate(1.0296448789776642), qargs=[qr[3], qr[4]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_d09701: 6.163759533339787, p_8dd582: 2.0099472182748075})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 4], [0, 6], [1, 0], [1, 2], [2, 1], [3, 6], [4, 0], [4, 5], [5, 4], [6, 0], [6, 3]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_d9165ea61332486ba7c3013706530320 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_d9165ea61332486ba7c3013706530320, shots=979).result().get_counts(qc)
RESULT = counts
