
import cirq
import qiskit
from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(6)]

p_72af2c = Symbol('p_72af2c')
p_5ed9e5 = Symbol('p_5ed9e5')
p_d7cead = Symbol('p_d7cead')
p_6a555a = Symbol('p_6a555a')
p_86b1e1 = Symbol('p_86b1e1')
p_02e598 = Symbol('p_02e598')
p_c6dce3 = Symbol('p_c6dce3')
p_7d8767 = Symbol('p_7d8767')
p_6849dc = Symbol('p_6849dc')
p_84dd61 = Symbol('p_84dd61')
p_7fd6f3 = Symbol('p_7fd6f3')
p_1a3b94 = Symbol('p_1a3b94')
p_2d35e2 = Symbol('p_2d35e2')
p_ba2c5d = Symbol('p_ba2c5d')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_6a555a)( qr[4] ))
circuit.append(Gates.ZGate( qr[3] ))
circuit.append(Gates.CRZGate(p_7fd6f3)( qr[2], qr[4] ))
circuit.append(Gates.CUGate(p_c6dce3, p_6849dc, p_d7cead, p_7d8767)( qr[2], qr[3] ))
circuit.append(Gates.C3SXGate( qr[1], qr[4], qr[0], qr[2] ))
circuit.append(Gates.CCXGate( qr[1], qr[5], qr[0] ))
circuit.append(Gates.C3SXGate( qr[4], qr[3], qr[5], qr[0] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.TGate( qr[4] ))
circuit.append(Gates.RCCXGate( qr[5], qr[3], qr[4] ))
circuit.append(Gates.SGate( qr[5] ))
circuit.append(Gates.CRZGate(4.167661441102218)( qr[1], qr[5] ))
circuit.append(Gates.RZGate(p_2d35e2)( qr[1] ))
circuit.append(Gates.C3SXGate( qr[0], qr[2], qr[1], qr[3] ))
circuit.append(Gates.CU1Gate(p_02e598)( qr[3], qr[0] ))
circuit.append(Gates.UGate(p_ba2c5d, p_86b1e1, p_72af2c)( qr[5] ))
circuit.append(Gates.RZZGate(p_1a3b94)( qr[0], qr[5] ))
circuit.append(Gates.SGate( qr[4] ))
circuit.append(Gates.SXGate( qr[0] ))
circuit.append(Gates.ZGate( qr[4] ))
circuit.append(Gates.CRZGate(p_5ed9e5)( qr[0], qr[5] ))
circuit.append(Gates.CU1Gate(p_84dd61)( qr[1], qr[4] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))



circuit = cirq.resolve_parameters(circuit, {
    "p_72af2c": 1.4112277317699358,
    "p_5ed9e5": 4.833923139882297,
    "p_d7cead": 2.3864521352475245,
    "p_6a555a": 6.163759533339787,
    "p_86b1e1": 0.07157463504881167,
    "p_02e598": 3.2142159669963557,
    "p_c6dce3": 0.5112149185250571,
    "p_7d8767": 5.987304452123941,
    "p_6849dc": 5.897054719225356,
    "p_84dd61": 4.028174522740928,
    "p_7fd6f3": 4.2641612072511235,
    "p_1a3b94": 5.1829934776392745,
    "p_2d35e2": 4.229610589867865,
    "p_ba2c5d": 5.887184334931191
}, recursive=True)
        








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

