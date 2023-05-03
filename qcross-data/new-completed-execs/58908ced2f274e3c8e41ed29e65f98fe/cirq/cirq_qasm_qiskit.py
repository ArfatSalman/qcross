
import cirq
import qiskit
from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(5)]



circuit = cirq.Circuit()

circuit.append(Gates.CYGate( qr[4], qr[0] ))
circuit.append(Gates.RYGate(5.393489737839679)( qr[0] ))
circuit.append(Gates.CXGate( qr[4], qr[2] ))
circuit.append(Gates.CYGate( qr[2], qr[0] ))
circuit.append(Gates.RVGate(0.2694018871971584, 3.6610185603230327, 1.6717980794833396)( qr[0] ))
circuit.append(Gates.CXGate( qr[1], qr[2] ))
circuit.append(Gates.RYGate(3.6367004709817228)( qr[0] ))
circuit.append(Gates.SXGate( qr[0] ))
circuit.append(Gates.RVGate(2.2068682001004865, 0.10969098183159173, 1.8129273219934456)( qr[3] ))
circuit.append(Gates.RYGate(2.187038626448052)( qr[4] ))
circuit.append(Gates.CSGate( qr[3], qr[1] ))
circuit.append(Gates.SXdgGate( qr[2] ))
circuit.append(Gates.CZGate( qr[0], qr[1] ))
circuit.append(Gates.CCXGate( qr[4], qr[1], qr[3] ))
circuit.append(Gates.RZGate(4.342933255918919)( qr[1] ))
circuit.append(Gates.UGate(5.780988845560674, 1.3228348249163877, 4.617489460561287)( qr[0] ))
circuit.append(Gates.TGate( qr[0] ))
circuit.append(Gates.ECRGate( qr[1], qr[3] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.CCZGate( qr[2], qr[3], qr[0] ))
subcircuit.append(Gates.RXGate(1.3936743262403044)( qr[0] ))
subcircuit.append(Gates.XGate( qr[3] ))
subcircuit.append(Gates.RZXGate(5.062431030267896)( qr[3], qr[0] ))
subcircuit.append(Gates.YGate( qr[4] ))
subcircuit.append(Gates.CZGate( qr[4], qr[2] ))
subcircuit.append(Gates.CSXGate( qr[3], qr[2] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.RYYGate(4.555588798234122)( qr[1], qr[2] ))
circuit.append(Gates.RYYGate(4.914511027415462)( qr[1], qr[2] ))
circuit.append(Gates.CSGate( qr[4], qr[0] ))
circuit.append(Gates.RZGate(3.3907281434225625)( qr[4] ))
circuit.append(Gates.CSXGate( qr[1], qr[4] ))
circuit.append(Gates.DCXGate( qr[2], qr[3] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.CSXGate( qr[0], qr[4] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))











expanded_circuit = cirq.expand_composite(circuit)
qasm_from_qiskit = qiskit.QuantumCircuit.from_qasm_str(cirq.qasm(expanded_circuit)).qasm()
cirq_circuit_from_qiskit_qasm = circuit_from_qasm(qasm_from_qiskit)

# since, importing in cirq uses different qubit names, we need to change the qubit names
circuit_transformed = cirq_circuit_from_qiskit_qasm.transform_qubits(lambda q: cirq.NamedQubit(q.name.replace("q_", "q")))

cirq.testing.assert_circuits_with_terminal_measurements_are_equivalent(circuit_transformed, circuit)




simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=979)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

