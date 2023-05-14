
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(11)]

p_b3b922 = Symbol('p_b3b922')
p_a1819b = Symbol('p_a1819b')
p_d7cdb5 = Symbol('p_d7cdb5')
p_b0de03 = Symbol('p_b0de03')
p_744464 = Symbol('p_744464')
p_1b382d = Symbol('p_1b382d')
p_c00892 = Symbol('p_c00892')

circuit = cirq.Circuit()


subcircuit = cirq.Circuit()
subcircuit.append(Gates.RZXGate(p_a1819b)( qr[10], qr[7] ))
subcircuit.append(Gates.CXGate( qr[2], qr[6] ))
subcircuit.append(Gates.CZGate( qr[7], qr[4] ))
subcircuit.append(Gates.CU1Gate(p_744464)( qr[1], qr[8] ))
subcircuit.append(Gates.CUGate(p_c00892, p_b3b922, 5.631160518436971, p_1b382d)( qr[0], qr[10] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.RZGate(p_d7cdb5)( qr[3] ))
circuit.append(Gates.CRZGate(p_b0de03)( qr[6], qr[2] ))
circuit.append(Gates.ZGate( qr[1] ))
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
circuit.append(cirq.measure(qr[10], key='cr10'))



circuit = cirq.resolve_parameters(circuit, {
    "p_b3b922": 2.696266694818697,
    "p_a1819b": 3.427505621225153,
    "p_d7cdb5": 6.163759533339787,
    "p_b0de03": 4.2641612072511235,
    "p_744464": 4.501598818751339,
    "p_1b382d": 2.9151388486514547,
    "p_c00892": 4.229610589867865
}, recursive=True)
        










simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=7838)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7', 'cr8', 'cr9', 'cr10'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

