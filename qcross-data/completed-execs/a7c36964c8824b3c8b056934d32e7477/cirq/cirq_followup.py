
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

p_4f8db3 = Symbol('p_4f8db3')
p_daae8b = Symbol('p_daae8b')
p_89f9ae = Symbol('p_89f9ae')
p_6f799f = Symbol('p_6f799f')
p_25d5a8 = Symbol('p_25d5a8')
p_eadd70 = Symbol('p_eadd70')
p_efceeb = Symbol('p_efceeb')
p_0cd2a2 = Symbol('p_0cd2a2')
p_574806 = Symbol('p_574806')
p_2907ce = Symbol('p_2907ce')
p_a8217e = Symbol('p_a8217e')
p_cf4aa0 = Symbol('p_cf4aa0')
p_a87faa = Symbol('p_a87faa')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_0cd2a2)( qr[3] ))
circuit.append(Gates.SXdgGate( qr[2] ))
circuit.append(Gates.CSXGate( qr[1], qr[0] ))
circuit.append(Gates.ECRGate( qr[3], qr[2] ))
circuit.append(Gates.CRXGate(p_a8217e)( qr[4], qr[3] ))
circuit.append(Gates.SGate( qr[0] ))
circuit.append(Gates.CRZGate(p_25d5a8)( qr[3], qr[4] ))
circuit.append(Gates.CHGate( qr[1], qr[4] ))
circuit.append(Gates.RYYGate(p_a87faa)( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.TGate( qr[4] ))
circuit.append(Gates.CSXGate( qr[1], qr[4] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(Gates.SGate( qr[4] ))
circuit.append(Gates.CUGate(p_6f799f, 4.167661441102218, 4.623446645668956, p_daae8b)( qr[1], qr[4] ))
circuit.append(Gates.RZGate(p_4f8db3)( qr[1] ))
circuit.append(Gates.RYYGate(p_efceeb)( qr[0], qr[2] ))
circuit.append(Gates.CU1Gate(p_574806)( qr[3], qr[0] ))
circuit.append(Gates.UGate(5.887184334931191, 0.07157463504881167, p_89f9ae)( qr[4] ))
circuit.append(Gates.CHGate( qr[2], qr[0] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.SGate( qr[2] ))
circuit.append(Gates.CSXGate( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[3] ))
circuit.append(Gates.CHGate( qr[0], qr[4] ))
circuit.append(Gates.CHGate( qr[0], qr[1] ))
circuit.append(Gates.CU1Gate(p_cf4aa0)( qr[0], qr[3] ))
circuit.append(Gates.RCCXGate( qr[0], qr[3], qr[1] ))
circuit.append(Gates.CUGate(5.03147076606842, p_eadd70, p_2907ce, 4.940217775579305)( qr[4], qr[3] ))
circuit.append(Gates.CRZGate(3.839241945509346)( qr[2], qr[1] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))



circuit = cirq.resolve_parameters(circuit, {
    "p_4f8db3": 4.229610589867865,
    "p_daae8b": 3.865496458458116,
    "p_89f9ae": 1.4112277317699358,
    "p_6f799f": 5.708725119517347,
    "p_25d5a8": 1.0296448789776642,
    "p_eadd70": 5.0063780207098425,
    "p_efceeb": 5.398622178940033,
    "p_0cd2a2": 6.163759533339787,
    "p_574806": 3.2142159669963557,
    "p_2907ce": 3.1562533916051736,
    "p_a8217e": 2.0099472182748075,
    "p_cf4aa0": 4.028174522740928,
    "p_a87faa": 1.6723037552953224
}, recursive=True)
        



circuit = apply_transformations(circuit)






simulator = cirq.DensityMatrixSimulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=979)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

