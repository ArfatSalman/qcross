
import cirq
import qiskit
from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(6)]



circuit = cirq.Circuit()

circuit.append(Gates.CSGate( qr[1], qr[3] ))
circuit.append(Gates.CU1Gate(2.7516388630934165)( qr[2], qr[0] ))
circuit.append(Gates.CPhaseGate(4.526280604536298)( qr[0], qr[1] ))
circuit.append(Gates.CRYGate(2.8957147333760322)( qr[4], qr[2] ))
circuit.append(Gates.ECRGate( qr[1], qr[3] ))
circuit.append(Gates.iSwapGate( qr[0], qr[5] ))
circuit.append(Gates.RYGate(5.218542100413873)( qr[0] ))
circuit.append(Gates.CYGate( qr[4], qr[0] ))
circuit.append(Gates.CUGate(4.0589886937440705, 5.489841527329702, 5.349444809703235, 0.0076492699425670645)( qr[3], qr[5] ))
circuit.append(Gates.CCXGate( qr[1], qr[5], qr[3] ))
circuit.append(Gates.CCXGate( qr[1], qr[4], qr[0] ))
circuit.append(Gates.SdgGate( qr[3] ))
circuit.append(Gates.CCXGate( qr[3], qr[5], qr[4] ))
circuit.append(Gates.CSXGate( qr[4], qr[1] ))
circuit.append(Gates.CRXGate(1.7239239743720898)( qr[2], qr[0] ))
circuit.append(Gates.CSGate( qr[4], qr[0] ))
circuit.append(Gates.SdgGate( qr[0] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.YGate( qr[0] ))
subcircuit.append(Gates.RXXGate(5.748731119826895)( qr[1], qr[4] ))
subcircuit.append(Gates.XGate( qr[3] ))
subcircuit.append(Gates.TdgGate( qr[4] ))
subcircuit.append(Gates.RGate(1.0099433123573884, 3.399529081072497)( qr[5] ))
subcircuit.append(Gates.U3Gate(5.953737875506177, 2.168117657673707, 5.952071466550862)( qr[3] ))
subcircuit.append(Gates.CU1Gate(4.560443955770688)( qr[3], qr[1] ))
subcircuit.append(Gates.CXGate( qr[0], qr[5] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.U1Gate(3.6101582139068564)( qr[2] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))











expanded_circuit = cirq.expand_composite(circuit)
qasm_from_qiskit = qiskit.QuantumCircuit.from_qasm_str(cirq.qasm(expanded_circuit)).qasm()
cirq_circuit_from_qiskit_qasm = circuit_from_qasm(qasm_from_qiskit)

# since, importing in cirq uses different qubit names, we need to change the qubit names
circuit_transformed = cirq_circuit_from_qiskit_qasm.transform_qubits(lambda q: cirq.NamedQubit(q.name.replace("q_", "q")))

cirq.testing.assert_circuits_with_terminal_measurements_are_equivalent(circuit_transformed, circuit)




simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=1385)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

