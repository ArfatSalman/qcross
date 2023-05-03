# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(11, name='qr')
cr = ClassicalRegister(11, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[10]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[6], qr[1]], cargs=[])
qc.append(ZGate(), qargs=[qr[5]], cargs=[])
qc.append(CCXGate(), qargs=[qr[0], qr[7], qr[4]], cargs=[])
qc.append(ZGate(), qargs=[qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[4]], cargs=[])
qc.append(RCCXGate(), qargs=[qr[9], qr[6], qr[3]], cargs=[])
qc.append(RZGate(4.229610589867865), qargs=[qr[2]], cargs=[])
qc.append(CCXGate(), qargs=[qr[4], qr[9], qr[1]], cargs=[])
qc.append(SdgGate(), qargs=[qr[4]], cargs=[])
qc.append(U2Gate(4.214504315296764, 4.6235667602042065), qargs=[qr[9]],
    cargs=[])
qc.append(CSXGate(), qargs=[qr[10], qr[1]], cargs=[])
qc.append(CHGate(), qargs=[qr[2], qr[4]], cargs=[])
qc.append(CU1Gate(4.028174522740928), qargs=[qr[7], qr[2]], cargs=[])
qc.append(RZGate(5.0063780207098425), qargs=[qr[6]], cargs=[])
qc.append(U2Gate(2.5163050709890156, 2.1276323672732023), qargs=[qr[1]],
    cargs=[])
qc.append(TGate(), qargs=[qr[2]], cargs=[])
qc.append(RZZGate(3.950837470808744), qargs=[qr[8], qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[5]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[0]], cargs=[])
qc.append(RZGate(4.722103101046168), qargs=[qr[1]], cargs=[])
qc.append(CRZGate(0.6393443962862078), qargs=[qr[0], qr[10]], cargs=[])
qc.append(CU1Gate(2.5476776328466872), qargs=[qr[10], qr[3]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[5]], cargs=[])
qc.append(RZGate(3.6614081973587154), qargs=[qr[6]], cargs=[])
qc.append(XGate(), qargs=[qr[3]], cargs=[])
qc.append(CSXGate(), qargs=[qr[4], qr[2]], cargs=[])
qc.append(CU1Gate(3.631024984774394), qargs=[qr[9], qr[4]], cargs=[])
qc.append(UGate(3.4183332103477166, 1.1450785027645094, 1.308491043619365),
    qargs=[qr[6]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: QASM_CONVERSION


from qiskit.qasm3 import loads, dumps
qc = loads(dumps(qc))

# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_52fd5bb3c8a74e63b20565a4224d67d6 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_52fd5bb3c8a74e63b20565a4224d67d6, shots=7838).result().get_counts(qc)
RESULT = counts
