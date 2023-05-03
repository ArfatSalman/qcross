
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

p_07b864 = Symbol('p_07b864')
p_12832b = Symbol('p_12832b')
p_aa27f8 = Symbol('p_aa27f8')
p_5f4a74 = Symbol('p_5f4a74')
p_d0f83e = Symbol('p_d0f83e')
p_6afe18 = Symbol('p_6afe18')
p_6d8eba = Symbol('p_6d8eba')
p_c41e19 = Symbol('p_c41e19')
p_431464 = Symbol('p_431464')
p_96609c = Symbol('p_96609c')
p_990bb6 = Symbol('p_990bb6')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_990bb6)( qr[5] ))
circuit.append(Gates.ZGate( qr[4] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.CRXGate(p_12832b)( qr[0], qr[3] ))
circuit.append(Gates.C3SXGate( qr[4], qr[2], qr[6], qr[0] ))
circuit.append(Gates.CHGate( qr[5], qr[4] ))
circuit.append(Gates.C3SXGate( qr[2], qr[0], qr[6], qr[3] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.ECRGate( qr[4], qr[1] ))
circuit.append(Gates.SdgGate( qr[4] ))
circuit.append(Gates.RCCXGate( qr[0], qr[3], qr[2] ))
circuit.append(Gates.SGate( qr[6] ))
circuit.append(Gates.RZGate(p_6afe18)( qr[6] ))
circuit.append(Gates.C3SXGate( qr[2], qr[0], qr[6], qr[1] ))
circuit.append(Gates.CU1Gate(p_07b864)( qr[5], qr[2] ))
circuit.append(Gates.CRXGate(p_431464)( qr[5], qr[4] ))
circuit.append(Gates.CHGate( qr[5], qr[2] ))
circuit.append(Gates.C3SXGate( qr[0], qr[2], qr[1], qr[5] ))
circuit.append(Gates.CSXGate( qr[2], qr[0] ))
circuit.append(Gates.ZGate( qr[3] ))
circuit.append(Gates.CRZGate(p_d0f83e)( qr[2], qr[4] ))
circuit.append(Gates.CU1Gate(4.028174522740928)( qr[6], qr[5] ))
circuit.append(Gates.C3SXGate( qr[0], qr[2], qr[3], qr[5] ))
circuit.append(Gates.CRZGate(p_5f4a74)( qr[4], qr[0] ))
circuit.append(Gates.U2Gate(p_6d8eba, p_c41e19)( qr[0] ))
circuit.append(Gates.TGate( qr[4] ))
circuit.append(Gates.SdgGate( qr[2] ))
circuit.append(Gates.RZZGate(p_96609c)( qr[1], qr[5] ))
circuit.append(Gates.TGate( qr[5] ))
circuit.append(Gates.RYYGate(p_aa27f8)( qr[5], qr[0] ))
circuit.append(cirq.measure(qr[2], key='cr0'))
circuit.append(cirq.measure(qr[6], key='cr1'))
circuit.append(cirq.measure(qr[0], key='cr2'))
circuit.append(cirq.measure(qr[1], key='cr3'))
circuit.append(cirq.measure(qr[5], key='cr4'))
circuit.append(cirq.measure(qr[3], key='cr5'))
circuit.append(cirq.measure(qr[4], key='cr6'))



circuit = cirq.resolve_parameters(circuit, {
    "p_07b864": 3.2142159669963557,
    "p_12832b": 2.0099472182748075,
    "p_aa27f8": 1.9669252191306448,
    "p_5f4a74": 2.586208953975239,
    "p_d0f83e": 4.833923139882297,
    "p_6afe18": 4.229610589867865,
    "p_6d8eba": 2.5163050709890156,
    "p_c41e19": 2.1276323672732023,
    "p_431464": 5.94477504571567,
    "p_96609c": 3.950837470808744,
    "p_990bb6": 6.163759533339787
}, recursive=True)
        



circuit = apply_transformations(circuit)






simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=1959)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

