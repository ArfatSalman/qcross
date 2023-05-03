
# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter

# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(2, name='qr')
cr = ClassicalRegister(2, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(CHGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CUGate(2.0087468885271504,5.883811190278971,5.864947219205212,5.7446598664897115), qargs=[qr[1], qr[0]], cargs=[])
qc.append(RXGate(5.794504209717704), qargs=[qr[1]], cargs=[])
qc.append(RZZGate(2.1663122372864825), qargs=[qr[1], qr[0]], cargs=[])
qc.append(DCXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(TGate(), qargs=[qr[0]], cargs=[])
qc.append(U2Gate(3.615801062466814,0.8936944779843444), qargs=[qr[1]], cargs=[])
qc.append(RYGate(2.2562188139100248), qargs=[qr[1]], cargs=[])
qc.append(RYYGate(6.060522892419086), qargs=[qr[1], qr[0]], cargs=[])
qc.append(SwapGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(TGate(), qargs=[qr[0]], cargs=[])
qc.append(SwapGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(U3Gate(3.8927238245726374,2.0377807006749333,4.064217417062462), qargs=[qr[0]], cargs=[])
qc.append(RZGate(2.414915889738904), qargs=[qr[1]], cargs=[])
qc.append(CRYGate(2.594321777907923), qargs=[qr[1], qr[0]], cargs=[])
qc.append(RXGate(2.3571868764276998), qargs=[qr[1]], cargs=[])
qc.append(RZZGate(0.3644709100093532), qargs=[qr[0], qr[1]], cargs=[])
qc.append(RXGate(2.5276999718154167), qargs=[qr[1]], cargs=[])
qc.append(CZGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(RZZGate(3.41477281916325), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(U3Gate(5.170631856240322,2.9463190555168968,2.269493738638121), qargs=[qr[0]], cargs=[])
qc.append(U3Gate(2.481557449187282,3.06771330185138,2.2732733996544363), qargs=[qr[1]], cargs=[])
qc.append(TGate(), qargs=[qr[0]], cargs=[])
qc.append(CUGate(0.8725199162352276,2.0033484721527364,1.6015864357317902,4.9684596562340495), qargs=[qr[1], qr[0]], cargs=[])
qc.append(RYGate(5.8249335523617525), qargs=[qr[0]], cargs=[])
qc.append(RZGate(4.757508594558637), qargs=[qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SwapGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CU3Gate(3.137732232950496,2.9454453048301827,2.754468708884141), qargs=[qr[0], qr[1]], cargs=[])

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
backend_09dbed020a434837a9b4b33b5a67c75a = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_09dbed020a434837a9b4b33b5a67c75a, shots=346).result().get_counts(qc)
RESULT = counts