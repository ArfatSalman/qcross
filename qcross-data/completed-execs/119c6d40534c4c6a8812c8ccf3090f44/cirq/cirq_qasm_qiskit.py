
import cirq
import qiskit
from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(4)]

p_4891c3 = Symbol('p_4891c3')
p_4d6844 = Symbol('p_4d6844')
p_72b19d = Symbol('p_72b19d')
p_1dbd94 = Symbol('p_1dbd94')
p_ab8a7b = Symbol('p_ab8a7b')

circuit = cirq.Circuit()

circuit.append(Gates.SdgGate( qr[1] ))
circuit.append(Gates.RYYGate(2.10593478876119)( qr[2], qr[1] ))
circuit.append(Gates.IGate( qr[1] ))
circuit.append(Gates.CZGate( qr[2], qr[3] ))
circuit.append(Gates.CZGate( qr[0], qr[3] ))
circuit.append(Gates.CZGate( qr[1], qr[2] ))
circuit.append(Gates.CU3Gate(p_72b19d, p_4891c3, p_4d6844)( qr[2], qr[0] ))
circuit.append(Gates.CHGate( qr[2], qr[3] ))
circuit.append(Gates.CPhaseGate(p_1dbd94)( qr[2], qr[0] ))
circuit.append(Gates.SGate( qr[0] ))
circuit.append(Gates.C3XGate( qr[3], qr[1], qr[2], qr[0] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))



circuit = cirq.resolve_parameters(circuit, {
    "p_4891c3": 3.7847055340640803,
    "p_4d6844": 5.596894918056728,
    "p_72b19d": 5.177552214723695,
    "p_1dbd94": 5.982058731459433,
    "p_ab8a7b": 0.45470685223891605
}, recursive=True)
        








expanded_circuit = cirq.expand_composite(circuit)
qasm_from_qiskit = qiskit.QuantumCircuit.from_qasm_str(cirq.qasm(expanded_circuit)).qasm()
cirq_circuit_from_qiskit_qasm = circuit_from_qasm(qasm_from_qiskit)

# since, importing in cirq uses different qubit names, we need to change the qubit names
circuit_transformed = cirq_circuit_from_qiskit_qasm.transform_qubits(lambda q: cirq.NamedQubit(q.name.replace("q_", "q")))

cirq.testing.assert_circuits_with_terminal_measurements_are_equivalent(circuit_transformed, circuit)




simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=692)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3'])
RESULT = counts

if __name__ == '__main__':
    import json
    print(json.dumps(RESULT, sort_keys=True))
