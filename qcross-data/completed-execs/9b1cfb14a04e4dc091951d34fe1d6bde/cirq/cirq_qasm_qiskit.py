
import cirq
import qiskit
from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(9)]

p_897886 = Symbol('p_897886')
p_0477e2 = Symbol('p_0477e2')
p_343721 = Symbol('p_343721')
p_837a0a = Symbol('p_837a0a')
p_31e933 = Symbol('p_31e933')
p_b58743 = Symbol('p_b58743')
p_a36cb0 = Symbol('p_a36cb0')
p_966369 = Symbol('p_966369')
p_a7959d = Symbol('p_a7959d')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_343721)( qr[8] ))
circuit.append(Gates.CSXGate( qr[2], qr[4] ))
circuit.append(Gates.CUGate(p_31e933, p_897886, p_a36cb0, p_a7959d)( qr[0], qr[6] ))
circuit.append(Gates.SdgGate( qr[1] ))
circuit.append(Gates.C3SXGate( qr[0], qr[8], qr[7], qr[5] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.XGate( qr[5] ))
circuit.append(Gates.SGate( qr[0] ))
circuit.append(Gates.SGate( qr[8] ))
circuit.append(Gates.C3SXGate( qr[1], qr[3], qr[2], qr[0] ))
circuit.append(Gates.SXGate( qr[0] ))
circuit.append(Gates.CU1Gate(p_837a0a)( qr[8], qr[3] ))
circuit.append(Gates.CRZGate(p_b58743)( qr[5], qr[8] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.CSXGate( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[7] ))
circuit.append(Gates.CHGate( qr[6], qr[1] ))
circuit.append(Gates.CSXGate( qr[3], qr[0] ))
circuit.append(Gates.CRZGate(p_0477e2)( qr[1], qr[2] ))
circuit.append(Gates.U2Gate(2.5163050709890156, p_966369)( qr[2] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))
circuit.append(cirq.measure(qr[7], key='cr7'))
circuit.append(cirq.measure(qr[8], key='cr8'))



circuit = cirq.resolve_parameters(circuit, {
    "p_897886": 5.897054719225356,
    "p_0477e2": 2.586208953975239,
    "p_343721": 6.163759533339787,
    "p_837a0a": 3.2142159669963557,
    "p_31e933": 0.5112149185250571,
    "p_b58743": 1.4112277317699358,
    "p_a36cb0": 2.3864521352475245,
    "p_966369": 2.1276323672732023,
    "p_a7959d": 5.987304452123941
}, recursive=True)
        








expanded_circuit = cirq.expand_composite(circuit)
qasm_from_qiskit = qiskit.QuantumCircuit.from_qasm_str(cirq.qasm(expanded_circuit)).qasm()
cirq_circuit_from_qiskit_qasm = circuit_from_qasm(qasm_from_qiskit)

# since, importing in cirq uses different qubit names, we need to change the qubit names
circuit_transformed = cirq_circuit_from_qiskit_qasm.transform_qubits(lambda q: cirq.NamedQubit(q.name.replace("q_", "q")))

cirq.testing.assert_circuits_with_terminal_measurements_are_equivalent(circuit_transformed, circuit)




simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=3919)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7', 'cr8'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

