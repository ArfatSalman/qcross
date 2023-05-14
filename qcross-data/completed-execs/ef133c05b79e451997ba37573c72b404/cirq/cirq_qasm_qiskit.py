
import cirq
import qiskit
from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(8)]

p_37851b = Symbol('p_37851b')
p_771172 = Symbol('p_771172')
p_e59639 = Symbol('p_e59639')
p_432785 = Symbol('p_432785')
p_0f1b6d = Symbol('p_0f1b6d')
p_f2cc7e = Symbol('p_f2cc7e')
p_2c778f = Symbol('p_2c778f')
p_0c9124 = Symbol('p_0c9124')
p_a04195 = Symbol('p_a04195')
p_2361ce = Symbol('p_2361ce')
p_3f48eb = Symbol('p_3f48eb')
p_acd647 = Symbol('p_acd647')
p_609841 = Symbol('p_609841')
p_fc560c = Symbol('p_fc560c')
p_1a7816 = Symbol('p_1a7816')
p_981c1e = Symbol('p_981c1e')
p_484055 = Symbol('p_484055')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_3f48eb)( qr[4] ))
circuit.append(Gates.ZGate( qr[6] ))
circuit.append(Gates.XGate( qr[6] ))
circuit.append(Gates.CRXGate(p_2361ce)( qr[0], qr[6] ))
circuit.append(Gates.CRZGate(1.0296448789776642)( qr[1], qr[6] ))
circuit.append(Gates.C3SXGate( qr[0], qr[7], qr[6], qr[3] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.RYYGate(1.740253089260498)( qr[6], qr[7] ))
circuit.append(Gates.CRZGate(p_771172)( qr[1], qr[7] ))
circuit.append(Gates.RZGate(4.229610589867865)( qr[1] ))
circuit.append(Gates.SXGate( qr[0] ))
circuit.append(Gates.CU1Gate(3.2142159669963557)( qr[4], qr[0] ))
circuit.append(Gates.CRXGate(p_0f1b6d)( qr[6], qr[4] ))
circuit.append(Gates.RZZGate(5.1829934776392745)( qr[7], qr[0] ))
circuit.append(Gates.CSXGate( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[6] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.CUGate(4.722103101046168, 5.3924725338944945, 4.88987246261121, p_609841)( qr[2], qr[0] ))
subcircuit.append(Gates.CUGate(2.862865991712737, 6.0504088665633065, p_e59639, p_0c9124)( qr[3], qr[6] ))
subcircuit.append(Gates.RXGate(3.698825211554417)( qr[3] ))
subcircuit.append(Gates.CHGate( qr[1], qr[6] ))
subcircuit.append(Gates.U2Gate(p_a04195, 1.0052392769301404)( qr[4] ))
subcircuit.append(Gates.RZGate(3.2374432046466546)( qr[7] ))
subcircuit.append(Gates.SXdgGate( qr[7] ))
subcircuit.append(Gates.CPhaseGate(p_acd647)( qr[7], qr[6] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.RZGate(p_f2cc7e)( qr[4] ))
circuit.append(Gates.CRXGate(p_484055)( qr[0], qr[3] ))
circuit.append(Gates.CUGate(5.03147076606842, p_fc560c, p_1a7816, p_37851b)( qr[6], qr[2] ))
circuit.append(Gates.U2Gate(p_981c1e, p_2c778f)( qr[2] ))
circuit.append(Gates.TGate( qr[6] ))
circuit.append(Gates.SdgGate( qr[0] ))
circuit.append(Gates.RZZGate(p_432785)( qr[3], qr[4] ))
circuit.append(Gates.TGate( qr[5] ))
circuit.append(Gates.RYYGate(1.9669252191306448)( qr[4], qr[2] ))
circuit.append(Gates.C3SXGate( qr[1], qr[3], qr[2], qr[5] ))
circuit.append(Gates.SXdgGate( qr[7] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))
circuit.append(cirq.measure(qr[7], key='cr7'))



circuit = cirq.resolve_parameters(circuit, {
    "p_37851b": 4.940217775579305,
    "p_771172": 4.167661441102218,
    "p_e59639": 1.7203758404994713,
    "p_432785": 3.950837470808744,
    "p_0f1b6d": 5.94477504571567,
    "p_f2cc7e": 3.775592041307464,
    "p_2c778f": 2.1276323672732023,
    "p_0c9124": 2.8704483107274004,
    "p_a04195": 0.25812405723927917,
    "p_2361ce": 5.987304452123941,
    "p_3f48eb": 6.163759533339787,
    "p_acd647": 1.672427069032094,
    "p_609841": 1.2497571638956968,
    "p_fc560c": 5.0063780207098425,
    "p_1a7816": 3.1562533916051736,
    "p_981c1e": 2.5163050709890156,
    "p_484055": 0.7279391018916035
}, recursive=True)
        








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

