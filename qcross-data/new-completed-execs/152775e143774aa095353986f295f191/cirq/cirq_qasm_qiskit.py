
import cirq
import qiskit
from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(2)]



circuit = cirq.Circuit()

circuit.append(Gates.UGate(1.0932143214299395, 6.100531540039404, 4.859714896792146)( qr[1] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.CYGate( qr[1], qr[0] ))
subcircuit.append(Gates.RVGate(2.4118372331017857, 4.007316327236995, 4.304922836512128)( qr[1] ))
subcircuit.append(Gates.RZXGate(4.840163560981886)( qr[1], qr[0] ))
subcircuit.append(Gates.RXGate(2.7792529037894678)( qr[1] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.CYGate( qr[0], qr[1] ))
circuit.append(Gates.RXGate(4.335996068527454)( qr[0] ))
circuit.append(Gates.SGate( qr[1] ))
circuit.append(Gates.RXGate(6.070601620234646)( qr[0] ))
circuit.append(Gates.RZXGate(3.9660842997699097)( qr[0], qr[1] ))
circuit.append(Gates.HGate( qr[1] ))
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
    from qcross.utils import display_results
    display_results( {"result": RESULT })

