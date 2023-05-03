
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
qc.append(RYYGate(1.7892872835005398), qargs=[qr[0], qr[5]], cargs=[])
qc.append(PhaseGate(3.7964394792576885), qargs=[qr[6]], cargs=[])
qc.append(RYGate(3.6138974545836176), qargs=[qr[2]], cargs=[])
qc.append(CU1Gate(4.877167017151953), qargs=[qr[4], qr[1]], cargs=[])
qc.append(CCXGate(), qargs=[qr[4], qr[3], qr[2]], cargs=[])
qc.append(ECRGate(), qargs=[qr[0], qr[6]], cargs=[])
qc.append(CSwapGate(), qargs=[qr[0], qr[6], qr[4]], cargs=[])
qc.append(ECRGate(), qargs=[qr[2], qr[0]], cargs=[])
qc.append(SwapGate(), qargs=[qr[3], qr[5]], cargs=[])
qc.append(CSwapGate(), qargs=[qr[3], qr[6], qr[1]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[6], qr[1], qr[4], qr[0]], cargs=[])
qc.append(HGate(), qargs=[qr[2]], cargs=[])
qc.append(UGate(5.066050249739578,3.676251393433825,2.5510590709018732), qargs=[qr[2]], cargs=[])
qc.append(U2Gate(4.9702527118009066,3.5114983819004046), qargs=[qr[4]], cargs=[])
qc.append(CSGate(), qargs=[qr[2], qr[5]], cargs=[])
qc.append(U2Gate(1.6924855892819173,6.035455549292343), qargs=[qr[6]], cargs=[])
qc.append(RYYGate(3.0928548495797905), qargs=[qr[1], qr[5]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[3], qr[1], qr[4], qr[5]], cargs=[])
qc.append(UGate(0.8822742453157227,3.4849606070943584,4.713462039096519), qargs=[qr[3]], cargs=[])
qc.append(CUGate(5.814210499839879,2.2396990253899713,5.986977817617511,6.091448724065051), qargs=[qr[3], qr[5]], cargs=[])
qc.append(U2Gate(4.95448520957096,2.4524844691285543), qargs=[qr[6]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[1], qr[3], qr[2], qr[0]], cargs=[])
qc.append(RXGate(5.129266867572668), qargs=[qr[0]], cargs=[])
qc.append(CRYGate(2.998268232293747), qargs=[qr[6], qr[1]], cargs=[])

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
backend_f942a370704e467aa681067f28978a83 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_f942a370704e467aa681067f28978a83, shots=1959).result().get_counts(qc)
RESULT = counts