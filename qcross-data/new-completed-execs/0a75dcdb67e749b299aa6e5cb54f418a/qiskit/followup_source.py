# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(4, name='qr')
cr = ClassicalRegister(4, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(SdgGate(), qargs=[qr[3]], cargs=[])
qc.append(DCXGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CYGate(), qargs=[qr[0], qr[3]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[3], qr[0], qr[2], qr[1]], cargs=[])
qc.append(CUGate(0.9157606983245934, 5.397500370041537, 3.7108393874093117, 3.651689382779405), qargs=[qr[1], qr[2]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[0], qr[1], qr[3]], cargs=[])
qc.append(CSdgGate(), qargs=[qr[1], qr[3]], cargs=[])
qc.append(DCXGate(), qargs=[qr[3], qr[0]], cargs=[])
qc.append(RZXGate(1.7115424816079432), qargs=[qr[0], qr[3]], cargs=[])
qc.append(RZXGate(1.6486589761943145), qargs=[qr[2], qr[0]], cargs=[])
qc.append(C3XGate(), qargs=[qr[0], qr[2], qr[3], qr[1]], cargs=[])
qc.append(RYYGate(4.794877298046951), qargs=[qr[0], qr[1]], cargs=[])
qc.append(RZXGate(3.4346411253220106), qargs=[qr[3], qr[1]], cargs=[])
qc.append(RYYGate(6.102373854375312), qargs=[qr[3], qr[2]], cargs=[])
qc.append(CU3Gate(2.6976815284019784, 0.9310317943034069, 1.8906179385735775), qargs=[qr[3], qr[0]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(RYGate(3.2534282040977613), qargs=[qr[2]], cargs=[])
subcircuit.append(DCXGate(), qargs=[qr[3], qr[2]], cargs=[])
subcircuit.append(ECRGate(), qargs=[qr[1], qr[2]], cargs=[])
subcircuit.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(IGate(), qargs=[qr[0]], cargs=[])
qc.append(UGate(5.176714778665683, 0.30607591346008556, 0.8506581770011129), qargs=[qr[3]], cargs=[])
qc.append(C3XGate(), qargs=[qr[2], qr[1], qr[3], qr[0]], cargs=[])
qc.append(UGate(2.478741058575176, 4.422282188870415, 4.889199801305671), qargs=[qr[1]], cargs=[])# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=['ccx', 'h'], optimization_level=1, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_2bbd7ec41abc4975badc01f7d72831db = Aer.get_backend('aer_simulator')
counts = execute(qc, backend=backend_2bbd7ec41abc4975badc01f7d72831db, shots=692).result().get_counts(qc)
RESULT = counts
