
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(8)]

p_dcc7c3 = Symbol('p_dcc7c3')
p_883ff5 = Symbol('p_883ff5')
p_cbd7c7 = Symbol('p_cbd7c7')
p_ac7c01 = Symbol('p_ac7c01')
p_a8d127 = Symbol('p_a8d127')
p_464996 = Symbol('p_464996')
p_cdc516 = Symbol('p_cdc516')
p_f56c05 = Symbol('p_f56c05')
p_93f2a9 = Symbol('p_93f2a9')
p_1c4575 = Symbol('p_1c4575')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_883ff5)( qr[4] ))
circuit.append(Gates.ZGate( qr[6] ))
circuit.append(Gates.XGate( qr[6] ))
circuit.append(Gates.CRXGate(p_a8d127)( qr[0], qr[6] ))
circuit.append(Gates.CRZGate(p_f56c05)( qr[1], qr[6] ))
circuit.append(Gates.C3SXGate( qr[0], qr[7], qr[6], qr[3] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.RYYGate(p_1c4575)( qr[6], qr[7] ))
circuit.append(Gates.CRZGate(p_cdc516)( qr[1], qr[7] ))
circuit.append(Gates.RZGate(p_93f2a9)( qr[1] ))
circuit.append(Gates.SXGate( qr[0] ))
circuit.append(Gates.CU1Gate(p_cbd7c7)( qr[4], qr[0] ))
circuit.append(Gates.CRXGate(p_464996)( qr[6], qr[4] ))
circuit.append(Gates.RZZGate(p_dcc7c3)( qr[7], qr[0] ))
circuit.append(Gates.CSXGate( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[6] ))
circuit.append(Gates.RZGate(p_ac7c01)( qr[4] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))
circuit.append(cirq.measure(qr[7], key='cr7'))



circuit = cirq.resolve_parameters(circuit, {
    "p_dcc7c3": 5.1829934776392745,
    "p_883ff5": 6.163759533339787,
    "p_cbd7c7": 3.2142159669963557,
    "p_ac7c01": 3.775592041307464,
    "p_a8d127": 5.987304452123941,
    "p_464996": 5.94477504571567,
    "p_cdc516": 4.167661441102218,
    "p_f56c05": 1.0296448789776642,
    "p_93f2a9": 4.229610589867865,
    "p_1c4575": 1.740253089260498
}, recursive=True)
        






qasm_output = cirq.qasm(cirq.expand_composite(circuit))
circuit = circuit_from_qasm(qasm_output) # new circuit





simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=2771)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['m_cr0_0', 'm_cr1_0', 'm_cr2_0', 'm_cr3_0', 'm_cr4_0', 'm_cr5_0', 'm_cr6_0', 'm_cr7_0'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

