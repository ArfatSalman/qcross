# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(2, name='qr')
cr = ClassicalRegister(2, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(IGate(), qargs=[qr[1]], cargs=[])
qc.append(SwapGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SwapGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(RYGate(1.1002993512000188), qargs=[qr[1]], cargs=[])
qc.append(CPhaseGate(1.9632220362422863), qargs=[qr[1], qr[0]], cargs=[])
qc.append(RYYGate(1.9181567063153306), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CRXGate(2.4590168324579773), qargs=[qr[0], qr[1]], cargs=[])
qc.append(PhaseGate(0.7665475532378738), qargs=[qr[0]], cargs=[])
qc.append(RYYGate(1.153606269131821), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CPhaseGate(1.1100132636552245), qargs=[qr[1], qr[0]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(UGate(3.8572757475580413, 1.8831270698344038, 5.011779985191158), qargs=[qr[1]], cargs=[])
qc.append(CRXGate(2.1827683748032527), qargs=[qr[0], qr[1]], cargs=[])
qc.append(IGate(), qargs=[qr[0]], cargs=[])
qc.append(RYGate(0.5934420994921776), qargs=[qr[0]], cargs=[])
qc.append(RYGate(0.5479105491667954), qargs=[qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[1]], cargs=[])
qc.append(UGate(6.2496149710424405, 5.8205761472087545, 5.829068520224341), qargs=[qr[1]], cargs=[])
qc.append(DCXGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(RZZGate(4.338194291975017), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[1]], cargs=[])
qc.append(CPhaseGate(1.7974397830964004), qargs=[qr[1], qr[0]], cargs=[])
qc.append(DCXGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SXGate(), qargs=[qr[0]], cargs=[])
qc.append(IGate(), qargs=[qr[0]], cargs=[])
qc.append(CRXGate(4.404558705198131), qargs=[qr[0], qr[1]], cargs=[])
qc.append(TdgGate(), qargs=[qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [1, 0], [1, 2], [2, 1]])# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_63cafb5ad84c4ccb88d84bf51dc6decc = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_63cafb5ad84c4ccb88d84bf51dc6decc, shots=346).result().get_counts(qc)
RESULT = counts
