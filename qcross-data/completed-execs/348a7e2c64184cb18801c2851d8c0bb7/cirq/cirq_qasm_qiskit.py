
import cirq
import qiskit
from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np

def apply_transformations(circuit, context=None):
    optimized_circuit = cirq.expand_composite(circuit)

    optimized_circuit = cirq.defer_measurements(optimized_circuit)

    optimized_circuit = cirq.merge_k_qubit_unitaries(
                optimized_circuit, k=2, rewriter=lambda op: op.with_tags("merged"), context=context)

    optimized_circuit = cirq.drop_empty_moments(optimized_circuit)

    optimized_circuit = cirq.eject_z(optimized_circuit, eject_parameterized=True)

    optimized_circuit = cirq.eject_phased_paulis(optimized_circuit, eject_parameterized=True)

    optimized_circuit = cirq.drop_negligible_operations(optimized_circuit)

    optimized_circuit = cirq.stratified_circuit(optimized_circuit)

    optimized_circuit = cirq.synchronize_terminal_measurements(optimized_circuit)

    # Assert the original and optimized circuit are equivalent.
    cirq.testing.assert_circuits_with_terminal_measurements_are_equivalent(
        circuit, optimized_circuit
    )

    return optimized_circuit


qr = [cirq.NamedQubit('q' + str(i)) for i in range(8)]

p_143887 = Symbol('p_143887')
p_72a534 = Symbol('p_72a534')
p_082ec3 = Symbol('p_082ec3')
p_fd33bb = Symbol('p_fd33bb')
p_c40958 = Symbol('p_c40958')
p_106180 = Symbol('p_106180')
p_083e1c = Symbol('p_083e1c')
p_36e2fe = Symbol('p_36e2fe')
p_f20bd4 = Symbol('p_f20bd4')
p_ec90c9 = Symbol('p_ec90c9')
p_2bbfa0 = Symbol('p_2bbfa0')
p_bb3cbe = Symbol('p_bb3cbe')
p_8baad8 = Symbol('p_8baad8')
p_057fbf = Symbol('p_057fbf')
p_0927f4 = Symbol('p_0927f4')
p_b8acf2 = Symbol('p_b8acf2')
p_1e860b = Symbol('p_1e860b')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_72a534)( qr[4] ))
circuit.append(Gates.ZGate( qr[6] ))
circuit.append(Gates.XGate( qr[6] ))
circuit.append(Gates.CRXGate(p_36e2fe)( qr[0], qr[6] ))
circuit.append(Gates.CRZGate(p_bb3cbe)( qr[1], qr[6] ))
circuit.append(Gates.C3SXGate( qr[0], qr[7], qr[6], qr[3] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.RYYGate(p_057fbf)( qr[6], qr[7] ))
circuit.append(Gates.CRZGate(p_0927f4)( qr[1], qr[7] ))
circuit.append(Gates.RZGate(p_b8acf2)( qr[1] ))
circuit.append(Gates.SXGate( qr[0] ))
circuit.append(Gates.CU1Gate(p_143887)( qr[4], qr[0] ))
circuit.append(Gates.CRXGate(p_ec90c9)( qr[6], qr[4] ))
circuit.append(Gates.RZZGate(p_fd33bb)( qr[7], qr[0] ))
circuit.append(Gates.CSXGate( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[6] ))
circuit.append(Gates.RZGate(p_082ec3)( qr[4] ))
circuit.append(Gates.CRXGate(p_106180)( qr[0], qr[3] ))
circuit.append(Gates.CUGate(p_8baad8, p_2bbfa0, p_c40958, p_1e860b)( qr[6], qr[2] ))
circuit.append(Gates.U2Gate(p_f20bd4, p_083e1c)( qr[2] ))
circuit.append(Gates.TGate( qr[6] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))
circuit.append(cirq.measure(qr[7], key='cr7'))



circuit = cirq.resolve_parameters(circuit, {
    "p_143887": 3.2142159669963557,
    "p_72a534": 6.163759533339787,
    "p_082ec3": 3.775592041307464,
    "p_fd33bb": 5.1829934776392745,
    "p_c40958": 3.1562533916051736,
    "p_106180": 0.7279391018916035,
    "p_083e1c": 2.1276323672732023,
    "p_36e2fe": 5.987304452123941,
    "p_f20bd4": 2.5163050709890156,
    "p_ec90c9": 5.94477504571567,
    "p_2bbfa0": 5.0063780207098425,
    "p_bb3cbe": 1.0296448789776642,
    "p_8baad8": 5.03147076606842,
    "p_057fbf": 1.740253089260498,
    "p_0927f4": 4.167661441102218,
    "p_b8acf2": 4.229610589867865,
    "p_1e860b": 4.940217775579305
}, recursive=True)
        



circuit = apply_transformations(circuit)




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
    from qcross.utils import display_results
    display_results( {"result": RESULT })

