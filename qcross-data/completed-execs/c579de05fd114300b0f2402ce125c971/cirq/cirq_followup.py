
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(6)]

p_d25745 = Symbol('p_d25745')
p_7280db = Symbol('p_7280db')
p_66bc6f = Symbol('p_66bc6f')
p_7efb1a = Symbol('p_7efb1a')
p_9e0b52 = Symbol('p_9e0b52')
p_6a275f = Symbol('p_6a275f')
p_a8dc96 = Symbol('p_a8dc96')
p_6c61a4 = Symbol('p_6c61a4')
p_0f968c = Symbol('p_0f968c')
p_55502a = Symbol('p_55502a')
p_74ecdc = Symbol('p_74ecdc')
p_3ebfd3 = Symbol('p_3ebfd3')
p_eb0914 = Symbol('p_eb0914')
p_e304cd = Symbol('p_e304cd')
p_5dbd96 = Symbol('p_5dbd96')
p_0caccb = Symbol('p_0caccb')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_0caccb)( qr[4] ))
circuit.append(Gates.ZGate( qr[3] ))
circuit.append(Gates.CRZGate(p_9e0b52)( qr[1], qr[4] ))
circuit.append(Gates.CUGate(p_55502a, p_74ecdc, p_5dbd96, p_66bc6f)( qr[1], qr[3] ))
circuit.append(Gates.C3SXGate( qr[2], qr[4], qr[0], qr[1] ))
circuit.append(Gates.CCXGate( qr[2], qr[5], qr[0] ))
circuit.append(Gates.C3SXGate( qr[4], qr[3], qr[5], qr[0] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.ZGate( qr[1] ))
circuit.append(Gates.TGate( qr[4] ))
circuit.append(Gates.RCCXGate( qr[5], qr[3], qr[4] ))
circuit.append(Gates.SGate( qr[5] ))
circuit.append(Gates.CRZGate(p_a8dc96)( qr[2], qr[5] ))
circuit.append(Gates.RZGate(p_6c61a4)( qr[2] ))
circuit.append(Gates.C3SXGate( qr[0], qr[1], qr[2], qr[3] ))
circuit.append(Gates.CU1Gate(p_3ebfd3)( qr[3], qr[0] ))
circuit.append(Gates.UGate(p_e304cd, p_0f968c, p_6a275f)( qr[5] ))
circuit.append(Gates.RZZGate(p_d25745)( qr[0], qr[5] ))
circuit.append(Gates.SGate( qr[4] ))
circuit.append(Gates.SXGate( qr[0] ))
circuit.append(Gates.ZGate( qr[4] ))
circuit.append(Gates.CRZGate(p_eb0914)( qr[0], qr[5] ))
circuit.append(Gates.CU1Gate(p_7efb1a)( qr[2], qr[4] ))
circuit.append(Gates.C3SXGate( qr[3], qr[0], qr[4], qr[1] ))
circuit.append(Gates.CRZGate(p_7280db)( qr[1], qr[5] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[2], key='cr1'))
circuit.append(cirq.measure(qr[1], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))



circuit = cirq.resolve_parameters(circuit, {
    "p_d25745": 5.1829934776392745,
    "p_7280db": 2.586208953975239,
    "p_66bc6f": 5.987304452123941,
    "p_7efb1a": 4.028174522740928,
    "p_9e0b52": 4.2641612072511235,
    "p_6a275f": 1.4112277317699358,
    "p_a8dc96": 4.167661441102218,
    "p_6c61a4": 4.229610589867865,
    "p_0f968c": 0.07157463504881167,
    "p_55502a": 0.5112149185250571,
    "p_74ecdc": 5.897054719225356,
    "p_3ebfd3": 3.2142159669963557,
    "p_eb0914": 4.833923139882297,
    "p_e304cd": 5.887184334931191,
    "p_5dbd96": 2.3864521352475245,
    "p_0caccb": 6.163759533339787
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

