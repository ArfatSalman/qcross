
import cirq
import qiskit
from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(5)]

p_ea6b64 = Symbol('p_ea6b64')
p_2e72b1 = Symbol('p_2e72b1')
p_ee580c = Symbol('p_ee580c')
p_6eeda0 = Symbol('p_6eeda0')
p_f65747 = Symbol('p_f65747')
p_18bd1c = Symbol('p_18bd1c')
p_ba0550 = Symbol('p_ba0550')
p_d56d65 = Symbol('p_d56d65')
p_01353d = Symbol('p_01353d')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_ea6b64)( qr[3] ))
circuit.append(Gates.SXdgGate( qr[2] ))
circuit.append(Gates.CSXGate( qr[1], qr[0] ))
circuit.append(Gates.ECRGate( qr[3], qr[2] ))
circuit.append(Gates.CRXGate(p_18bd1c)( qr[4], qr[3] ))
circuit.append(Gates.SGate( qr[0] ))
circuit.append(Gates.CRZGate(p_f65747)( qr[3], qr[4] ))
circuit.append(Gates.CHGate( qr[1], qr[4] ))
circuit.append(Gates.RYYGate(p_01353d)( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.TGate( qr[4] ))
circuit.append(Gates.CSXGate( qr[1], qr[4] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(Gates.SGate( qr[4] ))
circuit.append(Gates.CUGate(p_ee580c, p_2e72b1, p_ba0550, 3.865496458458116)( qr[1], qr[4] ))
circuit.append(Gates.RZGate(4.229610589867865)( qr[1] ))
circuit.append(Gates.RYYGate(5.398622178940033)( qr[0], qr[2] ))
circuit.append(Gates.CU1Gate(3.2142159669963557)( qr[3], qr[0] ))
circuit.append(Gates.UGate(p_6eeda0, 0.07157463504881167, p_d56d65)( qr[4] ))
circuit.append(Gates.CHGate( qr[2], qr[0] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))



circuit = cirq.resolve_parameters(circuit, {
    "p_ea6b64": 6.163759533339787,
    "p_2e72b1": 4.167661441102218,
    "p_ee580c": 5.708725119517347,
    "p_6eeda0": 5.887184334931191,
    "p_f65747": 1.0296448789776642,
    "p_18bd1c": 2.0099472182748075,
    "p_ba0550": 4.623446645668956,
    "p_d56d65": 1.4112277317699358,
    "p_01353d": 1.6723037552953224
}, recursive=True)
        








expanded_circuit = cirq.expand_composite(circuit)
qasm_from_qiskit = qiskit.QuantumCircuit.from_qasm_str(cirq.qasm(expanded_circuit)).qasm()
cirq_circuit_from_qiskit_qasm = circuit_from_qasm(qasm_from_qiskit)

# since, importing in cirq uses different qubit names, we need to change the qubit names
circuit_transformed = cirq_circuit_from_qiskit_qasm.transform_qubits(lambda q: cirq.NamedQubit(q.name.replace("q_", "q")))

cirq.testing.assert_circuits_with_terminal_measurements_are_equivalent(circuit_transformed, circuit)




simulator = cirq.DensityMatrixSimulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=979)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

