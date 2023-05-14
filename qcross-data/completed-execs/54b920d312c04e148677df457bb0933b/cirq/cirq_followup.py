
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

p_097544 = Symbol('p_097544')
p_6bf657 = Symbol('p_6bf657')
p_cda6ce = Symbol('p_cda6ce')
p_74776f = Symbol('p_74776f')
p_45ab98 = Symbol('p_45ab98')
p_814b0e = Symbol('p_814b0e')
p_2092b7 = Symbol('p_2092b7')
p_9cf47d = Symbol('p_9cf47d')
p_2a789a = Symbol('p_2a789a')
p_f9d44b = Symbol('p_f9d44b')
p_a08081 = Symbol('p_a08081')
p_6b1e96 = Symbol('p_6b1e96')
p_e59b9b = Symbol('p_e59b9b')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_6bf657)( qr[4] ))
circuit.append(Gates.ZGate( qr[6] ))
circuit.append(Gates.XGate( qr[6] ))
circuit.append(Gates.CRXGate(p_cda6ce)( qr[0], qr[6] ))
circuit.append(Gates.CRZGate(1.0296448789776642)( qr[1], qr[6] ))
circuit.append(Gates.C3SXGate( qr[0], qr[7], qr[6], qr[3] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.RYYGate(p_f9d44b)( qr[6], qr[7] ))
circuit.append(Gates.CRZGate(p_814b0e)( qr[1], qr[7] ))
circuit.append(Gates.RZGate(p_e59b9b)( qr[1] ))
circuit.append(Gates.SXGate( qr[0] ))
circuit.append(Gates.CU1Gate(p_2092b7)( qr[4], qr[0] ))
circuit.append(Gates.CRXGate(5.94477504571567)( qr[6], qr[4] ))
circuit.append(Gates.RZZGate(p_097544)( qr[7], qr[0] ))
circuit.append(Gates.CSXGate( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[6] ))
circuit.append(Gates.RZGate(p_6b1e96)( qr[4] ))
circuit.append(Gates.CRXGate(p_9cf47d)( qr[0], qr[3] ))
circuit.append(Gates.CUGate(p_2a789a, p_74776f, 3.1562533916051736, p_a08081)( qr[6], qr[2] ))
circuit.append(Gates.U2Gate(2.5163050709890156, p_45ab98)( qr[2] ))
circuit.append(Gates.TGate( qr[6] ))
circuit.append(Gates.SdgGate( qr[0] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))
circuit.append(cirq.measure(qr[7], key='cr7'))



circuit = cirq.resolve_parameters(circuit, {
    "p_097544": 5.1829934776392745,
    "p_6bf657": 6.163759533339787,
    "p_cda6ce": 5.987304452123941,
    "p_74776f": 5.0063780207098425,
    "p_45ab98": 2.1276323672732023,
    "p_814b0e": 4.167661441102218,
    "p_2092b7": 3.2142159669963557,
    "p_9cf47d": 0.7279391018916035,
    "p_2a789a": 5.03147076606842,
    "p_f9d44b": 1.740253089260498,
    "p_a08081": 4.940217775579305,
    "p_6b1e96": 3.775592041307464,
    "p_e59b9b": 4.229610589867865
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

