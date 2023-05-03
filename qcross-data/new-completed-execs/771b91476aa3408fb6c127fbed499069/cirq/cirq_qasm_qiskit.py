
import cirq
import qiskit
from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(7)]



circuit = cirq.Circuit()

circuit.append(Gates.U1Gate(5.479758197394313)( qr[1] ))
circuit.append(Gates.RGate(6.143639644288786, 3.8563981362966246)( qr[2] ))
circuit.append(Gates.SwapGate( qr[3], qr[5] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.CUGate(1.573398276884453, 2.4750711131608187, 2.608178435015891, 0.020264981462429707)( qr[3], qr[2] ))
subcircuit.append(Gates.CCXGate( qr[3], qr[6], qr[2] ))
subcircuit.append(Gates.CXGate( qr[6], qr[4] ))
subcircuit.append(Gates.XGate( qr[1] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.CU3Gate(0.22167464109509083, 6.012192432688993, 0.4115095208941581)( qr[5], qr[1] ))
circuit.append(Gates.CCZGate( qr[1], qr[3], qr[0] ))
circuit.append(Gates.U2Gate(0.9648254328971443, 2.9933536728613173)( qr[4] ))
circuit.append(Gates.RXXGate(2.032522200125169)( qr[4], qr[1] ))
circuit.append(Gates.CSGate( qr[3], qr[1] ))
circuit.append(Gates.RGate(4.790279244293115, 5.917497614834585)( qr[1] ))
circuit.append(Gates.RZZGate(1.6645038233620808)( qr[4], qr[6] ))
circuit.append(Gates.U1Gate(0.07676574518435057)( qr[2] ))
circuit.append(Gates.XGate( qr[4] ))
circuit.append(Gates.XGate( qr[2] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))











expanded_circuit = cirq.expand_composite(circuit)
qasm_from_qiskit = qiskit.QuantumCircuit.from_qasm_str(cirq.qasm(expanded_circuit)).qasm()
cirq_circuit_from_qiskit_qasm = circuit_from_qasm(qasm_from_qiskit)

# since, importing in cirq uses different qubit names, we need to change the qubit names
circuit_transformed = cirq_circuit_from_qiskit_qasm.transform_qubits(lambda q: cirq.NamedQubit(q.name.replace("q_", "q")))

cirq.testing.assert_circuits_with_terminal_measurements_are_equivalent(circuit_transformed, circuit)




simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=1959)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

