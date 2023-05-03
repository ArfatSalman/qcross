
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



circuit = cirq.Circuit()

circuit.append(Gates.RZGate(6.163759533339787)( qr[1] ))
circuit.append(Gates.RZZGate(4.066449154047175)( qr[2], qr[3] ))
circuit.append(Gates.iSwapGate( qr[2], qr[3] ))
circuit.append(Gates.CSXGate( qr[1], qr[0] ))
circuit.append(Gates.XGate( qr[2] ))
circuit.append(Gates.CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245, 5.987304452123941)( qr[0], qr[2] ))
circuit.append(Gates.CU1Gate(5.154187354656876)( qr[3], qr[0] ))
circuit.append(Gates.CHGate( qr[3], qr[2] ))
circuit.append(Gates.CHGate( qr[1], qr[2] ))
circuit.append(Gates.C3SXGate( qr[3], qr[0], qr[1], qr[2] ))
circuit.append(Gates.C3SXGate( qr[3], qr[1], qr[0], qr[2] ))
circuit.append(Gates.TGate( qr[2] ))
circuit.append(Gates.SXdgGate( qr[2] ))
circuit.append(Gates.TGate( qr[2] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(Gates.RCCXGate( qr[1], qr[0], qr[3] ))
circuit.append(Gates.RYYGate(1.740253089260498)( qr[2], qr[0] ))
circuit.append(Gates.RCCXGate( qr[2], qr[3], qr[0] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(Gates.SGate( qr[3] ))
circuit.append(Gates.CRZGate(2.9790366726895714)( qr[0], qr[1] ))
circuit.append(Gates.C3SXGate( qr[1], qr[2], qr[0], qr[3] ))
circuit.append(Gates.RYYGate(5.398622178940033)( qr[2], qr[0] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(Gates.CU1Gate(3.2142159669963557)( qr[0], qr[3] ))
circuit.append(Gates.iSwapGate( qr[1], qr[0] ))
circuit.append(Gates.CRXGate(5.94477504571567)( qr[2], qr[0] ))
circuit.append(Gates.U2Gate(4.214504315296764, 4.6235667602042065)( qr[2] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))






circuit = apply_transformations(circuit)


qasm_output = cirq.qasm(cirq.expand_composite(circuit))
circuit = circuit_from_qasm(qasm_output) # new circuit





simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=692)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['m_cr0_0', 'm_cr1_0', 'm_cr2_0', 'm_cr3_0'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

