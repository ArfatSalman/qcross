import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *
from qiskit.circuit import Parameter


qr = QuantumRegister(1, name='qr')
cr = ClassicalRegister(1, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')

qc.append(U1Gate(3.481387546019227), qargs=[qr[0]], cargs=[])

import qiskit.quantum_info as qi

op = qi.Operator(qc)

# ---CIRQ
    

import cirq

import numpy as np
from functools import reduce

class U1Gate(cirq.Gate):
    def __init__(self, lam):
        super(U1Gate, self)
        self.lam = lam

    def _num_qubits_(self):
        return 1

    def _unitary_(self):
        lam = float(self.lam)
        return np.array([[1, 0], [0, np.exp(1j * lam)]])

    def _circuit_diagram_info_(self, args):
        return f"U1({self.lam:.2f})"

q = [cirq.NamedQubit('q' + str(i)) for i in range(1)]

circuit = cirq.Circuit(
    U1Gate(3.481387546019227)(q[0])
)

op.equiv(circuit.unitary())