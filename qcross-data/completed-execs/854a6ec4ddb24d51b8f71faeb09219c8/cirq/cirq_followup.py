
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(6)]

p_5a7038 = Symbol('p_5a7038')
p_7d6e79 = Symbol('p_7d6e79')
p_9f724d = Symbol('p_9f724d')
p_e94aea = Symbol('p_e94aea')
p_52b317 = Symbol('p_52b317')
p_320da9 = Symbol('p_320da9')
p_2b203d = Symbol('p_2b203d')
p_334c70 = Symbol('p_334c70')
p_94dcf5 = Symbol('p_94dcf5')

circuit = cirq.Circuit()


subcircuit = cirq.Circuit()
subcircuit.append(Gates.RZGate(p_2b203d)( qr[2] ))
subcircuit.append(Gates.TGate( qr[1] ))
subcircuit.append(Gates.CUGate(p_320da9, p_52b317, 5.631160518436971, p_7d6e79)( qr[0], qr[3] ))
subcircuit.append(Gates.TGate( qr[2] ))
subcircuit.append(Gates.RZXGate(p_334c70)( qr[4], qr[0] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.RZGate(6.163759533339787)( qr[4] ))
circuit.append(Gates.ZGate( qr[3] ))
circuit.append(Gates.CRZGate(p_94dcf5)( qr[2], qr[4] ))
circuit.append(Gates.CUGate(p_9f724d, p_e94aea, p_5a7038, 5.987304452123941)( qr[2], qr[3] ))
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
    "p_5a7038": 2.3864521352475245,
    "p_7d6e79": 2.9151388486514547,
    "p_9f724d": 0.5112149185250571,
    "p_e94aea": 5.897054719225356,
    "p_52b317": 2.696266694818697,
    "p_320da9": 4.229610589867865,
    "p_2b203d": 3.672121211148789,
    "p_334c70": 4.563562108824195,
    "p_94dcf5": 4.2641612072511235
}, recursive=True)
        






qasm_output = cirq.qasm(cirq.expand_composite(circuit))
circuit = circuit_from_qasm(qasm_output) # new circuit





simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=1385)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['m_cr0_0', 'm_cr1_0', 'm_cr2_0', 'm_cr3_0', 'm_cr4_0', 'm_cr5_0'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

