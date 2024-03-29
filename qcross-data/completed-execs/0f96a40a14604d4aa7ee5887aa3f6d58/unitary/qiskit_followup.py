# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(3, name='qr')
cr = ClassicalRegister(3, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(RZGate(6.163759533339787), qargs=[qr[0]], cargs=[])
qc.append(CHGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(SXdgGate(), qargs=[qr[1]], cargs=[])
qc.append(iSwapGate(), qargs=[qr[1], qr[0]], cargs=[])
qc.append(CSXGate(), qargs=[qr[0], qr[2]], cargs=[])
# SECTION
# NAME: USELESS_ENTITIES

qr_d43cad = QuantumRegister(2, name='qr_d43cad')
qc.add_register(qr_d43cad)
# SECTION

# NAME: MEASUREMENT
# Execute the circuit and obtain the unitary matrix
from qiskit import Aer, transpile, execute
result = execute(qc.reverse_bits(), backend=Aer.get_backend('unitary_simulator')).result()
UNITARY = result.get_unitary(qc).data


qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=None)
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_52fa27ac90aa4b948147b42382c83e6d = Aer.get_backend('qasm_simulator')
counts = execute(qc, backend=backend_52fa27ac90aa4b948147b42382c83e6d, shots=489).result().get_counts(qc)
RESULT = counts
