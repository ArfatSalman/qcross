
import cirq
import qiskit
from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr_1 = [cirq.NamedQubit('q' + str(i)) for i in range(5)]



circuit = cirq.Circuit()

circuit.append(cirq.measure(qr_1[0], key='cr0'))
circuit.append(cirq.measure(qr_1[1], key='cr1'))
circuit.append(cirq.measure(qr_1[2], key='cr2'))
circuit.append(cirq.measure(qr_1[3], key='cr3'))
circuit.append(cirq.measure(qr_1[4], key='cr4'))











expanded_circuit = cirq.expand_composite(circuit)
qasm_from_qiskit = qiskit.QuantumCircuit.from_qasm_str(cirq.qasm(expanded_circuit)).qasm()
cirq_circuit_from_qiskit_qasm = circuit_from_qasm(qasm_from_qiskit)

# since, importing in cirq uses different qubit names, we need to change the qubit names
circuit_transformed = cirq_circuit_from_qiskit_qasm.transform_qubits(lambda q: cirq.NamedQubit(q.name.replace("q_", "q")))

cirq.testing.assert_circuits_with_terminal_measurements_are_equivalent(circuit_transformed, circuit)




simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=1385)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

