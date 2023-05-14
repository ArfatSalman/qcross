
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

p_597899 = Symbol('p_597899')
p_300a3c = Symbol('p_300a3c')
p_b934bd = Symbol('p_b934bd')
p_9136a9 = Symbol('p_9136a9')
p_bcf56a = Symbol('p_bcf56a')
p_ee7fe0 = Symbol('p_ee7fe0')
p_9fd00a = Symbol('p_9fd00a')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_bcf56a)( qr[1] ))
circuit.append(Gates.RZZGate(p_597899)( qr[2], qr[3] ))
circuit.append(Gates.iSwapGate( qr[2], qr[3] ))
circuit.append(Gates.CSXGate( qr[1], qr[0] ))
circuit.append(Gates.XGate( qr[2] ))
circuit.append(Gates.CUGate(p_9136a9, p_b934bd, 2.3864521352475245, p_9fd00a)( qr[0], qr[2] ))
circuit.append(Gates.CU1Gate(p_ee7fe0)( qr[3], qr[0] ))
circuit.append(Gates.CHGate( qr[3], qr[2] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.ECRGate( qr[1], qr[3] ))
subcircuit.append(Gates.U2Gate(6.171674001528992, 4.948673314014118)( qr[0] ))
subcircuit.append(Gates.SGate( qr[1] ))
subcircuit.append(Gates.CXGate( qr[0], qr[3] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.CHGate( qr[1], qr[2] ))
circuit.append(Gates.C3SXGate( qr[3], qr[0], qr[1], qr[2] ))
circuit.append(Gates.C3SXGate( qr[3], qr[1], qr[0], qr[2] ))
circuit.append(Gates.TGate( qr[2] ))
circuit.append(Gates.SXdgGate( qr[2] ))
circuit.append(Gates.TGate( qr[2] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(Gates.RCCXGate( qr[1], qr[0], qr[3] ))
circuit.append(Gates.RYYGate(p_300a3c)( qr[2], qr[0] ))
circuit.append(Gates.RCCXGate( qr[2], qr[3], qr[0] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))



circuit = cirq.resolve_parameters(circuit, {
    "p_597899": 4.066449154047175,
    "p_300a3c": 1.740253089260498,
    "p_b934bd": 5.897054719225356,
    "p_9136a9": 0.5112149185250571,
    "p_bcf56a": 6.163759533339787,
    "p_ee7fe0": 5.154187354656876,
    "p_9fd00a": 5.987304452123941
}, recursive=True)
        



circuit = apply_transformations(circuit)






simulator = cirq.DensityMatrixSimulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=692)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

