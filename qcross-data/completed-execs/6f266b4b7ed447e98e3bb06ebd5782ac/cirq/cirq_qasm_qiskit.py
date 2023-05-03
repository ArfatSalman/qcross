
import cirq
import qiskit
from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(5)]

p_466c3c = Symbol('p_466c3c')
p_fb2b59 = Symbol('p_fb2b59')
p_f17856 = Symbol('p_f17856')
p_b0d476 = Symbol('p_b0d476')
p_c9d928 = Symbol('p_c9d928')
p_faf457 = Symbol('p_faf457')
p_cd9fd2 = Symbol('p_cd9fd2')
p_d9736e = Symbol('p_d9736e')
p_38ffe1 = Symbol('p_38ffe1')
p_305826 = Symbol('p_305826')
p_2e343f = Symbol('p_2e343f')
p_3eae93 = Symbol('p_3eae93')
p_499aed = Symbol('p_499aed')
p_40b220 = Symbol('p_40b220')
p_fbab31 = Symbol('p_fbab31')
p_6f4c81 = Symbol('p_6f4c81')
p_3681fa = Symbol('p_3681fa')
p_697593 = Symbol('p_697593')
p_e1e662 = Symbol('p_e1e662')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_d9736e)( qr[3] ))
circuit.append(Gates.SXdgGate( qr[2] ))
circuit.append(Gates.CSXGate( qr[1], qr[0] ))
circuit.append(Gates.ECRGate( qr[3], qr[2] ))
circuit.append(Gates.CRXGate(p_499aed)( qr[4], qr[3] ))
circuit.append(Gates.SGate( qr[0] ))
circuit.append(Gates.CRZGate(p_c9d928)( qr[3], qr[4] ))
circuit.append(Gates.CHGate( qr[1], qr[4] ))
circuit.append(Gates.RYYGate(p_e1e662)( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.TGate( qr[4] ))
circuit.append(Gates.CSXGate( qr[1], qr[4] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(Gates.SGate( qr[4] ))
circuit.append(Gates.CUGate(p_b0d476, p_40b220, 4.623446645668956, p_fb2b59)( qr[1], qr[4] ))
circuit.append(Gates.RZGate(p_466c3c)( qr[1] ))
circuit.append(Gates.RYYGate(p_3681fa)( qr[0], qr[2] ))
circuit.append(Gates.CU1Gate(p_38ffe1)( qr[3], qr[0] ))
circuit.append(Gates.UGate(p_6f4c81, p_3eae93, p_f17856)( qr[4] ))
circuit.append(Gates.CHGate( qr[2], qr[0] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.SGate( qr[2] ))
circuit.append(Gates.CSXGate( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[3] ))
circuit.append(Gates.CHGate( qr[0], qr[4] ))
circuit.append(Gates.CHGate( qr[0], qr[1] ))
circuit.append(Gates.CU1Gate(p_fbab31)( qr[0], qr[3] ))
circuit.append(Gates.RCCXGate( qr[0], qr[3], qr[1] ))
circuit.append(Gates.CUGate(p_2e343f, p_faf457, p_305826, p_697593)( qr[4], qr[3] ))
circuit.append(Gates.CRZGate(p_cd9fd2)( qr[2], qr[1] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))



circuit = cirq.resolve_parameters(circuit, {
    "p_466c3c": 4.229610589867865,
    "p_fb2b59": 3.865496458458116,
    "p_f17856": 1.4112277317699358,
    "p_b0d476": 5.708725119517347,
    "p_c9d928": 1.0296448789776642,
    "p_faf457": 5.0063780207098425,
    "p_cd9fd2": 3.839241945509346,
    "p_d9736e": 6.163759533339787,
    "p_38ffe1": 3.2142159669963557,
    "p_305826": 3.1562533916051736,
    "p_2e343f": 5.03147076606842,
    "p_3eae93": 0.07157463504881167,
    "p_499aed": 2.0099472182748075,
    "p_40b220": 4.167661441102218,
    "p_fbab31": 4.028174522740928,
    "p_6f4c81": 5.887184334931191,
    "p_3681fa": 5.398622178940033,
    "p_697593": 4.940217775579305,
    "p_e1e662": 1.6723037552953224
}, recursive=True)
        








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

