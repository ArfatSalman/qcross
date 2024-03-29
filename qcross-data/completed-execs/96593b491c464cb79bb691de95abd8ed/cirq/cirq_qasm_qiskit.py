
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


qr = [cirq.NamedQubit('q' + str(i)) for i in range(2)]



circuit = cirq.Circuit()

circuit.append(Gates.RZZGate(6.163759533339787)( qr[1], qr[0] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.ECRGate( qr[1], qr[0] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(Gates.iSwapGate( qr[1], qr[0] ))
circuit.append(Gates.CSXGate( qr[0], qr[1] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.RYYGate(1.977559237989846)( qr[0], qr[1] ))
circuit.append(Gates.TGate( qr[1] ))
circuit.append(Gates.SXGate( qr[1] ))
circuit.append(Gates.CRXGate(5.987304452123941)( qr[0], qr[1] ))
circuit.append(Gates.CHGate( qr[0], qr[1] ))
circuit.append(Gates.CRZGate(2.2498881927557752)( qr[0], qr[1] ))
circuit.append(Gates.SXGate( qr[1] ))
circuit.append(Gates.RZGate(5.320621737498446)( qr[1] ))
circuit.append(Gates.RZGate(5.512260524440591)( qr[1] ))
circuit.append(Gates.CU1Gate(1.6723037552953224)( qr[0], qr[1] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.RZZGate(6.086884486572108)( qr[0], qr[1] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(Gates.RYYGate(3.3705408413231095)( qr[0], qr[1] ))
circuit.append(Gates.SXGate( qr[1] ))
circuit.append(Gates.RZGate(5.190931186022931)( qr[1] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.RYYGate(5.167261531657622)( qr[1], qr[0] ))
circuit.append(Gates.SGate( qr[0] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.RXGate(6.221353754875494)( qr[0] ))
subcircuit.append(Gates.CSXGate( qr[1], qr[0] ))
subcircuit.append(Gates.CYGate( qr[1], qr[0] ))
subcircuit.append(Gates.HGate( qr[1] ))
subcircuit.append(Gates.SXGate( qr[1] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.CRZGate(4.167661441102218)( qr[1], qr[0] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))






circuit = apply_transformations(circuit)




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

