
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


qr = [cirq.NamedQubit('q' + str(i)) for i in range(7)]

p_b96123 = Symbol('p_b96123')
p_016d54 = Symbol('p_016d54')
p_99427e = Symbol('p_99427e')
p_93d5ac = Symbol('p_93d5ac')
p_7691c4 = Symbol('p_7691c4')
p_7ec4f4 = Symbol('p_7ec4f4')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(6.163759533339787)( qr[4] ))
circuit.append(Gates.ZGate( qr[6] ))
circuit.append(Gates.XGate( qr[3] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.HGate( qr[0] ))
subcircuit.append(Gates.RZZGate(p_99427e)( qr[0], qr[5] ))
subcircuit.append(Gates.CRZGate(p_016d54)( qr[0], qr[5] ))
subcircuit.append(Gates.CSXGate( qr[4], qr[0] ))
subcircuit.append(Gates.SwapGate( qr[1], qr[4] ))
subcircuit.append(Gates.RYYGate(0.5501056885328758)( qr[2], qr[0] ))
subcircuit.append(Gates.SXdgGate( qr[5] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.CRXGate(p_93d5ac)( qr[2], qr[5] ))
circuit.append(Gates.C3SXGate( qr[6], qr[0], qr[1], qr[2] ))
circuit.append(Gates.CHGate( qr[4], qr[6] ))
circuit.append(Gates.C3SXGate( qr[0], qr[2], qr[1], qr[5] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.ECRGate( qr[6], qr[3] ))
circuit.append(Gates.SdgGate( qr[6] ))
circuit.append(Gates.RCCXGate( qr[2], qr[5], qr[0] ))
circuit.append(Gates.SGate( qr[1] ))
circuit.append(Gates.RZGate(p_b96123)( qr[1] ))
circuit.append(Gates.C3SXGate( qr[0], qr[2], qr[1], qr[3] ))
circuit.append(Gates.CU1Gate(p_7691c4)( qr[4], qr[0] ))
circuit.append(Gates.CRXGate(p_7ec4f4)( qr[4], qr[6] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))



circuit = cirq.resolve_parameters(circuit, {
    "p_b96123": 4.229610589867865,
    "p_016d54": 2.008796895454228,
    "p_99427e": 5.017245588344839,
    "p_93d5ac": 2.0099472182748075,
    "p_7691c4": 3.2142159669963557,
    "p_7ec4f4": 5.94477504571567
}, recursive=True)
        



circuit = apply_transformations(circuit)






simulator = cirq.DensityMatrixSimulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=1959)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })
