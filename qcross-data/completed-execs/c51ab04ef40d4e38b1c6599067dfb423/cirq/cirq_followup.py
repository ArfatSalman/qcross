
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


qr = [cirq.NamedQubit('q' + str(i)) for i in range(5)]

p_236385 = Symbol('p_236385')
p_500aa6 = Symbol('p_500aa6')
p_8f916e = Symbol('p_8f916e')
p_8aac37 = Symbol('p_8aac37')
p_9f7fb1 = Symbol('p_9f7fb1')
p_3176a0 = Symbol('p_3176a0')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(6.163759533339787)( qr[3] ))
circuit.append(Gates.SXdgGate( qr[2] ))
circuit.append(Gates.CSXGate( qr[1], qr[0] ))
circuit.append(Gates.ECRGate( qr[3], qr[2] ))
circuit.append(Gates.CRXGate(p_3176a0)( qr[4], qr[3] ))
circuit.append(Gates.SGate( qr[0] ))
circuit.append(Gates.CRZGate(1.0296448789776642)( qr[3], qr[4] ))
circuit.append(Gates.CHGate( qr[1], qr[4] ))
circuit.append(Gates.RYYGate(1.6723037552953224)( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.TGate( qr[4] ))
circuit.append(Gates.CSXGate( qr[1], qr[4] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(Gates.SGate( qr[4] ))
circuit.append(Gates.CUGate(5.708725119517347, 4.167661441102218, p_8aac37, 3.865496458458116)( qr[1], qr[4] ))
circuit.append(Gates.RZGate(p_8f916e)( qr[1] ))
circuit.append(Gates.RYYGate(5.398622178940033)( qr[0], qr[2] ))
circuit.append(Gates.CU1Gate(3.2142159669963557)( qr[3], qr[0] ))
circuit.append(Gates.UGate(p_9f7fb1, p_236385, p_500aa6)( qr[4] ))
circuit.append(Gates.CHGate( qr[2], qr[0] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.SGate( qr[2] ))
circuit.append(Gates.CSXGate( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[3] ))
circuit.append(Gates.CHGate( qr[0], qr[4] ))
circuit.append(Gates.CHGate( qr[0], qr[1] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))



circuit = cirq.resolve_parameters(circuit, {
    "p_236385": 0.07157463504881167,
    "p_500aa6": 1.4112277317699358,
    "p_8f916e": 4.229610589867865,
    "p_8aac37": 4.623446645668956,
    "p_9f7fb1": 5.887184334931191,
    "p_3176a0": 2.0099472182748075
}, recursive=True)
        



circuit = apply_transformations(circuit)






simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=979)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

