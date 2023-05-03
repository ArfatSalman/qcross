# SECTION
# NAME: PROLOGUE

import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter
# SECTION
# NAME: CIRCUIT

qr = QuantumRegister(9, name='qr')
cr = ClassicalRegister(9, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')


subcircuit = QuantumCircuit(qr, cr, name='subcircuit')
subcircuit.append(DCXGate(), qargs=[qr[8], qr[7]], cargs=[])
subcircuit.append(XGate(), qargs=[qr[4]], cargs=[])
subcircuit.append(ZGate(), qargs=[qr[2]], cargs=[])
subcircuit.append(UGate(5.01836135520768,5.190931186022931,1.2128092629174942), qargs=[qr[7]], cargs=[])

qc.append(subcircuit, qargs=qr, cargs=cr)
qc.append(subcircuit.inverse(), qargs=qr, cargs=cr)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2, coupling_map=[[0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 6], [2, 0], [3, 0], [3, 7], [3, 11], [4, 0], [5, 6], [5, 8], [6, 1], [6, 5], [7, 3], [8, 5], [9, 11], [10, 11], [11, 3], [11, 9], [11, 10]])
# SECTION
# NAME: EXECUTION

from qiskit import Aer, transpile, execute
backend_2464f306817a470781f41676b6573ca7 = Aer.get_backend('aer_simulator_matrix_product_state')
counts = execute(qc, backend=backend_2464f306817a470781f41676b6573ca7, shots=3919).result().get_counts(qc)
RESULT = counts
