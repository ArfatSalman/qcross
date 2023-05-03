
import cirq
import qiskit
from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(10)]



circuit = cirq.Circuit()

circuit.append(Gates.SdgGate( qr[9] ))
circuit.append(Gates.HGate( qr[6] ))
circuit.append(Gates.U3Gate(6.248539137506652, 3.0437559890158274, 3.877040016955039)( qr[3] ))
circuit.append(Gates.TGate( qr[8] ))
circuit.append(Gates.RYGate(2.4289944643648695)( qr[2] ))
circuit.append(Gates.SwapGate( qr[9], qr[1] ))
circuit.append(Gates.RYYGate(2.092741391579245)( qr[6], qr[3] ))
circuit.append(Gates.RZGate(2.184568031539945)( qr[9] ))
circuit.append(Gates.RZGate(0.6748073587752819)( qr[4] ))
circuit.append(Gates.U1Gate(1.4687935154189555)( qr[9] ))
circuit.append(Gates.UGate(2.4455568111156785, 3.2132129187211773, 5.7839656565594115)( qr[3] ))
circuit.append(Gates.U1Gate(2.6497338339327143)( qr[9] ))
circuit.append(Gates.SXdgGate( qr[9] ))
circuit.append(Gates.RXGate(0.6137530841617304)( qr[0] ))
circuit.append(Gates.CSGate( qr[9], qr[4] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.RGate(3.863590788996665, 1.7755874178641218)( qr[0] ))
subcircuit.append(Gates.SXGate( qr[0] ))
subcircuit.append(Gates.TGate( qr[7] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.HGate( qr[4] ))
circuit.append(Gates.RCCXGate( qr[8], qr[2], qr[3] ))
circuit.append(Gates.CSXGate( qr[9], qr[7] ))
circuit.append(Gates.CPhaseGate(4.048113620213937)( qr[5], qr[9] ))
circuit.append(Gates.HGate( qr[3] ))
circuit.append(Gates.HGate( qr[0] ))
circuit.append(Gates.CSXGate( qr[7], qr[2] ))
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

