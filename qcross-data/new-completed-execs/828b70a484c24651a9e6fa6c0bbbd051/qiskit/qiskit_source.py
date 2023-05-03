
# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter

# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(7, name='qr')
cr = ClassicalRegister(7, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RYYGate(0.1584650651944304), qargs=[qr[1], qr[2]], cargs=[])
qc.append(YGate(), qargs=[qr[2]], cargs=[])
qc.append(RXGate(1.9643059251773882), qargs=[qr[6]], cargs=[])
qc.append(CRXGate(2.2091452154672204), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CUGate(5.28444061678252,2.26438130892656,4.508815818648728,5.843141721322287), qargs=[qr[4], qr[0]], cargs=[])
qc.append(RXGate(2.316480646141322), qargs=[qr[1]], cargs=[])
qc.append(RZXGate(1.7530034337193163), qargs=[qr[0], qr[4]], cargs=[])
qc.append(CU1Gate(2.75818719037007), qargs=[qr[4], qr[1]], cargs=[])
qc.append(HGate(), qargs=[qr[0]], cargs=[])
qc.append(CSwapGate(), qargs=[qr[0], qr[4], qr[5]], cargs=[])
qc.append(HGate(), qargs=[qr[2]], cargs=[])
qc.append(CU3Gate(0.29341892717166834,6.249908353941511,2.9247183841853848), qargs=[qr[4], qr[3]], cargs=[])
qc.append(RYGate(3.70789888536151), qargs=[qr[5]], cargs=[])
qc.append(CYGate(), qargs=[qr[5], qr[0]], cargs=[])
qc.append(CZGate(), qargs=[qr[3], qr[6]], cargs=[])
qc.append(CSGate(), qargs=[qr[3], qr[0]], cargs=[])
qc.append(CSwapGate(), qargs=[qr[2], qr[5], qr[4]], cargs=[])
qc.append(SXGate(), qargs=[qr[1]], cargs=[])
qc.append(HGate(), qargs=[qr[2]], cargs=[])
qc.append(CRXGate(2.360789071411234), qargs=[qr[3], qr[4]], cargs=[])
qc.append(CZGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(RXGate(2.191505539211396), qargs=[qr[3]], cargs=[])
qc.append(RYYGate(0.39681210536068023), qargs=[qr[1], qr[4]], cargs=[])
qc.append(CYGate(), qargs=[qr[4], qr[5]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(YGate(), qargs=[qr[0]], cargs=[])
qc.append(CU3Gate(5.928213929259535,1.0062255952575803,2.115561623846294), qargs=[qr[5], qr[2]], cargs=[])
qc.append(CYGate(), qargs=[qr[1], qr[6]], cargs=[])
qc.append(CZGate(), qargs=[qr[3], qr[0]], cargs=[])
qc.append(ECRGate(), qargs=[qr[2], qr[4]], cargs=[])

# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=3, coupling_map=None)

# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_21955a8b91af405c9f7acaa497e0a4ff = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_21955a8b91af405c9f7acaa497e0a4ff, shots=1959).result().get_counts(qc)
RESULT = counts