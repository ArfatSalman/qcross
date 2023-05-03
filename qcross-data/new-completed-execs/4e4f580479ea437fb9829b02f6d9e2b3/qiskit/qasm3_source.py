# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit.library import RVGate
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(6, name='qr')
cr = ClassicalRegister(6, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(CUGate(1.6223452394490818, 5.934623154479406, 1.7805086724904042, 5.061824279359645), qargs=[qr[4], qr[1]], cargs=[])
qc.append(RC3XGate(), qargs=[qr[2], qr[5], qr[4], qr[3]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(CSXGate(), qargs=[qr[1], qr[4]], cargs=[])
subcircuit.append(PhaseGate(2.2974214640336745), qargs=[qr[5]], cargs=[])
subcircuit.append(IGate(), qargs=[qr[4]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CSXGate(), qargs=[qr[1], qr[4]], cargs=[])
qc.append(CU1Gate(1.4856120967675965), qargs=[qr[0], qr[4]], cargs=[])
qc.append(CRYGate(5.668943646639131), qargs=[qr[1], qr[5]], cargs=[])
qc.append(CU1Gate(0.6022957689924475), qargs=[qr[2], qr[0]], cargs=[])
qc.append(U2Gate(2.512828094986993, 4.8320076449293525), qargs=[qr[4]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[3], qr[4]], cargs=[])
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
qc = transpile(qc, basis_gates=None, optimization_level=1, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_191f0d9c2cb54e0bafaefd07e9ed2c24 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_191f0d9c2cb54e0bafaefd07e9ed2c24, shots=1385).result().get_counts(qc)
RESULT = counts
