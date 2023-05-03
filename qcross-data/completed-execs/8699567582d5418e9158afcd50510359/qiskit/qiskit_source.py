
# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter

# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(CYGate(), qargs=[qr[0], qr[6]], cargs=[])
qc.append(U1Gate(3.321288277959951), qargs=[qr[2]], cargs=[])
qc.append(YGate(), qargs=[qr[3]], cargs=[])
qc.append(ECRGate(), qargs=[qr[5], qr[1]], cargs=[])
qc.append(RZGate(3.0238378046938514), qargs=[qr[6]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[3], qr[6]], cargs=[])
qc.append(ECRGate(), qargs=[qr[4], qr[3]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[2], qr[5], qr[3]], cargs=[])
qc.append(SdgGate(), qargs=[qr[1]], cargs=[])
qc.append(PhaseGate(0.2289483555541983), qargs=[qr[3]], cargs=[])
qc.append(CYGate(), qargs=[qr[5], qr[7]], cargs=[])
qc.append(PhaseGate(4.268329737032283), qargs=[qr[4]], cargs=[])
qc.append(CSwapGate(), qargs=[qr[2], qr[3], qr[7]], cargs=[])
qc.append(UGate(0.7278978053151748,5.145064315568138,1.7503156588884659), qargs=[qr[2]], cargs=[])
qc.append(C4XGate(), qargs=[qr[4], qr[1], qr[2], qr[6], qr[8]], cargs=[])
qc.append(RZZGate(6.262915463363716), qargs=[qr[9], qr[7]], cargs=[])
qc.append(SdgGate(), qargs=[qr[3]], cargs=[])
qc.append(ECRGate(), qargs=[qr[2], qr[7]], cargs=[])
qc.append(RZZGate(2.0261195842682675), qargs=[qr[7], qr[5]], cargs=[])
qc.append(U1Gate(0.5870983336064636), qargs=[qr[0]], cargs=[])
qc.append(RZZGate(4.586260430147017), qargs=[qr[7], qr[9]], cargs=[])
qc.append(YGate(), qargs=[qr[1]], cargs=[])
qc.append(C3XGate(), qargs=[qr[6], qr[3], qr[8], qr[4]], cargs=[])
qc.append(C4XGate(), qargs=[qr[0], qr[7], qr[5], qr[6], qr[4]], cargs=[])
qc.append(CSXGate(), qargs=[qr[9], qr[4]], cargs=[])
qc.append(C4XGate(), qargs=[qr[0], qr[8], qr[9], qr[5], qr[2]], cargs=[])

# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1, coupling_map=None)

# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_a92e993c9b464800be6faf9bcf4cb258 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_a92e993c9b464800be6faf9bcf4cb258, shots=5542).result().get_counts(qc)
RESULT = counts