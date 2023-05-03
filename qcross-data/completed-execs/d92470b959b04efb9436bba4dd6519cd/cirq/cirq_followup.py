
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


qr = [cirq.NamedQubit('q' + str(i)) for i in range(8)]

p_dd8db9 = Symbol('p_dd8db9')
p_fbfefd = Symbol('p_fbfefd')
p_79e2ca = Symbol('p_79e2ca')
p_d2a644 = Symbol('p_d2a644')
p_803a1f = Symbol('p_803a1f')
p_fd6f6d = Symbol('p_fd6f6d')
p_50a615 = Symbol('p_50a615')
p_bae028 = Symbol('p_bae028')
p_49f1fc = Symbol('p_49f1fc')
p_5b9a9c = Symbol('p_5b9a9c')
p_4a90e8 = Symbol('p_4a90e8')
p_28e9ae = Symbol('p_28e9ae')
p_d68182 = Symbol('p_d68182')
p_f964c1 = Symbol('p_f964c1')
p_02c08d = Symbol('p_02c08d')
p_64828e = Symbol('p_64828e')
p_1ab04f = Symbol('p_1ab04f')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_5b9a9c)( qr[4] ))
circuit.append(Gates.ZGate( qr[6] ))
circuit.append(Gates.XGate( qr[6] ))
circuit.append(Gates.CRXGate(p_dd8db9)( qr[0], qr[6] ))
circuit.append(Gates.CRZGate(p_d2a644)( qr[1], qr[6] ))
circuit.append(Gates.C3SXGate( qr[0], qr[7], qr[6], qr[3] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.RYYGate(p_d68182)( qr[6], qr[7] ))
circuit.append(Gates.CRZGate(p_50a615)( qr[1], qr[7] ))
circuit.append(Gates.RZGate(p_fbfefd)( qr[1] ))
circuit.append(Gates.SXGate( qr[0] ))
circuit.append(Gates.CU1Gate(p_4a90e8)( qr[4], qr[0] ))
circuit.append(Gates.CRXGate(p_f964c1)( qr[6], qr[4] ))
circuit.append(Gates.RZZGate(p_28e9ae)( qr[7], qr[0] ))
circuit.append(Gates.CSXGate( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[6] ))
circuit.append(Gates.RZGate(p_02c08d)( qr[4] ))
circuit.append(Gates.CRXGate(p_bae028)( qr[0], qr[3] ))
circuit.append(Gates.CUGate(p_1ab04f, p_79e2ca, 3.1562533916051736, p_49f1fc)( qr[6], qr[2] ))
circuit.append(Gates.U2Gate(p_64828e, p_fd6f6d)( qr[2] ))
circuit.append(Gates.TGate( qr[6] ))
circuit.append(Gates.SdgGate( qr[0] ))
circuit.append(Gates.RZZGate(p_803a1f)( qr[3], qr[4] ))
circuit.append(Gates.TGate( qr[5] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))
circuit.append(cirq.measure(qr[7], key='cr7'))



circuit = cirq.resolve_parameters(circuit, {
    "p_dd8db9": 5.987304452123941,
    "p_fbfefd": 4.229610589867865,
    "p_79e2ca": 5.0063780207098425,
    "p_d2a644": 1.0296448789776642,
    "p_803a1f": 3.950837470808744,
    "p_fd6f6d": 2.1276323672732023,
    "p_50a615": 4.167661441102218,
    "p_bae028": 0.7279391018916035,
    "p_49f1fc": 4.940217775579305,
    "p_5b9a9c": 6.163759533339787,
    "p_4a90e8": 3.2142159669963557,
    "p_28e9ae": 5.1829934776392745,
    "p_d68182": 1.740253089260498,
    "p_f964c1": 5.94477504571567,
    "p_02c08d": 3.775592041307464,
    "p_64828e": 2.5163050709890156,
    "p_1ab04f": 5.03147076606842
}, recursive=True)
        



circuit = apply_transformations(circuit)


qasm_output = cirq.qasm(cirq.expand_composite(circuit))
circuit = circuit_from_qasm(qasm_output) # new circuit





simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=2771)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['m_cr0_0', 'm_cr1_0', 'm_cr2_0', 'm_cr3_0', 'm_cr4_0', 'm_cr5_0', 'm_cr6_0', 'm_cr7_0'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

