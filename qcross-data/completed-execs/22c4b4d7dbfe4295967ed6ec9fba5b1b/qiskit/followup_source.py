# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(10, name='qr')
cr = ClassicalRegister(10, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[3]], cargs=[])
qc.append(CRZGate(4.2641612072511235), qargs=[qr[6], qr[3]], cargs=[])
qc.append(CRXGate(5.987304452123941), qargs=[qr[1], qr[7]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_7601dd = QuantumRegister(9, name='qr_7601dd')
qc.add_register(qr_7601dd)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=['cx', 'h', 's', 't'], optimization_level=0,
    coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_45e5fe214fac4ac1863ece87f042f069 = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_45e5fe214fac4ac1863ece87f042f069, shots=5542).result().get_counts(qc)
RESULT = counts
