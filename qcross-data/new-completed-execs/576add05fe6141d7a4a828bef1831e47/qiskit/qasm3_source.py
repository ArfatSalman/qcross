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
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(ECRGate(), qargs=[qr[7], qr[1]], cargs=[])
subcircuit.append(CXGate(), qargs=[qr[6], qr[0]], cargs=[])
subcircuit.append(SXdgGate(), qargs=[qr[4]], cargs=[])
subcircuit.append(HGate(), qargs=[qr[6]], cargs=[])
subcircuit.append(RZZGate(1.1809864697709562), qargs=[qr[0], qr[6]], cargs=[])
subcircuit.append(U1Gate(3.0511475243475985), qargs=[qr[3]], cargs=[])
subcircuit.append(UGate(1.758300519432271, 2.7759984582269563, 5.130578246510858), qargs=[qr[1]], cargs=[])
subcircuit.append(RYYGate(2.8616233109786804), qargs=[qr[5], qr[2]], cargs=[])
subcircuit.append(CU3Gate(5.782992008877923, 2.583390532654726, 3.229621753302509), qargs=[qr[6], qr[5]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1, coupling_map=None)
# SECTION
# NAME: QASM_CONVERSION

from qiskit.qasm3 import loads, dumps
qc = loads(dumps(qc))

# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_96a24546c67e428497607f653ce7c1a9 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_96a24546c67e428497607f653ce7c1a9, shots=2771).result().get_counts(qc)
RESULT = counts
