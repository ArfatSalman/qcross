
import cirq
import qiskit
from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(3)]



circuit = cirq.Circuit()

circuit.append(Gates.CZGate( qr[1], qr[2] ))
circuit.append(Gates.CCXGate( qr[2], qr[1], qr[0] ))
circuit.append(Gates.CU3Gate(0.02974191542848892, 1.097684714540871, 0.5523925010367368)( qr[1], qr[0] ))
circuit.append(Gates.HGate( qr[0] ))
circuit.append(Gates.U1Gate(4.64787760789041)( qr[0] ))
circuit.append(Gates.iSwapGate( qr[0], qr[2] ))
circuit.append(Gates.YGate( qr[2] ))
circuit.append(Gates.CZGate( qr[1], qr[2] ))
circuit.append(Gates.iSwapGate( qr[1], qr[2] ))
circuit.append(Gates.YGate( qr[1] ))
circuit.append(Gates.RYYGate(2.3941143994200504)( qr[1], qr[0] ))
circuit.append(Gates.TdgGate( qr[0] ))
circuit.append(Gates.SGate( qr[2] ))
circuit.append(Gates.RXGate(5.932085825305516)( qr[2] ))
circuit.append(Gates.CSwapGate( qr[2], qr[0], qr[1] ))
circuit.append(Gates.SdgGate( qr[2] ))
circuit.append(Gates.U3Gate(0.20490217819899895, 0.2844754781181525, 4.8984947281198385)( qr[2] ))
circuit.append(Gates.CYGate( qr[1], qr[2] ))
circuit.append(Gates.RYGate(4.64391690767843)( qr[1] ))
circuit.append(Gates.SGate( qr[1] ))
circuit.append(Gates.IGate( qr[0] ))
circuit.append(Gates.U1Gate(3.4582628336664856)( qr[0] ))
circuit.append(Gates.IGate( qr[1] ))
circuit.append(Gates.CSXGate( qr[2], qr[0] ))
circuit.append(Gates.SGate( qr[0] ))
circuit.append(Gates.CU1Gate(3.1245965108163056)( qr[1], qr[2] ))
circuit.append(Gates.RXGate(0.16532103311248328)( qr[1] ))
circuit.append(Gates.TdgGate( qr[2] ))
circuit.append(Gates.RYGate(2.5451656062496135)( qr[1] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))











expanded_circuit = cirq.expand_composite(circuit)
qasm_from_qiskit = qiskit.QuantumCircuit.from_qasm_str(cirq.qasm(expanded_circuit)).qasm()
cirq_circuit_from_qiskit_qasm = circuit_from_qasm(qasm_from_qiskit)

# since, importing in cirq uses different qubit names, we need to change the qubit names
circuit_transformed = cirq_circuit_from_qiskit_qasm.transform_qubits(lambda q: cirq.NamedQubit(q.name.replace("q_", "q")))

cirq.testing.assert_circuits_with_terminal_measurements_are_equivalent(circuit_transformed, circuit)




simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=489)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2'])
RESULT = counts

if __name__ == '__main__':
    import json
    print(json.dumps(RESULT, sort_keys=True))
