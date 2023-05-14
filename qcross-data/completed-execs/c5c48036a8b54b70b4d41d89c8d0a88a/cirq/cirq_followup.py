
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(10)]

p_4534a2 = Symbol('p_4534a2')
p_c28457 = Symbol('p_c28457')
p_88080a = Symbol('p_88080a')
p_089fca = Symbol('p_089fca')
p_0aa97a = Symbol('p_0aa97a')
p_f1630e = Symbol('p_f1630e')
p_a25c71 = Symbol('p_a25c71')
p_63f494 = Symbol('p_63f494')
p_4537df = Symbol('p_4537df')
p_cab727 = Symbol('p_cab727')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_88080a)( qr[3] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.RZXGate(p_cab727)( qr[0], qr[6] ))
subcircuit.append(Gates.UGate(p_4534a2, p_0aa97a, p_c28457)( qr[5] ))
subcircuit.append(Gates.ZGate( qr[2] ))
subcircuit.append(Gates.UGate(p_63f494, 5.190931186022931, p_4537df)( qr[4] ))
subcircuit.append(Gates.DCXGate( qr[1], qr[8] ))
subcircuit.append(Gates.CUGate(p_f1630e, p_a25c71, 5.631160518436971, 2.9151388486514547)( qr[0], qr[9] ))
subcircuit.append(Gates.ECRGate( qr[9], qr[0] ))
subcircuit.append(Gates.C3XGate(p_089fca)( qr[6], qr[4], qr[8], qr[9] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.CRZGate(4.2641612072511235)( qr[6], qr[3] ))
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



circuit = cirq.resolve_parameters(circuit, {
    "p_4534a2": 2.6397681660693015,
    "p_c28457": 3.427505621225153,
    "p_88080a": 6.163759533339787,
    "p_089fca": 5.94477504571567,
    "p_0aa97a": 5.320621737498446,
    "p_f1630e": 4.229610589867865,
    "p_a25c71": 2.696266694818697,
    "p_63f494": 5.01836135520768,
    "p_4537df": 1.2128092629174942,
    "p_cab727": 0.6833824466861163
}, recursive=True)
        










simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=5542)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7', 'cr8', 'cr9'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

