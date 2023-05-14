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
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])
subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(U3Gate(4.094867647151279, 5.154187354656876, 0.4903361071050254), qargs=[qr[1]], cargs=[])
subcircuit.append(IGate(), qargs=[qr[2]], cargs=[])
subcircuit.append(UGate(5.01836135520768, 5.190931186022931, 1.2128092629174942), qargs=[qr[4]], cargs=[])
qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
qc.append(CRZGate(4.2641612072511235), qargs=[qr[6], qr[2]], cargs=[])
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=['ccx', 'h'], optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION
from qiskit import Aer, transpile, execute
backend_d109b29d70c1406bbe0b20ef7cb410c3 = Aer.get_backend(
    'aer_simulator_density_matrix')
counts = execute(qc, backend=backend_d109b29d70c1406bbe0b20ef7cb410c3,
    shots=7838).result().get_counts(qc)
RESULT = counts
