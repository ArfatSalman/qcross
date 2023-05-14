
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


qr = [cirq.NamedQubit('q' + str(i)) for i in range(4)]

p_26bdc5 = Symbol('p_26bdc5')
p_ef51d2 = Symbol('p_ef51d2')
p_b28578 = Symbol('p_b28578')
p_129651 = Symbol('p_129651')
p_ca72f6 = Symbol('p_ca72f6')
p_6111a3 = Symbol('p_6111a3')
p_04934c = Symbol('p_04934c')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_26bdc5)( qr[1] ))
circuit.append(Gates.RZZGate(p_b28578)( qr[2], qr[3] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.TdgGate( qr[2] ))
subcircuit.append(Gates.U1Gate(5.01836135520768)( qr[1] ))
subcircuit.append(Gates.CRYGate(4.736752714049485)( qr[0], qr[3] ))
subcircuit.append(Gates.RXGate(6.1292830756636185)( qr[2] ))
subcircuit.append(Gates.CHGate( qr[2], qr[3] ))
subcircuit.append(Gates.CXGate( qr[2], qr[0] ))
subcircuit.append(Gates.RZZGate(3.516607467010828)( qr[3], qr[1] ))
subcircuit.append(Gates.PhaseGate(3.2287759437031154)( qr[1] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.iSwapGate( qr[2], qr[3] ))
circuit.append(Gates.CSXGate( qr[1], qr[0] ))
circuit.append(Gates.XGate( qr[2] ))
circuit.append(Gates.CUGate(p_ef51d2, p_ca72f6, p_6111a3, p_129651)( qr[0], qr[2] ))
circuit.append(Gates.CU1Gate(p_04934c)( qr[3], qr[0] ))
circuit.append(Gates.CHGate( qr[3], qr[2] ))
circuit.append(Gates.CHGate( qr[1], qr[2] ))
circuit.append(Gates.C3SXGate( qr[3], qr[0], qr[1], qr[2] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))



circuit = cirq.resolve_parameters(circuit, {
    "p_26bdc5": 6.163759533339787,
    "p_ef51d2": 0.5112149185250571,
    "p_b28578": 4.066449154047175,
    "p_129651": 5.987304452123941,
    "p_ca72f6": 5.897054719225356,
    "p_6111a3": 2.3864521352475245,
    "p_04934c": 5.154187354656876
}, recursive=True)
        



circuit = apply_transformations(circuit)






simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=692)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

