
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


qr = [cirq.NamedQubit('q' + str(i)) for i in range(11)]

p_3603f7 = Symbol('p_3603f7')
p_fd786b = Symbol('p_fd786b')
p_b354cf = Symbol('p_b354cf')
p_a0ebfc = Symbol('p_a0ebfc')
p_27de98 = Symbol('p_27de98')
p_95a7b3 = Symbol('p_95a7b3')
p_91f56a = Symbol('p_91f56a')
p_317aec = Symbol('p_317aec')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_95a7b3)( qr[3] ))
circuit.append(Gates.CRZGate(4.2641612072511235)( qr[6], qr[2] ))
circuit.append(Gates.ZGate( qr[1] ))
circuit.append(Gates.CCXGate( qr[5], qr[9], qr[7] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.XGate( qr[7] ))
circuit.append(Gates.RCCXGate( qr[10], qr[6], qr[8] ))
circuit.append(Gates.RZGate(4.229610589867865)( qr[0] ))
circuit.append(Gates.CCXGate( qr[7], qr[10], qr[2] ))
circuit.append(Gates.SdgGate( qr[7] ))
circuit.append(Gates.U2Gate(4.214504315296764, p_fd786b)( qr[10] ))
circuit.append(Gates.CSXGate( qr[3], qr[2] ))
circuit.append(Gates.CHGate( qr[0], qr[7] ))
circuit.append(Gates.CU1Gate(4.028174522740928)( qr[9], qr[0] ))
circuit.append(Gates.RZGate(p_3603f7)( qr[6] ))
circuit.append(Gates.U2Gate(p_27de98, p_317aec)( qr[2] ))
circuit.append(Gates.TGate( qr[0] ))
circuit.append(Gates.RZZGate(3.950837470808744)( qr[4], qr[0] ))
circuit.append(Gates.TGate( qr[0] ))
circuit.append(Gates.TGate( qr[1] ))
circuit.append(Gates.SXdgGate( qr[5] ))
circuit.append(Gates.RZGate(4.722103101046168)( qr[2] ))
circuit.append(Gates.CRZGate(p_91f56a)( qr[5], qr[3] ))
circuit.append(Gates.CU1Gate(p_a0ebfc)( qr[3], qr[8] ))
circuit.append(Gates.SXdgGate( qr[1] ))
circuit.append(Gates.RZGate(p_b354cf)( qr[6] ))
circuit.append(Gates.XGate( qr[8] ))
circuit.append(Gates.CSXGate( qr[7], qr[0] ))
circuit.append(Gates.CU1Gate(3.631024984774394)( qr[10], qr[7] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))
circuit.append(cirq.measure(qr[7], key='cr7'))
circuit.append(cirq.measure(qr[8], key='cr8'))
circuit.append(cirq.measure(qr[9], key='cr9'))
circuit.append(cirq.measure(qr[10], key='cr10'))



circuit = cirq.resolve_parameters(circuit, {
    "p_3603f7": 5.0063780207098425,
    "p_fd786b": 4.6235667602042065,
    "p_b354cf": 3.6614081973587154,
    "p_a0ebfc": 2.5476776328466872,
    "p_27de98": 2.5163050709890156,
    "p_95a7b3": 6.163759533339787,
    "p_91f56a": 0.6393443962862078,
    "p_317aec": 2.1276323672732023
}, recursive=True)
        



circuit = apply_transformations(circuit)




expanded_circuit = cirq.expand_composite(circuit)
qasm_from_qiskit = qiskit.QuantumCircuit.from_qasm_str(cirq.qasm(expanded_circuit)).qasm()
cirq_circuit_from_qiskit_qasm = circuit_from_qasm(qasm_from_qiskit)

# since, importing in cirq uses different qubit names, we need to change the qubit names
circuit_transformed = cirq_circuit_from_qiskit_qasm.transform_qubits(lambda q: cirq.NamedQubit(q.name.replace("q_", "q")))

cirq.testing.assert_circuits_with_terminal_measurements_are_equivalent(circuit_transformed, circuit)




simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=7838)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7', 'cr8', 'cr9', 'cr10'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

