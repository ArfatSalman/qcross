
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


qr = [cirq.NamedQubit('q' + str(i)) for i in range(7)]

p_2e68f3 = Symbol('p_2e68f3')
p_f3b6b3 = Symbol('p_f3b6b3')
p_02e0d1 = Symbol('p_02e0d1')
p_bdd144 = Symbol('p_bdd144')
p_031c73 = Symbol('p_031c73')
p_9bff3f = Symbol('p_9bff3f')
p_d48307 = Symbol('p_d48307')
p_cbf48f = Symbol('p_cbf48f')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_02e0d1)( qr[4] ))
circuit.append(Gates.ZGate( qr[6] ))
circuit.append(Gates.XGate( qr[3] ))
circuit.append(Gates.CRXGate(2.0099472182748075)( qr[2], qr[5] ))
circuit.append(Gates.C3SXGate( qr[6], qr[0], qr[1], qr[2] ))
circuit.append(Gates.CHGate( qr[4], qr[6] ))
circuit.append(Gates.C3SXGate( qr[0], qr[2], qr[1], qr[5] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.ECRGate( qr[6], qr[3] ))
circuit.append(Gates.SdgGate( qr[6] ))
circuit.append(Gates.RCCXGate( qr[2], qr[5], qr[0] ))
circuit.append(Gates.SGate( qr[1] ))
circuit.append(Gates.RZGate(p_2e68f3)( qr[1] ))
circuit.append(Gates.C3SXGate( qr[0], qr[2], qr[1], qr[3] ))
circuit.append(Gates.CU1Gate(p_d48307)( qr[4], qr[0] ))
circuit.append(Gates.CRXGate(5.94477504571567)( qr[4], qr[6] ))
circuit.append(Gates.CHGate( qr[4], qr[0] ))
circuit.append(Gates.C3SXGate( qr[2], qr[0], qr[3], qr[4] ))
circuit.append(Gates.CSXGate( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[5] ))
circuit.append(Gates.CRZGate(p_bdd144)( qr[0], qr[6] ))
circuit.append(Gates.CU1Gate(p_9bff3f)( qr[1], qr[4] ))
circuit.append(Gates.C3SXGate( qr[2], qr[0], qr[5], qr[4] ))
circuit.append(Gates.CRZGate(p_f3b6b3)( qr[6], qr[2] ))
circuit.append(Gates.U2Gate(2.5163050709890156, p_cbf48f)( qr[2] ))
circuit.append(Gates.TGate( qr[6] ))
circuit.append(Gates.SdgGate( qr[0] ))
circuit.append(Gates.RZZGate(3.950837470808744)( qr[3], qr[4] ))
circuit.append(Gates.TGate( qr[4] ))
circuit.append(Gates.RYYGate(p_031c73)( qr[4], qr[2] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))



circuit = cirq.resolve_parameters(circuit, {
    "p_2e68f3": 4.229610589867865,
    "p_f3b6b3": 2.586208953975239,
    "p_02e0d1": 6.163759533339787,
    "p_bdd144": 4.833923139882297,
    "p_031c73": 1.9669252191306448,
    "p_9bff3f": 4.028174522740928,
    "p_d48307": 3.2142159669963557,
    "p_cbf48f": 2.1276323672732023
}, recursive=True)
        



circuit = apply_transformations(circuit)




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

