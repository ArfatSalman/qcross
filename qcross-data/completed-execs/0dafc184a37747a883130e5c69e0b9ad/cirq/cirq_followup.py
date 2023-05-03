import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


def apply_transformations(circuit, context=cirq.TransformerContext(deep=True)):
    optimized_circuit = cirq.expand_composite(circuit, context=context)

    optimized_circuit = cirq.defer_measurements(optimized_circuit, context=context)

    optimized_circuit = cirq.merge_k_qubit_unitaries(
        optimized_circuit,
        k=2,
        rewriter=lambda op: op.with_tags("merged"),
        context=context,
    )

    optimized_circuit = cirq.drop_empty_moments(optimized_circuit, context=context)

    optimized_circuit = cirq.eject_z(
        optimized_circuit, eject_parameterized=True, context=context
    )

    optimized_circuit = cirq.eject_phased_paulis(
        optimized_circuit, context=context, eject_parameterized=True
    )

    optimized_circuit = cirq.drop_negligible_operations(
        optimized_circuit, context=context
    )

    optimized_circuit = cirq.stratified_circuit(optimized_circuit, context=context)

    optimized_circuit = cirq.synchronize_terminal_measurements(
        optimized_circuit, context=context
    )

    # Assert the original and optimized circuit are equivalent.
    cirq.testing.assert_circuits_with_terminal_measurements_are_equivalent(
        circuit, optimized_circuit
    )

    return optimized_circuit


qr = [cirq.NamedQubit("q" + str(i)) for i in range(7)]


circuit = cirq.Circuit()

circuit.append(Gates.RZGate(6.163759533339787)(qr[4]))
circuit.append(Gates.ZGate(qr[6]))
circuit.append(Gates.XGate(qr[3]))
circuit.append(Gates.CRXGate(2.0099472182748075)(qr[2], qr[5]))
circuit.append(cirq.measure(qr[0], key="cr0"))
circuit.append(cirq.measure(qr[1], key="cr1"))
circuit.append(cirq.measure(qr[2], key="cr2"))
circuit.append(cirq.measure(qr[3], key="cr3"))
circuit.append(cirq.measure(qr[4], key="cr4"))
circuit.append(cirq.measure(qr[5], key="cr5"))
circuit.append(cirq.measure(qr[6], key="cr6"))


circuit = apply_transformations(circuit)


simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=1959)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(
    result, keys=["cr0", "cr1", "cr2", "cr3", "cr4", "cr5", "cr6"]
)

RESULT = counts


if __name__ == "__main__":
    pass
    # from qcross.utils import display_results

    # display_results({"result": RESULT})
