# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: PARAMETERS

p_5a7038 = Parameter('p_5a7038')
p_7d6e79 = Parameter('p_7d6e79')
p_9f724d = Parameter('p_9f724d')
p_e94aea = Parameter('p_e94aea')
p_52b317 = Parameter('p_52b317')
p_320da9 = Parameter('p_320da9')
p_2b203d = Parameter('p_2b203d')
p_334c70 = Parameter('p_334c70')
p_94dcf5 = Parameter('p_94dcf5')
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(6, name='qr')
cr = ClassicalRegister(6, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(RZGate(p_2b203d), qargs=[qr[2]], cargs=[])
subcircuit.append(TGate(), qargs=[qr[1]], cargs=[])
subcircuit.append(CUGate(p_320da9, p_52b317, 5.631160518436971, p_7d6e79), qargs=[qr[0], qr[3]], cargs=[])
subcircuit.append(TGate(), qargs=[qr[2]], cargs=[])
subcircuit.append(RZXGate(p_334c70), qargs=[qr[4], qr[0]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(RZGate(6.163759533339787), qargs=[qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(p_94dcf5), qargs=[qr[2], qr[4]], cargs=[])
qc.append(CUGate(p_9f724d, p_e94aea, p_5a7038, 5.987304452123941), qargs=[qr[2], qr[3]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[1], qr[4], qr[0], qr[2]], cargs=[])
qc.append(CCXGate(), qargs=[qr[1], qr[5], qr[0]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[4], qr[3], qr[5], qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[4]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[5], qr[3], qr[4]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: PARAMETER_BINDING

qc = qc.bind_parameters({p_5a7038: 2.3864521352475245, p_7d6e79: 2.9151388486514547, p_9f724d: 0.5112149185250571, p_e94aea: 5.897054719225356, p_52b317: 2.696266694818697, p_320da9: 4.229610589867865, p_2b203d: 3.672121211148789, p_334c70: 4.563562108824195, p_94dcf5: 4.2641612072511235})
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: QASM_CONVERSION
qc = QuantumCircuit.from_qasm_str(qc.qasm())
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_0aff2fac769e4ad9b21c82b362b87241 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_0aff2fac769e4ad9b21c82b362b87241, shots=1385).result().get_counts(qc)
RESULT = counts
