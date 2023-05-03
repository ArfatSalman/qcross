
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

p_219d62 = Symbol('p_219d62')
p_f67f84 = Symbol('p_f67f84')
p_b9edf2 = Symbol('p_b9edf2')
p_cac0af = Symbol('p_cac0af')
p_c04ae3 = Symbol('p_c04ae3')
p_7ec521 = Symbol('p_7ec521')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_c04ae3)( qr[3] ))
circuit.append(Gates.SXdgGate( qr[2] ))
circuit.append(Gates.CSXGate( qr[1], qr[0] ))
circuit.append(Gates.ECRGate( qr[3], qr[2] ))
circuit.append(Gates.CRXGate(2.0099472182748075)( qr[4], qr[3] ))
circuit.append(Gates.SGate( qr[0] ))
circuit.append(Gates.CRZGate(1.0296448789776642)( qr[3], qr[4] ))
circuit.append(Gates.CHGate( qr[1], qr[4] ))
circuit.append(Gates.RYYGate(p_219d62)( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.TGate( qr[4] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.CU1Gate(p_cac0af)( qr[2], qr[4] ))
subcircuit.append(Gates.CU3Gate(p_b9edf2, 2.6636908506222836, 6.221353754875494)( qr[4], qr[1] ))
subcircuit.append(Gates.IGate( qr[1] ))
subcircuit.append(Gates.IGate( qr[0] ))
subcircuit.append(Gates.ECRGate( qr[3], qr[1] ))
subcircuit.append(Gates.UGate(p_7ec521, 2.3568871696687452, 6.011900464835247)( qr[2] ))
subcircuit.append(Gates.CSwapGate( qr[0], qr[4], qr[1] ))
subcircuit.append(Gates.HGate( qr[0] ))
subcircuit.append(Gates.CRXGate(p_f67f84)( qr[2], qr[0] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.CSXGate( qr[1], qr[4] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))



circuit = cirq.resolve_parameters(circuit, {
    "p_219d62": 1.6723037552953224,
    "p_f67f84": 5.091930552861214,
    "p_b9edf2": 3.865496458458116,
    "p_cac0af": 4.501598818751339,
    "p_c04ae3": 6.163759533339787,
    "p_7ec521": 3.5173414605326783
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

