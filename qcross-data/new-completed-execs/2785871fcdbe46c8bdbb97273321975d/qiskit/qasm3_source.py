# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(5, name='qr')
cr = ClassicalRegister(5, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(SGate(), qargs=[qr[3]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CCZGate(), qargs=[qr[4], qr[1], qr[0]], cargs=[])
subcircuit.append(RZZGate(1.494768934171475), qargs=[qr[3], qr[0]], cargs=[])
subcircuit.append(RGate(0.2569619900931398,2.6199756460968913), qargs=[qr[4]], cargs=[])
subcircuit.append(TdgGate(), qargs=[qr[3]], cargs=[])
subcircuit.append(SXdgGate(), qargs=[qr[1]], cargs=[])
subcircuit.append(PhaseGate(4.75198563922302), qargs=[qr[0]], cargs=[])
subcircuit.append(RC3XGate(), qargs=[qr[1], qr[3], qr[4], qr[2]], cargs=[])
subcircuit.append(SGate(), qargs=[qr[3]], cargs=[])
subcircuit.append(CHGate(), qargs=[qr[1], qr[3]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CSdgGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(RXGate(5.16336000498251), qargs=[qr[2]], cargs=[])
qc.append(SGate(), qargs=[qr[3]], cargs=[])
qc.append(CRXGate(3.8747797547682863), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CXGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(SwapGate(), qargs=[qr[3], qr[1]], cargs=[])
qc.append(CSXGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(CSdgGate(), qargs=[qr[3], qr[2]], cargs=[])
qc.append(DCXGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(CPhaseGate(1.6310047821220433), qargs=[qr[3], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: QASM_CONVERSION


from qiskit.qasm3 import loads, dumps
qc = loads(dumps(qc))

# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_231057da500e42c5ad60bce1fb79c55b = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_231057da500e42c5ad60bce1fb79c55b, shots=979).result().get_counts(qc)
RESULT = counts
