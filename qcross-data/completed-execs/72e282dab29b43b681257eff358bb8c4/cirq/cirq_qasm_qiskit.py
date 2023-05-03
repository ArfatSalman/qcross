
import cirq
import qiskit
from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(11)]

p_a3a14d = Symbol('p_a3a14d')
p_03a56d = Symbol('p_03a56d')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_a3a14d)( qr[6] ))
circuit.append(Gates.CRZGate(p_03a56d)( qr[10], qr[9] ))
circuit.append(Gates.ZGate( qr[7] ))
circuit.append(cirq.measure(qr[2], key='cr0'))
circuit.append(cirq.measure(qr[7], key='cr1'))
circuit.append(cirq.measure(qr[9], key='cr2'))
circuit.append(cirq.measure(qr[6], key='cr3'))
circuit.append(cirq.measure(qr[0], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[10], key='cr6'))
circuit.append(cirq.measure(qr[4], key='cr7'))
circuit.append(cirq.measure(qr[8], key='cr8'))
circuit.append(cirq.measure(qr[1], key='cr9'))
circuit.append(cirq.measure(qr[3], key='cr10'))



circuit = cirq.resolve_parameters(circuit, {
    "p_a3a14d": 6.163759533339787,
    "p_03a56d": 4.2641612072511235
}, recursive=True)
        








expanded_circuit = cirq.expand_composite(circuit)
qasm_from_qiskit = qiskit.QuantumCircuit.from_qasm_str(cirq.qasm(expanded_circuit)).qasm()
cirq_circuit_from_qiskit_qasm = circuit_from_qasm(qasm_from_qiskit)

# since, importing in cirq uses different qubit names, we need to change the qubit names
circuit_transformed = cirq_circuit_from_qiskit_qasm.transform_qubits(lambda q: cirq.NamedQubit(q.name.replace("q_", "q")))

cirq.testing.assert_circuits_with_terminal_measurements_are_equivalent(circuit_transformed, circuit)




simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=7838)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7', 'cr8', 'cr9', 'cr10'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

