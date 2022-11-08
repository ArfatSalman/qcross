
# # SECTION
# # NAME: PROLOGUE

# import qiskit
# from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
# from qiskit.circuit.library.standard_gates import *
# from qiskit.circuit import Parameter

# # SECTION
# # NAME: CIRCUIT

# qr = QuantumRegister(7, name='qr')
# cr = ClassicalRegister(7, name='cr')
# qc = QuantumCircuit(qr, cr, name='qc')
# qc.append(CU1Gate(5.83674944466042), qargs=[qr[1], qr[0]], cargs=[])
# qc.append(ZGate(), qargs=[qr[2]], cargs=[])
# qc.append(C4XGate(), qargs=[qr[4], qr[3], qr[0], qr[1], qr[6]], cargs=[])
# qc.append(RCCXGate(), qargs=[qr[2], qr[3], qr[0]], cargs=[])
# qc.append(RCCXGate(), qargs=[qr[0], qr[1], qr[4]], cargs=[])

# # SECTION
# # NAME: MEASUREMENT

# qc.measure(qr, cr)

# # SECTION
# # NAME: OPTIMIZATION_LEVEL

# from qiskit import transpile
# qc = transpile(qc, basis_gates=None, optimization_level=0, coupling_map=None)

# # SECTION
# # NAME: EXECUTION

# from qiskit import Aer, transpile, execute
# backend_3402d4d15bf24ec58dbf6472ed794f8f = Aer.get_backend('qasm_simulator')
# counts = execute(qc, backend=backend_3402d4d15bf24ec58dbf6472ed794f8f, shots=1959).result().get_counts(qc)
# RESULT = counts

from pyquil import Program
from pyquil.gates import *

import numpy as np

from pyquil.quil import DefGate

cu1_gate = np.array([[], []])

p = Program()
ro = p.declare('ro', 'BIT', 7) # classical register