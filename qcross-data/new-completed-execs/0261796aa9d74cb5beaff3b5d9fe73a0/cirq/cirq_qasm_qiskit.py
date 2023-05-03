
import cirq
import qiskit
from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(10)]



circuit = cirq.Circuit()

circuit.append(Gates.CSwapGate( qr[0], qr[9], qr[7] ))
circuit.append(Gates.PhaseGate(3.343442682560371)( qr[0] ))
circuit.append(Gates.SGate( qr[3] ))
circuit.append(Gates.HGate( qr[5] ))
circuit.append(Gates.CRZGate(3.2858177251722944)( qr[9], qr[7] ))
circuit.append(Gates.RVGate(1.6270903792852736, 1.0744526495059412, 3.7558505518080576)( qr[3] ))
circuit.append(Gates.HGate( qr[0] ))
circuit.append(Gates.U2Gate(0.5159858283914562, 3.092014702746218)( qr[6] ))
circuit.append(Gates.RVGate(5.944576757265284, 5.021353132730173, 4.714404259070525)( qr[0] ))
circuit.append(Gates.RC3XGate( qr[0], qr[1], qr[7], qr[2] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.CU3Gate(0.6044097350971822, 4.888657590196426, 2.507112428772863)( qr[9], qr[5] ))
subcircuit.append(Gates.RZXGate(0.4541176237749392)( qr[5], qr[3] ))
subcircuit.append(Gates.CSwapGate( qr[1], qr[9], qr[4] ))
subcircuit.append(Gates.RVGate(2.6258763463210713, 6.086094132835261, 0.057422744634472736)( qr[2] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.ZGate( qr[9] ))
circuit.append(Gates.CRXGate(1.0327406277155489)( qr[4], qr[6] ))
circuit.append(Gates.CRZGate(3.051239290740801)( qr[1], qr[0] ))
circuit.append(Gates.ECRGate( qr[5], qr[4] ))
circuit.append(Gates.RYGate(5.127275071501011)( qr[8] ))
circuit.append(Gates.IGate( qr[5] ))
circuit.append(Gates.CSXGate( qr[3], qr[7] ))
circuit.append(Gates.CRZGate(1.6690058311460272)( qr[7], qr[2] ))
circuit.append(Gates.XGate( qr[3] ))
circuit.append(Gates.CRZGate(1.620800307377981)( qr[1], qr[5] ))
circuit.append(Gates.CU1Gate(0.4967177059820002)( qr[0], qr[7] ))
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

