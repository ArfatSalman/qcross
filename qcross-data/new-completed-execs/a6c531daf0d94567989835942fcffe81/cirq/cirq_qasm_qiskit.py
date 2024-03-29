
import cirq
import qiskit
from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(7)]



circuit = cirq.Circuit()

circuit.append(Gates.U3Gate(1.2333979366062962, 0.8994966515664887, 3.0003132360957094)( qr[1] ))
circuit.append(Gates.SwapGate( qr[5], qr[0] ))
circuit.append(Gates.CU1Gate(5.8809885406034885)( qr[4], qr[0] ))
circuit.append(Gates.CSXGate( qr[0], qr[3] ))
circuit.append(Gates.SXGate( qr[0] ))
circuit.append(Gates.CPhaseGate(4.661904537785083)( qr[4], qr[6] ))
circuit.append(Gates.U3Gate(6.161570642375718, 0.7126827811277849, 1.428988687288719)( qr[5] ))
circuit.append(Gates.CRZGate(2.777640838880794)( qr[0], qr[3] ))
circuit.append(Gates.SwapGate( qr[0], qr[4] ))
circuit.append(Gates.SXGate( qr[2] ))
circuit.append(Gates.U2Gate(1.9012707343238924, 6.017351377795965)( qr[3] ))
circuit.append(Gates.U2Gate(1.3178440304272925, 3.434672943879739)( qr[3] ))
circuit.append(Gates.DCXGate( qr[1], qr[6] ))
circuit.append(Gates.U3Gate(2.0260584085672413, 5.46425242678673, 4.443597328220221)( qr[5] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.ECRGate( qr[6], qr[2] ))
subcircuit.append(Gates.RZZGate(3.4677289488904535)( qr[5], qr[2] ))
subcircuit.append(Gates.CZGate( qr[3], qr[4] ))
subcircuit.append(Gates.CPhaseGate(5.900280104099499)( qr[2], qr[1] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.DCXGate( qr[4], qr[1] ))
circuit.append(Gates.CXGate( qr[2], qr[3] ))
circuit.append(Gates.CRXGate(0.47168664474085104)( qr[4], qr[2] ))
circuit.append(Gates.PhaseGate(5.273838382452584)( qr[3] ))
circuit.append(Gates.PhaseGate(0.6110285192622922)( qr[5] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))











expanded_circuit = cirq.expand_composite(circuit)
qasm_from_qiskit = qiskit.QuantumCircuit.from_qasm_str(cirq.qasm(expanded_circuit)).qasm()
cirq_circuit_from_qiskit_qasm = circuit_from_qasm(qasm_from_qiskit)

# since, importing in cirq uses different qubit names, we need to change the qubit names
circuit_transformed = cirq_circuit_from_qiskit_qasm.transform_qubits(lambda q: cirq.NamedQubit(q.name.replace("q_", "q")))

cirq.testing.assert_circuits_with_terminal_measurements_are_equivalent(circuit_transformed, circuit)




simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=1959)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

