
import cirq
import qiskit
from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(2)]



circuit = cirq.Circuit()

circuit.append(Gates.SwapGate( qr[0], qr[1] ))
circuit.append(Gates.RZXGate(3.8834807859507263)( qr[1], qr[0] ))
circuit.append(Gates.SwapGate( qr[1], qr[0] ))
circuit.append(Gates.UGate(4.973624404177978, 1.450846828228022, 5.424728583609293)( qr[0] ))
circuit.append(Gates.CRXGate(3.510034154259637)( qr[1], qr[0] ))
circuit.append(Gates.RZXGate(1.9764943500940788)( qr[1], qr[0] ))
circuit.append(Gates.RXGate(1.444335936996841)( qr[1] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(Gates.UGate(0.7650180880812659, 1.1640465366080328, 3.351987550000961)( qr[1] ))
circuit.append(Gates.U2Gate(2.138082427163418, 5.230899032902529)( qr[1] ))
circuit.append(Gates.CPhaseGate(0.554577471370062)( qr[0], qr[1] ))
circuit.append(Gates.TGate( qr[1] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(Gates.CHGate( qr[1], qr[0] ))
circuit.append(Gates.U3Gate(0.9335631365840328, 4.520121169686029, 5.198491695816633)( qr[0] ))
circuit.append(Gates.SXdgGate( qr[1] ))
circuit.append(Gates.HGate( qr[1] ))
circuit.append(Gates.CRXGate(3.4913681561376415)( qr[0], qr[1] ))
circuit.append(Gates.SXdgGate( qr[1] ))
circuit.append(Gates.SGate( qr[0] ))
circuit.append(Gates.CSXGate( qr[1], qr[0] ))
circuit.append(Gates.CSXGate( qr[1], qr[0] ))
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
