
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


qr = [cirq.NamedQubit('q' + str(i)) for i in range(2)]

p_492844 = Symbol('p_492844')
p_730e02 = Symbol('p_730e02')
p_57eb86 = Symbol('p_57eb86')
p_66f8bd = Symbol('p_66f8bd')
p_413130 = Symbol('p_413130')
p_00b361 = Symbol('p_00b361')
p_37a10a = Symbol('p_37a10a')
p_8594a5 = Symbol('p_8594a5')
p_1a08ce = Symbol('p_1a08ce')
p_ec5eaf = Symbol('p_ec5eaf')
p_dd7bb0 = Symbol('p_dd7bb0')

circuit = cirq.Circuit()

circuit.append(Gates.RZZGate(p_492844)( qr[1], qr[0] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.ECRGate( qr[1], qr[0] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(Gates.iSwapGate( qr[1], qr[0] ))
circuit.append(Gates.CSXGate( qr[0], qr[1] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.RYYGate(p_1a08ce)( qr[0], qr[1] ))
circuit.append(Gates.TGate( qr[1] ))
circuit.append(Gates.SXGate( qr[1] ))
circuit.append(Gates.CRXGate(p_730e02)( qr[0], qr[1] ))
circuit.append(Gates.CHGate( qr[0], qr[1] ))
circuit.append(Gates.CRZGate(p_37a10a)( qr[0], qr[1] ))
circuit.append(Gates.SXGate( qr[1] ))
circuit.append(Gates.RZGate(p_00b361)( qr[1] ))
circuit.append(Gates.RZGate(p_413130)( qr[1] ))
circuit.append(Gates.CU1Gate(p_57eb86)( qr[0], qr[1] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.RZZGate(p_8594a5)( qr[0], qr[1] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(Gates.RYYGate(p_66f8bd)( qr[0], qr[1] ))
circuit.append(Gates.SXGate( qr[1] ))
circuit.append(Gates.RZGate(p_ec5eaf)( qr[1] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.RYYGate(p_dd7bb0)( qr[1], qr[0] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))



circuit = cirq.resolve_parameters(circuit, {
    "p_492844": 6.163759533339787,
    "p_730e02": 5.987304452123941,
    "p_57eb86": 1.6723037552953224,
    "p_66f8bd": 3.3705408413231095,
    "p_413130": 5.512260524440591,
    "p_00b361": 5.320621737498446,
    "p_37a10a": 2.2498881927557752,
    "p_8594a5": 6.086884486572108,
    "p_1a08ce": 1.977559237989846,
    "p_ec5eaf": 5.190931186022931,
    "p_dd7bb0": 5.167261531657622
}, recursive=True)
        



circuit = apply_transformations(circuit)






simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=346)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

