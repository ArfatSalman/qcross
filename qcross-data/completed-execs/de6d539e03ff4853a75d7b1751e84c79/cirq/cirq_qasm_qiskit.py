
import cirq
import qiskit
from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(8)]



circuit = cirq.Circuit()

circuit.append(Gates.DCXGate( qr[7], qr[1] ))
circuit.append(Gates.CRZGate(3.5837947443419367)( qr[7], qr[3] ))
circuit.append(Gates.SXGate( qr[0] ))
circuit.append(Gates.iSwapGate( qr[3], qr[2] ))
circuit.append(Gates.CRYGate(4.123021946449677)( qr[5], qr[1] ))
circuit.append(Gates.CSXGate( qr[4], qr[7] ))
circuit.append(Gates.RZXGate(4.811413391581055)( qr[5], qr[0] ))
circuit.append(Gates.CU1Gate(3.648178050626694)( qr[6], qr[4] ))
circuit.append(Gates.RYGate(5.8216640063628375)( qr[1] ))
circuit.append(Gates.CU1Gate(0.7038286154091901)( qr[7], qr[1] ))
circuit.append(Gates.DCXGate( qr[2], qr[5] ))
circuit.append(Gates.CYGate( qr[6], qr[5] ))
circuit.append(Gates.SGate( qr[3] ))
circuit.append(Gates.CRZGate(0.18001367059010623)( qr[1], qr[6] ))
circuit.append(Gates.ZGate( qr[4] ))
circuit.append(Gates.CSXGate( qr[2], qr[6] ))
circuit.append(Gates.PhaseGate(5.414747327887186)( qr[1] ))
circuit.append(Gates.CRYGate(4.001439863248854)( qr[1], qr[5] ))
circuit.append(Gates.SXGate( qr[2] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))
circuit.append(cirq.measure(qr[7], key='cr7'))











expanded_circuit = cirq.expand_composite(circuit)
qasm_from_qiskit = qiskit.QuantumCircuit.from_qasm_str(cirq.qasm(expanded_circuit)).qasm()
cirq_circuit_from_qiskit_qasm = circuit_from_qasm(qasm_from_qiskit)

# since, importing in cirq uses different qubit names, we need to change the qubit names
circuit_transformed = cirq_circuit_from_qiskit_qasm.transform_qubits(lambda q: cirq.NamedQubit(q.name.replace("q_", "q")))

cirq.testing.assert_circuits_with_terminal_measurements_are_equivalent(circuit_transformed, circuit)




simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=2771)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7'])
RESULT = counts

if __name__ == '__main__':
    import json
    print(json.dumps(RESULT, sort_keys=True))
