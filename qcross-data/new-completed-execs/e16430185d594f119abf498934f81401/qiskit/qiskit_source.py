
# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter

# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(8, name='qr')
cr = ClassicalRegister(8, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(ECRGate(), qargs=[qr[1], qr[7]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[1], qr[0], qr[5], qr[6]], cargs=[])
qc.append(CPhaseGate(0.7207706407070019), qargs=[qr[4], qr[3]], cargs=[])
qc.append(DCXGate(), qargs=[qr[3], qr[4]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[2], qr[1], qr[4]], cargs=[])
qc.append(SwapGate(), qargs=[qr[6], qr[5]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[4], qr[7]], cargs=[])
qc.append(RXGate(4.802467793465571), qargs=[qr[0]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[0], qr[5]], cargs=[])
qc.append(CU1Gate(3.4625444838065618), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CSwapGate(), qargs=[qr[0], qr[3], qr[6]], cargs=[])
qc.append(RGate(5.104156300804455,6.227137798959555), qargs=[qr[0]], cargs=[])
qc.append(TGate(), qargs=[qr[5]], cargs=[])
qc.append(RXXGate(6.256338963756067), qargs=[qr[1], qr[5]], cargs=[])
qc.append(DCXGate(), qargs=[qr[7], qr[6]], cargs=[])
qc.append(RYGate(2.803631472128793), qargs=[qr[3]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[4], qr[3], qr[1], qr[2]], cargs=[])
qc.append(CU1Gate(1.5456697172063534), qargs=[qr[7], qr[6]], cargs=[])
qc.append(RYGate(4.278284783932528), qargs=[qr[7]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[7], qr[2], qr[0]], cargs=[])
qc.append(RGate(0.2852105385229711,5.142516617776941), qargs=[qr[2]], cargs=[])
qc.append(RXXGate(2.2028067729502347), qargs=[qr[1], qr[6]], cargs=[])
qc.append(RXGate(1.732522506962926), qargs=[qr[7]], cargs=[])
qc.append(CCXGate(), qargs=[qr[5], qr[1], qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[3]], cargs=[])
qc.append(IGate(), qargs=[qr[3]], cargs=[])

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
backend_60af6325ceea4641ad221d3b809f1658 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_60af6325ceea4641ad221d3b809f1658, shots=2771).result().get_counts(qc)
RESULT = counts