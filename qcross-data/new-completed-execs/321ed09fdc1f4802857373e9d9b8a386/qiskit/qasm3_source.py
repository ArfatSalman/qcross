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
qc.append(CRXGate(3.789039586142132), qargs=[qr[0], qr[1]], cargs=[])


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(XGate(), qargs=[qr[0]], cargs=[])
subcircuit.append(PhaseGate(1.0991937230132693), qargs=[qr[0]], cargs=[])
subcircuit.append(RZZGate(0.29263822564237946), qargs=[qr[0], qr[1]], cargs=[])
subcircuit.append(CU1Gate(1.319709844326333), qargs=[qr[1], qr[0]], cargs=[])
subcircuit.append(CPhaseGate(0.07651702010631041), qargs=[qr[0], qr[1]], cargs=[])
subcircuit.append(CUGate(3.544831331267256,5.290981419397922,4.5769317827703135,3.078979867833689), qargs=[qr[0], qr[1]], cargs=[])
subcircuit.append(RGate(3.7945044816842795,4.841616274028528), qargs=[qr[0]], cargs=[])
subcircuit.append(CZGate(), qargs=[qr[1], qr[0]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(PhaseGate(2.3969015822468824), qargs=[qr[0]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(PhaseGate(2.7534454125103585), qargs=[qr[1]], cargs=[])
qc.append(PhaseGate(4.877116605613038), qargs=[qr[0]], cargs=[])
qc.append(TdgGate(), qargs=[qr[1]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(PhaseGate(5.974310031718985), qargs=[qr[1]], cargs=[])
qc.append(U2Gate(3.2332547554497055, 2.6884001068559122), qargs=[qr[0]], cargs=[])
qc.append(HGate(), qargs=[qr[1]], cargs=[])
qc.append(CYGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(DCXGate(), qargs=[qr[1], qr[0]], cargs=[])
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
qc = transpile(qc, basis_gates=None, optimization_level=3, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_fa977bf02d4046c0ab2548d684da6fd8 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_fa977bf02d4046c0ab2548d684da6fd8, shots=346).result().get_counts(qc)
RESULT = counts
