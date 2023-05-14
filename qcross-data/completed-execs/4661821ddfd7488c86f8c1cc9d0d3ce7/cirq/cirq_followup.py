
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(6)]

p_8fbc55 = Symbol('p_8fbc55')
p_57585f = Symbol('p_57585f')
p_285ae7 = Symbol('p_285ae7')
p_0602a6 = Symbol('p_0602a6')
p_0a2147 = Symbol('p_0a2147')
p_bb1901 = Symbol('p_bb1901')
p_82597a = Symbol('p_82597a')
p_34e682 = Symbol('p_34e682')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_34e682)( qr[4] ))
circuit.append(Gates.ZGate( qr[3] ))
circuit.append(Gates.CRZGate(p_0602a6)( qr[2], qr[4] ))
circuit.append(Gates.CUGate(p_285ae7, p_bb1901, p_8fbc55, p_57585f)( qr[2], qr[3] ))
circuit.append(Gates.C3SXGate( qr[1], qr[4], qr[0], qr[2] ))
circuit.append(Gates.CCXGate( qr[1], qr[5], qr[0] ))
circuit.append(Gates.C3SXGate( qr[4], qr[3], qr[5], qr[0] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.TGate( qr[4] ))
circuit.append(Gates.RCCXGate( qr[5], qr[3], qr[4] ))
circuit.append(Gates.SGate( qr[5] ))
circuit.append(Gates.CRZGate(p_82597a)( qr[1], qr[5] ))
circuit.append(Gates.RZGate(p_0a2147)( qr[1] ))
circuit.append(Gates.C3SXGate( qr[0], qr[2], qr[1], qr[3] ))
circuit.append(Gates.CU1Gate(3.2142159669963557)( qr[3], qr[0] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))



circuit = cirq.resolve_parameters(circuit, {
    "p_8fbc55": 2.3864521352475245,
    "p_57585f": 5.987304452123941,
    "p_285ae7": 0.5112149185250571,
    "p_0602a6": 4.2641612072511235,
    "p_0a2147": 4.229610589867865,
    "p_bb1901": 5.897054719225356,
    "p_82597a": 4.167661441102218,
    "p_34e682": 6.163759533339787
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

