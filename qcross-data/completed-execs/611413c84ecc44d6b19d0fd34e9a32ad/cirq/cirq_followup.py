
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


qr_1 = [cirq.NamedQubit('q' + str(i)) for i in range(2)]



qc_1 = cirq.Circuit()

qc_1.append(Gates.ZGate( qr_1[0] ))
qc_1.append(cirq.measure(qr_1[0], key='cr0'))
qc_1.append(cirq.measure(qr_1[1], key='cr1'))






qc_1 = apply_transformations(qc_1)


qasm_output = cirq.qasm(cirq.expand_composite(qc_1))
qc_1 = circuit_from_qasm(qasm_output) # new circuit





simulator = cirq.DensityMatrixSimulator(seed=np.random.RandomState())


result_1 = simulator.run(qc_1, repetitions=7838)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result_1, keys=['m_cr0_0', 'm_cr1_0'])

RESULT_1 = counts




# Circuit 2

            
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


qr_2 = [cirq.NamedQubit('q' + str(i)) for i in range(9)]



qc_2 = cirq.Circuit()

qc_2.append(Gates.RZGate(6.163759533339787)( qr_2[2] ))
qc_2.append(Gates.CRZGate(4.2641612072511235)( qr_2[4], qr_2[1] ))
qc_2.append(Gates.CCXGate( qr_2[3], qr_2[7], qr_2[5] ))
qc_2.append(Gates.ZGate( qr_2[1] ))
qc_2.append(Gates.XGate( qr_2[5] ))
qc_2.append(Gates.RCCXGate( qr_2[8], qr_2[4], qr_2[6] ))
qc_2.append(Gates.RZGate(4.229610589867865)( qr_2[0] ))
qc_2.append(Gates.CCXGate( qr_2[5], qr_2[8], qr_2[1] ))
qc_2.append(Gates.SdgGate( qr_2[5] ))
qc_2.append(Gates.U2Gate(4.214504315296764, 4.6235667602042065)( qr_2[8] ))
qc_2.append(Gates.CSXGate( qr_2[2], qr_2[1] ))
qc_2.append(Gates.CHGate( qr_2[0], qr_2[5] ))
qc_2.append(cirq.measure(qr_2[0], key='cr0'))
qc_2.append(cirq.measure(qr_2[1], key='cr1'))
qc_2.append(cirq.measure(qr_2[2], key='cr2'))
qc_2.append(cirq.measure(qr_2[3], key='cr3'))
qc_2.append(cirq.measure(qr_2[4], key='cr4'))
qc_2.append(cirq.measure(qr_2[5], key='cr5'))
qc_2.append(cirq.measure(qr_2[6], key='cr6'))
qc_2.append(cirq.measure(qr_2[7], key='cr7'))
qc_2.append(cirq.measure(qr_2[8], key='cr8'))






qc_2 = apply_transformations(qc_2)


qasm_output = cirq.qasm(cirq.expand_composite(qc_2))
qc_2 = circuit_from_qasm(qasm_output) # new circuit





simulator = cirq.DensityMatrixSimulator(seed=np.random.RandomState())


result_2 = simulator.run(qc_2, repetitions=7838)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result_2, keys=['m_cr0_0', 'm_cr1_0', 'm_cr2_0', 'm_cr3_0', 'm_cr4_0', 'm_cr5_0', 'm_cr6_0', 'm_cr7_0', 'm_cr8_0'])

RESULT_2 = counts


RESULT = [RESULT_1, RESULT_2]

if __name__ == '__main__':
    from qcross.utils import display_results
    for i in RESULT:
        display_results( {"result": i })


