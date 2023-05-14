
import cirq

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


qr = [cirq.NamedQubit('q' + str(i)) for i in range(10)]

p_fc0ce7 = Symbol('p_fc0ce7')
p_532c13 = Symbol('p_532c13')
p_96cba0 = Symbol('p_96cba0')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(6.163759533339787)( qr[0] ))
circuit.append(Gates.CRZGate(p_fc0ce7)( qr[7], qr[0] ))
circuit.append(Gates.CRXGate(5.987304452123941)( qr[5], qr[9] ))
circuit.append(Gates.CCXGate( qr[3], qr[4], qr[9] ))
circuit.append(Gates.ZGate( qr[8] ))
circuit.append(Gates.TGate( qr[4] ))
circuit.append(Gates.XGate( qr[6] ))
circuit.append(Gates.CRZGate(4.167661441102218)( qr[5], qr[7] ))
circuit.append(Gates.RZGate(4.229610589867865)( qr[5] ))
circuit.append(Gates.SXGate( qr[8] ))
circuit.append(Gates.CSXGate( qr[1], qr[6] ))
circuit.append(Gates.CCXGate( qr[1], qr[4], qr[3] ))
circuit.append(Gates.C3SXGate( qr[8], qr[1], qr[2], qr[4] ))
circuit.append(Gates.CSXGate( qr[2], qr[8] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.CHGate( qr[9], qr[5] ))
circuit.append(Gates.CSXGate( qr[8], qr[2] ))
circuit.append(Gates.CRZGate(p_96cba0)( qr[5], qr[8] ))
circuit.append(Gates.U2Gate(p_532c13, 2.1276323672732023)( qr[8] ))
circuit.append(Gates.TGate( qr[2] ))
circuit.append(Gates.SXdgGate( qr[4] ))
circuit.append(Gates.TGate( qr[6] ))
circuit.append(Gates.RZGate(5.014941143947427)( qr[5] ))
circuit.append(cirq.measure(qr[2], key='cr0'))
circuit.append(cirq.measure(qr[5], key='cr1'))
circuit.append(cirq.measure(qr[8], key='cr2'))
circuit.append(cirq.measure(qr[0], key='cr3'))
circuit.append(cirq.measure(qr[1], key='cr4'))
circuit.append(cirq.measure(qr[3], key='cr5'))
circuit.append(cirq.measure(qr[7], key='cr6'))
circuit.append(cirq.measure(qr[9], key='cr7'))
circuit.append(cirq.measure(qr[6], key='cr8'))
circuit.append(cirq.measure(qr[4], key='cr9'))



circuit = cirq.resolve_parameters(circuit, {
    "p_fc0ce7": 4.2641612072511235,
    "p_532c13": 2.5163050709890156,
    "p_96cba0": 2.586208953975239
}, recursive=True)
        



circuit = apply_transformations(circuit)






simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=5542)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7', 'cr8', 'cr9'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

