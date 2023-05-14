
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


qr = [cirq.NamedQubit('q' + str(i)) for i in range(6)]

p_2f6fa1 = Symbol('p_2f6fa1')
p_d2b7ff = Symbol('p_d2b7ff')
p_796036 = Symbol('p_796036')
p_deb987 = Symbol('p_deb987')
p_f98523 = Symbol('p_f98523')
p_31d9e7 = Symbol('p_31d9e7')
p_7d1017 = Symbol('p_7d1017')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_d2b7ff)( qr[4] ))
circuit.append(Gates.ZGate( qr[3] ))
circuit.append(Gates.CRZGate(4.2641612072511235)( qr[2], qr[4] ))
circuit.append(Gates.CUGate(p_2f6fa1, p_31d9e7, p_deb987, p_f98523)( qr[2], qr[3] ))
circuit.append(Gates.C3SXGate( qr[1], qr[4], qr[0], qr[2] ))
circuit.append(Gates.CCXGate( qr[1], qr[5], qr[0] ))
circuit.append(Gates.C3SXGate( qr[4], qr[3], qr[5], qr[0] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.RZZGate(5.017245588344839)( qr[0], qr[1] ))
subcircuit.append(Gates.iSwapGate( qr[3], qr[2] ))
subcircuit.append(Gates.XGate( qr[0] ))
subcircuit.append(Gates.CSXGate( qr[0], qr[1] ))
subcircuit.append(Gates.RCCXGate( qr[4], qr[5], qr[1] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.TGate( qr[4] ))
circuit.append(Gates.RCCXGate( qr[5], qr[3], qr[4] ))
circuit.append(Gates.SGate( qr[5] ))
circuit.append(Gates.CRZGate(4.167661441102218)( qr[1], qr[5] ))
circuit.append(Gates.RZGate(p_796036)( qr[1] ))
circuit.append(Gates.C3SXGate( qr[0], qr[2], qr[1], qr[3] ))
circuit.append(Gates.CU1Gate(3.2142159669963557)( qr[3], qr[0] ))
circuit.append(Gates.UGate(5.887184334931191, p_7d1017, 1.4112277317699358)( qr[5] ))
circuit.append(Gates.RZZGate(5.1829934776392745)( qr[0], qr[5] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))



circuit = cirq.resolve_parameters(circuit, {
    "p_2f6fa1": 0.5112149185250571,
    "p_d2b7ff": 6.163759533339787,
    "p_796036": 4.229610589867865,
    "p_deb987": 2.3864521352475245,
    "p_f98523": 5.987304452123941,
    "p_31d9e7": 5.897054719225356,
    "p_7d1017": 0.07157463504881167
}, recursive=True)
        



circuit = apply_transformations(circuit)






simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=1385)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

