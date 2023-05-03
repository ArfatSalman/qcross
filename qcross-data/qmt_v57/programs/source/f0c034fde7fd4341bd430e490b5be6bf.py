
# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter

# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(YGate(), qargs=[qr[8]], cargs=[])
qc.append(CU3Gate(1.137265035582176,1.9191341652886187,2.035659400824786), qargs=[qr[2], qr[5]], cargs=[])
qc.append(ECRGate(), qargs=[qr[4], qr[1]], cargs=[])
qc.append(HGate(), qargs=[qr[8]], cargs=[])
qc.append(CRZGate(5.5072773697390085), qargs=[qr[5], qr[0]], cargs=[])
qc.append(RXGate(4.368068524516866), qargs=[qr[9]], cargs=[])
qc.append(CZGate(), qargs=[qr[6], qr[1]], cargs=[])
qc.append(SdgGate(), qargs=[qr[7]], cargs=[])
qc.append(CRYGate(4.03209544447551), qargs=[qr[1], qr[4]], cargs=[])
qc.append(SwapGate(), qargs=[qr[9], qr[2]], cargs=[])
qc.append(YGate(), qargs=[qr[9]], cargs=[])
qc.append(SwapGate(), qargs=[qr[0], qr[8]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[3]], cargs=[])
qc.append(ECRGate(), qargs=[qr[3], qr[7]], cargs=[])
qc.append(DCXGate(), qargs=[qr[9], qr[1]], cargs=[])
qc.append(CCXGate(), qargs=[qr[8], qr[2], qr[3]], cargs=[])
qc.append(YGate(), qargs=[qr[7]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[7], qr[3], qr[5], qr[1]], cargs=[])
qc.append(U3Gate(1.6951114914418934,5.599301713249363,3.1864266503972143), qargs=[qr[4]], cargs=[])
qc.append(RXGate(5.528457770513217), qargs=[qr[7]], cargs=[])
qc.append(C3SXGate(), qargs=[qr[2], qr[6], qr[1], qr[7]], cargs=[])
qc.append(CSwapGate(), qargs=[qr[9], qr[3], qr[1]], cargs=[])
qc.append(RZZGate(3.5190638597992265), qargs=[qr[8], qr[5]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[6]], cargs=[])
qc.append(HGate(), qargs=[qr[6]], cargs=[])
qc.append(RZXGate(3.656646631785722), qargs=[qr[0], qr[9]], cargs=[])
qc.append(HGate(), qargs=[qr[3]], cargs=[])
qc.append(XGate(), qargs=[qr[7]], cargs=[])

# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)

# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_e446145f36cc4d908b5e15c7b8c1e90c = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_e446145f36cc4d908b5e15c7b8c1e90c, shots=5542).result().get_counts(qc)
RESULT = counts