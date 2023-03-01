cirq_qasm = """
// Generated from Cirq v1.1.0

OPENQASM 2.0;
include "qelib1.inc";


// Qubits: [q_0]
qreg q[1];

h q[0];
"""

qiskit_qasm = """
OPENQASM 2.0;
include "qelib1.inc";
qreg q[1];
h q[0];
"""


import cirq
import qiskit
from cirq.contrib.qasm_import import circuit_from_qasm

qr = [cirq.NamedQubit("q" + str(i)) for i in range(2)]
# qr = cirq.LineQubit.range(2)


circuit = cirq.Circuit()

circuit.append(cirq.H(qr[0]))


# c2 = circuit_from_qasm(qiskit.QuantumCircuit.from_qasm_str(cirq.qasm(circuit)).qasm())
c2 = circuit_from_qasm(qiskit.QuantumCircuit.from_qasm_str(cirq.qasm(circuit)).qasm())
# print(qiskit.QuantumCircuit.from_qasm_str(cirq.qasm(circuit)).qasm())
# print(c2)
c2 = c2.transform_qubits(lambda q: cirq.NamedQubit(q.name.replace("q_", "q")))
# print(c2.to_qasm())
# print(len(c2.all_qubits()))

cirq.testing.assert_circuits_with_terminal_measurements_are_equivalent(c2, circuit)
