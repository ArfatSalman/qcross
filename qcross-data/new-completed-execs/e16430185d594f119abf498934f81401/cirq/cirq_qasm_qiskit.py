
import cirq
import qiskit
from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(8)]



circuit = cirq.Circuit()

circuit.append(Gates.ECRGate( qr[1], qr[7] ))
circuit.append(Gates.RC3XGate( qr[1], qr[0], qr[5], qr[6] ))
circuit.append(Gates.CPhaseGate(0.7207706407070019)( qr[4], qr[3] ))
circuit.append(Gates.DCXGate( qr[3], qr[4] ))
circuit.append(Gates.RCCXGate( qr[2], qr[1], qr[4] ))
circuit.append(Gates.SwapGate( qr[6], qr[5] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.CCXGate( qr[2], qr[5], qr[3] ))
subcircuit.append(Gates.RCCXGate( qr[5], qr[0], qr[1] ))
subcircuit.append(Gates.CSdgGate( qr[2], qr[5] ))
subcircuit.append(Gates.CPhaseGate(0.37327159055448994)( qr[2], qr[3] ))
subcircuit.append(Gates.CUGate(5.603364910525811, 0.5779107198193537, 1.1120816789855388, 4.149916491769281)( qr[3], qr[2] ))
subcircuit.append(Gates.RZXGate(1.264637581124353)( qr[7], qr[1] ))
subcircuit.append(Gates.SdgGate( qr[2] ))
subcircuit.append(Gates.YGate( qr[3] ))
subcircuit.append(Gates.RGate(3.026082456028544, 4.216289330198313)( qr[6] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.iSwapGate( qr[4], qr[7] ))
circuit.append(Gates.RXGate(4.802467793465571)( qr[0] ))
circuit.append(Gates.iSwapGate( qr[0], qr[5] ))
circuit.append(Gates.CU1Gate(3.4625444838065618)( qr[0], qr[6] ))
circuit.append(Gates.CSwapGate( qr[0], qr[3], qr[6] ))
circuit.append(Gates.RGate(5.104156300804455, 6.227137798959555)( qr[0] ))
circuit.append(Gates.TGate( qr[5] ))
circuit.append(Gates.RXXGate(6.256338963756067)( qr[1], qr[5] ))
circuit.append(Gates.DCXGate( qr[7], qr[6] ))
circuit.append(Gates.RYGate(2.803631472128793)( qr[3] ))
circuit.append(Gates.RC3XGate( qr[4], qr[3], qr[1], qr[2] ))
circuit.append(Gates.CU1Gate(1.5456697172063534)( qr[7], qr[6] ))
circuit.append(Gates.RYGate(4.278284783932528)( qr[7] ))
circuit.append(Gates.RCCXGate( qr[7], qr[2], qr[0] ))
circuit.append(Gates.RGate(0.2852105385229711, 5.142516617776941)( qr[2] ))
circuit.append(Gates.RXXGate(2.2028067729502347)( qr[1], qr[6] ))
circuit.append(Gates.RXGate(1.732522506962926)( qr[7] ))
circuit.append(Gates.CCXGate( qr[5], qr[1], qr[6] ))
circuit.append(Gates.XGate( qr[3] ))
circuit.append(Gates.IGate( qr[3] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))
circuit.append(cirq.measure(qr[7], key='cr7'))











expanded_circuit = cirq.expand_composite(circuit)
qasm_from_qiskit = qiskit.QuantumCircuit.from_qasm_str(cirq.qasm(expanded_circuit)).qasm()
cirq_circuit_from_qiskit_qasm = circuit_from_qasm(qasm_from_qiskit)

# since, importing in cirq uses different qubit names, we need to change the qubit names
circuit_transformed = cirq_circuit_from_qiskit_qasm.transform_qubits(lambda q: cirq.NamedQubit(q.name.replace("q_", "q")))

cirq.testing.assert_circuits_with_terminal_measurements_are_equivalent(circuit_transformed, circuit)




simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=2771)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

