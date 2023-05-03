
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(6)]

p_7ebac6 = Symbol('p_7ebac6')
p_02fa5f = Symbol('p_02fa5f')
p_68bc2a = Symbol('p_68bc2a')
p_b1a917 = Symbol('p_b1a917')
p_d2b847 = Symbol('p_d2b847')
p_98866e = Symbol('p_98866e')
p_896a7d = Symbol('p_896a7d')
p_583e59 = Symbol('p_583e59')
p_eef840 = Symbol('p_eef840')

circuit = cirq.Circuit()


subcircuit = cirq.Circuit()
subcircuit.append(Gates.RZGate(p_896a7d)( qr[2] ))
subcircuit.append(Gates.TGate( qr[1] ))
subcircuit.append(Gates.CUGate(p_98866e, p_d2b847, 5.631160518436971, p_02fa5f)( qr[0], qr[3] ))
subcircuit.append(Gates.TGate( qr[2] ))
subcircuit.append(Gates.RZXGate(p_583e59)( qr[4], qr[0] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.RZGate(6.163759533339787)( qr[4] ))
circuit.append(Gates.ZGate( qr[3] ))
circuit.append(Gates.CRZGate(p_eef840)( qr[2], qr[4] ))
circuit.append(Gates.CUGate(p_68bc2a, p_b1a917, p_7ebac6, 5.987304452123941)( qr[2], qr[3] ))
circuit.append(Gates.C3SXGate( qr[1], qr[4], qr[0], qr[2] ))
circuit.append(Gates.CCXGate( qr[1], qr[5], qr[0] ))
circuit.append(Gates.C3SXGate( qr[4], qr[3], qr[5], qr[0] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.TGate( qr[4] ))
circuit.append(Gates.RCCXGate( qr[5], qr[3], qr[4] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))



circuit = cirq.resolve_parameters(circuit, {
    "p_7ebac6": 2.3864521352475245,
    "p_02fa5f": 2.9151388486514547,
    "p_68bc2a": 0.5112149185250571,
    "p_b1a917": 5.897054719225356,
    "p_d2b847": 2.696266694818697,
    "p_98866e": 4.229610589867865,
    "p_896a7d": 3.672121211148789,
    "p_583e59": 4.563562108824195,
    "p_eef840": 4.2641612072511235
}, recursive=True)
        










simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=1385)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

