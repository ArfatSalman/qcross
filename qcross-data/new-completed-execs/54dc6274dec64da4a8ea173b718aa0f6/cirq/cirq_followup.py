
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



circuit = cirq.Circuit()

circuit.append(Gates.CRXGate(0.027261864368738644)( qr[8], qr[1] ))
circuit.append(Gates.CXGate( qr[6], qr[9] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(Gates.CRXGate(0.9075502808788635)( qr[6], qr[8] ))
circuit.append(Gates.ECRGate( qr[2], qr[0] ))
circuit.append(Gates.CSwapGate( qr[2], qr[8], qr[0] ))
circuit.append(Gates.RGate(6.099682100802839, 2.494306691997326)( qr[8] ))
circuit.append(Gates.RZXGate(3.7330617289797328)( qr[5], qr[2] ))
circuit.append(Gates.RYGate(3.5568415538710556)( qr[8] ))
circuit.append(Gates.U3Gate(1.0222809503303705, 1.6895773379952999, 3.5291798838720747)( qr[8] ))
circuit.append(Gates.CYGate( qr[5], qr[6] ))
circuit.append(Gates.U2Gate(3.044931199643564, 1.2044318302402206)( qr[2] ))
circuit.append(Gates.CSwapGate( qr[1], qr[6], qr[8] ))
circuit.append(Gates.SXGate( qr[5] ))
circuit.append(Gates.UGate(3.5905146351798125, 1.4398630066945612, 4.930260809283397)( qr[7] ))
circuit.append(Gates.UGate(1.945778856930902, 5.959001893737209, 3.3890130318399554)( qr[6] ))
circuit.append(Gates.CRXGate(6.15516938685536)( qr[5], qr[1] ))
circuit.append(Gates.U2Gate(4.734912763130236, 2.0633539972431736)( qr[7] ))
circuit.append(Gates.RGate(3.329578139088272, 2.6679935782057154)( qr[0] ))
circuit.append(Gates.XGate( qr[3] ))
circuit.append(Gates.CRXGate(0.9250999602143393)( qr[6], qr[0] ))
circuit.append(Gates.RZXGate(3.9273226264569736)( qr[5], qr[1] ))
circuit.append(Gates.CPhaseGate(2.3272657174534204)( qr[5], qr[6] ))
circuit.append(Gates.CSwapGate( qr[2], qr[5], qr[7] ))
circuit.append(Gates.RYGate(3.9320786554188296)( qr[6] ))
circuit.append(Gates.ZGate( qr[3] ))
circuit.append(Gates.U2Gate(1.5093939547937507, 0.3575732764804263)( qr[6] ))
circuit.append(Gates.CRXGate(3.1862838323251004)( qr[2], qr[5] ))
circuit.append(Gates.CHGate( qr[4], qr[2] ))
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

