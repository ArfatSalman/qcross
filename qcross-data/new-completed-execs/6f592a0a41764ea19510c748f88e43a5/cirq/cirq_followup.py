
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



circuit = cirq.Circuit()

circuit.append(Gates.CPhaseGate(3.5690023406020117)( qr[1], qr[0] ))
circuit.append(Gates.ZGate( qr[1] ))
circuit.append(Gates.CRXGate(0.5834164558695757)( qr[1], qr[0] ))
circuit.append(Gates.PhaseGate(3.894930545586774)( qr[0] ))
circuit.append(Gates.IGate( qr[1] ))
circuit.append(Gates.CZGate( qr[0], qr[1] ))
circuit.append(Gates.SXGate( qr[0] ))
circuit.append(Gates.U2Gate(5.482574947566191, 0.8373110034524618)( qr[0] ))
circuit.append(Gates.PhaseGate(0.3578418944802631)( qr[1] ))
circuit.append(Gates.SwapGate( qr[1], qr[0] ))
circuit.append(Gates.SXdgGate( qr[1] ))
circuit.append(Gates.CHGate( qr[1], qr[0] ))
circuit.append(Gates.CPhaseGate(5.397112728340784)( qr[1], qr[0] ))
circuit.append(Gates.SXGate( qr[1] ))
circuit.append(Gates.CRYGate(1.174494077676677)( qr[0], qr[1] ))
circuit.append(Gates.HGate( qr[1] ))
circuit.append(Gates.YGate( qr[0] ))
circuit.append(Gates.RGate(2.8467414627241734, 3.5481884646507713)( qr[1] ))
circuit.append(Gates.RZXGate(3.2681088907886817)( qr[1], qr[0] ))
circuit.append(Gates.CRYGate(5.6914225992075504)( qr[0], qr[1] ))
circuit.append(Gates.U3Gate(4.266994303739899, 1.914216390388542, 1.0614410494494415)( qr[1] ))
circuit.append(Gates.CHGate( qr[1], qr[0] ))
circuit.append(Gates.CU3Gate(0.6949120689264752, 0.9164071466076199, 5.136397164125832)( qr[0], qr[1] ))
circuit.append(Gates.CRYGate(2.843774029250561)( qr[1], qr[0] ))
circuit.append(Gates.CU3Gate(0.6994648472584757, 3.50667959618503, 5.986466284185033)( qr[1], qr[0] ))
circuit.append(Gates.SXGate( qr[0] ))
circuit.append(cirq.measure(qr[1], key='cr0'))
circuit.append(cirq.measure(qr[0], key='cr1'))






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

