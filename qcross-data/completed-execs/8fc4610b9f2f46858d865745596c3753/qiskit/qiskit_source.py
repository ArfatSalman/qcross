
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
qc.append(CRYGate(5.084522291571211), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CRYGate(0.5214443205823275), qargs=[qr[0], qr[1]], cargs=[])
qc.append(UGate(5.249389156861369,5.506136172902856,5.236656888622806), qargs=[qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(DCXGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CU3Gate(1.3702172143092286,1.9059592606091926,5.782626030792982), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CU3Gate(3.371102520538735,2.998573490180536,1.776109337694477), qargs=[qr[1], qr[0]], cargs=[])
qc.append(DCXGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(UGate(4.284938125077518,1.0148536455132817,2.487168338274746), qargs=[qr[0]], cargs=[])
qc.append(RYGate(3.900848522710214), qargs=[qr[0]], cargs=[])
qc.append(RZGate(2.334985126003777), qargs=[qr[1]], cargs=[])
qc.append(RYGate(1.7484204274088997), qargs=[qr[0]], cargs=[])
qc.append(TdgGate(), qargs=[qr[0]], cargs=[])
qc.append(CU3Gate(4.742430815090222,1.8154225091000729,3.693501832396555), qargs=[qr[1], qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(SGate(), qargs=[qr[1]], cargs=[])
qc.append(RZGate(5.556271444847221), qargs=[qr[1]], cargs=[])
qc.append(CRZGate(1.6719873041871378), qargs=[qr[1], qr[0]], cargs=[])
qc.append(DCXGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(U2Gate(3.6951879813098216,4.977624965840704), qargs=[qr[1]], cargs=[])
qc.append(CU3Gate(5.4144948963161035,6.127785368788657,2.137798063823039), qargs=[qr[1], qr[0]], cargs=[])
qc.append(U2Gate(4.611032125076666,2.7074003913270643), qargs=[qr[1]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(U2Gate(6.108789748804481,2.1969367629951018), qargs=[qr[0]], cargs=[])
qc.append(RYGate(2.811127302481191), qargs=[qr[0]], cargs=[])
qc.append(TGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])

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
backend_d5aed2ce95d04fcf9b7ec48cd069b4b3 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_d5aed2ce95d04fcf9b7ec48cd069b4b3, shots=346).result().get_counts(qc)
RESULT = counts