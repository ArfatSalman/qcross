
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


qr = [cirq.NamedQubit('q' + str(i)) for i in range(3)]

p_d5d30f = Symbol('p_d5d30f')
p_483362 = Symbol('p_483362')
p_c08e15 = Symbol('p_c08e15')
p_304ede = Symbol('p_304ede')
p_3c2ca3 = Symbol('p_3c2ca3')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_304ede)( qr[1] ))
circuit.append(Gates.CHGate( qr[2], qr[0] ))
circuit.append(Gates.SXdgGate( qr[2] ))
circuit.append(Gates.iSwapGate( qr[2], qr[1] ))
circuit.append(Gates.CSXGate( qr[1], qr[0] ))
circuit.append(Gates.XGate( qr[2] ))
circuit.append(Gates.SGate( qr[2] ))
circuit.append(Gates.SdgGate( qr[1] ))
circuit.append(Gates.CRXGate(p_d5d30f)( qr[0], qr[2] ))
circuit.append(Gates.SGate( qr[2] ))
circuit.append(Gates.CCXGate( qr[1], qr[0], qr[2] ))
circuit.append(Gates.CHGate( qr[2], qr[0] ))
circuit.append(Gates.CHGate( qr[1], qr[2] ))
circuit.append(Gates.RYYGate(p_483362)( qr[1], qr[0] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.TGate( qr[0] ))
circuit.append(Gates.ZGate( qr[1] ))
circuit.append(Gates.SGate( qr[2] ))
circuit.append(Gates.ECRGate( qr[2], qr[0] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.RCCXGate( qr[1], qr[0], qr[2] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(Gates.SdgGate( qr[2] ))
circuit.append(Gates.RCCXGate( qr[0], qr[2], qr[1] ))
circuit.append(Gates.CRZGate(p_c08e15)( qr[2], qr[1] ))
circuit.append(Gates.SGate( qr[2] ))
circuit.append(Gates.CRZGate(p_3c2ca3)( qr[2], qr[1] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))



circuit = cirq.resolve_parameters(circuit, {
    "p_d5d30f": 5.987304452123941,
    "p_483362": 1.6723037552953224,
    "p_c08e15": 4.167661441102218,
    "p_304ede": 6.163759533339787,
    "p_3c2ca3": 0.05525155902669336
}, recursive=True)
        



circuit = apply_transformations(circuit)






simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=489)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

