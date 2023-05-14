
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

p_63d6aa = Symbol('p_63d6aa')
p_92b6fe = Symbol('p_92b6fe')
p_db8eb2 = Symbol('p_db8eb2')
p_b138c0 = Symbol('p_b138c0')
p_2f176b = Symbol('p_2f176b')
p_4a9935 = Symbol('p_4a9935')
p_b2e764 = Symbol('p_b2e764')
p_bfb580 = Symbol('p_bfb580')
p_dfd8ce = Symbol('p_dfd8ce')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_92b6fe)( qr[1] ))
circuit.append(Gates.RZZGate(p_4a9935)( qr[2], qr[3] ))
circuit.append(Gates.iSwapGate( qr[2], qr[3] ))
circuit.append(Gates.CSXGate( qr[1], qr[0] ))
circuit.append(Gates.XGate( qr[2] ))
circuit.append(Gates.CUGate(p_dfd8ce, p_db8eb2, 2.3864521352475245, p_bfb580)( qr[0], qr[2] ))
circuit.append(Gates.CU1Gate(p_b2e764)( qr[3], qr[0] ))
circuit.append(Gates.CHGate( qr[3], qr[2] ))
circuit.append(Gates.CHGate( qr[1], qr[2] ))
circuit.append(Gates.C3SXGate( qr[3], qr[0], qr[1], qr[2] ))
circuit.append(Gates.C3SXGate( qr[3], qr[1], qr[0], qr[2] ))
circuit.append(Gates.TGate( qr[2] ))
circuit.append(Gates.SXdgGate( qr[2] ))
circuit.append(Gates.TGate( qr[2] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(Gates.RCCXGate( qr[1], qr[0], qr[3] ))
circuit.append(Gates.RYYGate(p_2f176b)( qr[2], qr[0] ))
circuit.append(Gates.RCCXGate( qr[2], qr[3], qr[0] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(Gates.SGate( qr[3] ))
circuit.append(Gates.CRZGate(p_b138c0)( qr[0], qr[1] ))
circuit.append(Gates.C3SXGate( qr[1], qr[2], qr[0], qr[3] ))
circuit.append(Gates.RYYGate(p_63d6aa)( qr[2], qr[0] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))



circuit = cirq.resolve_parameters(circuit, {
    "p_63d6aa": 5.398622178940033,
    "p_92b6fe": 6.163759533339787,
    "p_db8eb2": 5.897054719225356,
    "p_b138c0": 2.9790366726895714,
    "p_2f176b": 1.740253089260498,
    "p_4a9935": 4.066449154047175,
    "p_b2e764": 5.154187354656876,
    "p_bfb580": 5.987304452123941,
    "p_dfd8ce": 0.5112149185250571
}, recursive=True)
        



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

