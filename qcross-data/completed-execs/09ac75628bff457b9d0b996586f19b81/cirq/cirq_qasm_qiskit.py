
import cirq
import qiskit
from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(6)]

p_b2b67d = Symbol('p_b2b67d')
p_4c7bdf = Symbol('p_4c7bdf')
p_543c46 = Symbol('p_543c46')
p_86736a = Symbol('p_86736a')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_543c46)( qr[4] ))
circuit.append(Gates.ZGate( qr[3] ))
circuit.append(Gates.CRZGate(p_86736a)( qr[2], qr[4] ))
circuit.append(Gates.CUGate(p_b2b67d, p_4c7bdf, 2.3864521352475245, 5.987304452123941)( qr[2], qr[3] ))
circuit.append(Gates.C3SXGate( qr[1], qr[4], qr[0], qr[2] ))
circuit.append(Gates.CCXGate( qr[1], qr[5], qr[0] ))
circuit.append(Gates.C3SXGate( qr[4], qr[3], qr[5], qr[0] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.TGate( qr[4] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))



circuit = cirq.resolve_parameters(circuit, {
    "p_b2b67d": 0.5112149185250571,
    "p_4c7bdf": 5.897054719225356,
    "p_543c46": 6.163759533339787,
    "p_86736a": 4.2641612072511235
}, recursive=True)
        








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
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

