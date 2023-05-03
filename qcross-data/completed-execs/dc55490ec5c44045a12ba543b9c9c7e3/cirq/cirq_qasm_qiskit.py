
import cirq
import qiskit
from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(2)]



circuit = cirq.Circuit()

circuit.append(Gates.ECRGate( qr[0], qr[1] ))
circuit.append(Gates.SwapGate( qr[1], qr[0] ))
circuit.append(Gates.CSXGate( qr[1], qr[0] ))
circuit.append(Gates.CU3Gate(0.19530688895228782, 1.7508214741181105, 0.6509821962978967)( qr[1], qr[0] ))
circuit.append(Gates.RZGate(0.07613141147187574)( qr[0] ))
circuit.append(Gates.CYGate( qr[0], qr[1] ))
circuit.append(Gates.RZXGate(2.3441041272871757)( qr[1], qr[0] ))
circuit.append(Gates.CSXGate( qr[1], qr[0] ))
circuit.append(Gates.CRZGate(0.11523003750909885)( qr[0], qr[1] ))
circuit.append(Gates.CYGate( qr[0], qr[1] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))











expanded_circuit = cirq.expand_composite(circuit)
qasm_from_qiskit = qiskit.QuantumCircuit.from_qasm_str(cirq.qasm(expanded_circuit)).qasm()
cirq_circuit_from_qiskit_qasm = circuit_from_qasm(qasm_from_qiskit)

# since, importing in cirq uses different qubit names, we need to change the qubit names
circuit_transformed = cirq_circuit_from_qiskit_qasm.transform_qubits(lambda q: cirq.NamedQubit(q.name.replace("q_", "q")))

cirq.testing.assert_circuits_with_terminal_measurements_are_equivalent(circuit_transformed, circuit)




simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=346)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1'])
RESULT = counts

if __name__ == '__main__':
    import json
    print(json.dumps(RESULT, sort_keys=True))
