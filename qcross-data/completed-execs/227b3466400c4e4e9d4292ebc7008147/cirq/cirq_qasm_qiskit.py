
import cirq
import qiskit
from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(2)]



circuit = cirq.Circuit()

circuit.append(Gates.TdgGate( qr[0] ))
circuit.append(Gates.PhaseGate(1.3428862289262922)( qr[0] ))
circuit.append(Gates.CHGate( qr[0], qr[1] ))
circuit.append(Gates.CU3Gate(4.165123907650545, 2.6766240976228306, 5.851109164020841)( qr[1], qr[0] ))
circuit.append(Gates.CZGate( qr[0], qr[1] ))
circuit.append(Gates.U3Gate(3.1124943003575862, 5.033907753688158, 3.427635111293556)( qr[1] ))
circuit.append(Gates.RZZGate(5.9643464495294385)( qr[0], qr[1] ))
circuit.append(Gates.U1Gate(3.005113685069328)( qr[0] ))
circuit.append(Gates.HGate( qr[0] ))
circuit.append(Gates.CHGate( qr[1], qr[0] ))
circuit.append(Gates.PhaseGate(0.3147213681222795)( qr[0] ))
circuit.append(Gates.SXGate( qr[0] ))
circuit.append(Gates.YGate( qr[1] ))
circuit.append(Gates.CYGate( qr[1], qr[0] ))
circuit.append(Gates.SXdgGate( qr[1] ))
circuit.append(Gates.YGate( qr[0] ))
circuit.append(Gates.U3Gate(0.6932622610946984, 0.5005689189307869, 3.802023333380939)( qr[1] ))
circuit.append(Gates.CZGate( qr[0], qr[1] ))
circuit.append(Gates.CYGate( qr[1], qr[0] ))
circuit.append(Gates.U2Gate(1.5441062376251906, 1.6281357791932107)( qr[0] ))
circuit.append(Gates.CYGate( qr[0], qr[1] ))
circuit.append(Gates.CHGate( qr[0], qr[1] ))
circuit.append(Gates.PhaseGate(3.369665394386499)( qr[1] ))
circuit.append(Gates.HGate( qr[0] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(Gates.U1Gate(2.7233411978459645)( qr[0] ))
circuit.append(Gates.YGate( qr[0] ))
circuit.append(Gates.RXXGate(4.459276651579209)( qr[0], qr[1] ))
circuit.append(Gates.SXGate( qr[1] ))
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
