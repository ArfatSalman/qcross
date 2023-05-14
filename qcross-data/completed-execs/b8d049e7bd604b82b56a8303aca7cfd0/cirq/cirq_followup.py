
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


qr = [cirq.NamedQubit('q' + str(i)) for i in range(10)]

p_a2b8a1 = Symbol('p_a2b8a1')
p_c71b89 = Symbol('p_c71b89')
p_109b12 = Symbol('p_109b12')
p_61c866 = Symbol('p_61c866')
p_55837c = Symbol('p_55837c')
p_bcdc65 = Symbol('p_bcdc65')
p_ad1c79 = Symbol('p_ad1c79')
p_0e4f1e = Symbol('p_0e4f1e')
p_708df6 = Symbol('p_708df6')
p_b373ee = Symbol('p_b373ee')
p_89d7ca = Symbol('p_89d7ca')
p_55cda5 = Symbol('p_55cda5')
p_1d0fad = Symbol('p_1d0fad')
p_a3b617 = Symbol('p_a3b617')
p_a0a530 = Symbol('p_a0a530')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_1d0fad)( qr[3] ))
circuit.append(Gates.CRZGate(p_708df6)( qr[6], qr[3] ))
circuit.append(Gates.CRXGate(p_0e4f1e)( qr[1], qr[7] ))
circuit.append(Gates.CCXGate( qr[5], qr[9], qr[7] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.U2Gate(p_a0a530, p_a3b617)( qr[0] ))
subcircuit.append(Gates.SXdgGate( qr[4] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.TGate( qr[9] ))
circuit.append(Gates.XGate( qr[8] ))
circuit.append(Gates.CRZGate(p_61c866)( qr[1], qr[6] ))
circuit.append(Gates.RZGate(p_55cda5)( qr[1] ))
circuit.append(Gates.SXGate( qr[2] ))
circuit.append(Gates.CSXGate( qr[4], qr[8] ))
circuit.append(Gates.CCXGate( qr[4], qr[9], qr[5] ))
circuit.append(Gates.C3SXGate( qr[2], qr[4], qr[0], qr[9] ))
circuit.append(Gates.CSXGate( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.CHGate( qr[7], qr[1] ))
circuit.append(Gates.CSXGate( qr[2], qr[0] ))
circuit.append(Gates.CRZGate(p_c71b89)( qr[1], qr[2] ))
circuit.append(Gates.U2Gate(p_b373ee, p_ad1c79)( qr[2] ))
circuit.append(Gates.TGate( qr[0] ))
circuit.append(Gates.SXdgGate( qr[9] ))
circuit.append(Gates.TGate( qr[8] ))
circuit.append(Gates.RZGate(p_a2b8a1)( qr[1] ))
circuit.append(Gates.CRXGate(p_89d7ca)( qr[7], qr[1] ))
circuit.append(Gates.UGate(p_55837c, p_bcdc65, p_109b12)( qr[2] ))
circuit.append(Gates.ECRGate( qr[4], qr[8] ))
circuit.append(Gates.ZGate( qr[3] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))
circuit.append(cirq.measure(qr[7], key='cr7'))
circuit.append(cirq.measure(qr[8], key='cr8'))
circuit.append(cirq.measure(qr[9], key='cr9'))



circuit = cirq.resolve_parameters(circuit, {
    "p_a2b8a1": 5.014941143947427,
    "p_c71b89": 2.586208953975239,
    "p_109b12": 2.271164628944128,
    "p_61c866": 4.167661441102218,
    "p_55837c": 5.080799300534071,
    "p_bcdc65": 5.023617931957853,
    "p_ad1c79": 2.1276323672732023,
    "p_0e4f1e": 5.987304452123941,
    "p_708df6": 4.2641612072511235,
    "p_b373ee": 2.5163050709890156,
    "p_89d7ca": 5.970852306777193,
    "p_55cda5": 4.229610589867865,
    "p_1d0fad": 6.163759533339787,
    "p_a3b617": 1.0052392769301404,
    "p_a0a530": 0.25812405723927917
}, recursive=True)
        



circuit = apply_transformations(circuit)






simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=5542)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7', 'cr8', 'cr9'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

