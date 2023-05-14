
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


qr = [cirq.NamedQubit('q' + str(i)) for i in range(9)]

p_299687 = Symbol('p_299687')
p_2d28aa = Symbol('p_2d28aa')
p_efba95 = Symbol('p_efba95')
p_c3019d = Symbol('p_c3019d')
p_0fe9c2 = Symbol('p_0fe9c2')
p_9640e8 = Symbol('p_9640e8')
p_0e9aa7 = Symbol('p_0e9aa7')
p_101f6d = Symbol('p_101f6d')
p_2ef906 = Symbol('p_2ef906')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_2d28aa)( qr[8] ))
circuit.append(Gates.CSXGate( qr[2], qr[4] ))
circuit.append(Gates.CUGate(p_9640e8, 5.897054719225356, p_2ef906, p_0fe9c2)( qr[0], qr[6] ))
circuit.append(Gates.SdgGate( qr[1] ))
circuit.append(Gates.C3SXGate( qr[0], qr[8], qr[7], qr[5] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.XGate( qr[5] ))
circuit.append(Gates.SGate( qr[0] ))
circuit.append(Gates.SGate( qr[8] ))
circuit.append(Gates.C3SXGate( qr[1], qr[3], qr[2], qr[0] ))
circuit.append(Gates.SXGate( qr[0] ))
circuit.append(Gates.CU1Gate(p_299687)( qr[8], qr[3] ))
circuit.append(Gates.CRZGate(p_c3019d)( qr[5], qr[8] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.CSXGate( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[7] ))
circuit.append(Gates.CHGate( qr[6], qr[1] ))
circuit.append(Gates.CSXGate( qr[3], qr[0] ))
circuit.append(Gates.CRZGate(p_efba95)( qr[1], qr[2] ))
circuit.append(Gates.U2Gate(p_0e9aa7, p_101f6d)( qr[2] ))
circuit.append(Gates.TGate( qr[8] ))
circuit.append(Gates.CCXGate( qr[0], qr[6], qr[1] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))
circuit.append(cirq.measure(qr[7], key='cr7'))
circuit.append(cirq.measure(qr[8], key='cr8'))



circuit = cirq.resolve_parameters(circuit, {
    "p_299687": 3.2142159669963557,
    "p_2d28aa": 6.163759533339787,
    "p_efba95": 2.586208953975239,
    "p_c3019d": 1.4112277317699358,
    "p_0fe9c2": 5.987304452123941,
    "p_9640e8": 0.5112149185250571,
    "p_0e9aa7": 2.5163050709890156,
    "p_101f6d": 2.1276323672732023,
    "p_2ef906": 2.3864521352475245
}, recursive=True)
        



circuit = apply_transformations(circuit)






simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=3919)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7', 'cr8'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })
