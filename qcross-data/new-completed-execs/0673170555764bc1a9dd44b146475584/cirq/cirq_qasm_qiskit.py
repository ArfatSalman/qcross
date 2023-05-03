
import cirq
import qiskit
from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(10)]



circuit = cirq.Circuit()

circuit.append(Gates.RZZGate(3.138388361681893)( qr[1], qr[0] ))
circuit.append(Gates.TGate( qr[2] ))
circuit.append(Gates.U1Gate(0.396418175987844)( qr[9] ))
circuit.append(Gates.CRZGate(5.16452425350899)( qr[1], qr[4] ))
circuit.append(Gates.CRXGate(3.0664993083734644)( qr[6], qr[2] ))
circuit.append(Gates.RCCXGate( qr[4], qr[1], qr[8] ))
circuit.append(Gates.CSGate( qr[8], qr[6] ))
circuit.append(Gates.CCZGate( qr[3], qr[7], qr[9] ))
circuit.append(Gates.CU3Gate(2.8185804779007992, 5.261790461945118, 2.326141806696294)( qr[1], qr[4] ))
circuit.append(Gates.CZGate( qr[3], qr[8] ))
circuit.append(Gates.CSdgGate( qr[3], qr[4] ))
circuit.append(Gates.CUGate(3.522950755972168, 4.8949869688966565, 1.528172084251171, 3.5827113474296604)( qr[8], qr[5] ))
circuit.append(Gates.RCCXGate( qr[3], qr[5], qr[7] ))
circuit.append(Gates.CSXGate( qr[6], qr[8] ))
circuit.append(Gates.RCCXGate( qr[6], qr[4], qr[7] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.CRYGate(0.18861614070395222)( qr[8], qr[4] ))
subcircuit.append(Gates.SwapGate( qr[9], qr[2] ))
subcircuit.append(Gates.CSXGate( qr[3], qr[9] ))
subcircuit.append(Gates.UGate(2.29898529136329, 2.602581019015746, 3.608523225163746)( qr[8] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.RYYGate(4.484588825647207)( qr[4], qr[5] ))
circuit.append(Gates.U1Gate(6.019643147584277)( qr[0] ))
circuit.append(Gates.PhaseGate(5.38252061225771)( qr[7] ))
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











expanded_circuit = cirq.expand_composite(circuit)
qasm_from_qiskit = qiskit.QuantumCircuit.from_qasm_str(cirq.qasm(expanded_circuit)).qasm()
cirq_circuit_from_qiskit_qasm = circuit_from_qasm(qasm_from_qiskit)

# since, importing in cirq uses different qubit names, we need to change the qubit names
circuit_transformed = cirq_circuit_from_qiskit_qasm.transform_qubits(lambda q: cirq.NamedQubit(q.name.replace("q_", "q")))

cirq.testing.assert_circuits_with_terminal_measurements_are_equivalent(circuit_transformed, circuit)




simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=5542)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7', 'cr8', 'cr9'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

