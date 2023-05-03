
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(4)]

p_4d1002 = Symbol('p_4d1002')
p_95d4c5 = Symbol('p_95d4c5')
p_c4621c = Symbol('p_c4621c')
p_7c06d6 = Symbol('p_7c06d6')
p_1cef4d = Symbol('p_1cef4d')
p_643384 = Symbol('p_643384')
p_0fdd04 = Symbol('p_0fdd04')
p_27af66 = Symbol('p_27af66')
p_c93870 = Symbol('p_c93870')
p_acd0b1 = Symbol('p_acd0b1')
p_d935d2 = Symbol('p_d935d2')
p_56ef16 = Symbol('p_56ef16')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_95d4c5)( qr[1] ))
circuit.append(Gates.RZZGate(p_c93870)( qr[2], qr[3] ))
circuit.append(Gates.iSwapGate( qr[2], qr[3] ))
circuit.append(Gates.CSXGate( qr[1], qr[0] ))
circuit.append(Gates.XGate( qr[2] ))
circuit.append(Gates.CUGate(p_0fdd04, p_c4621c, p_7c06d6, p_1cef4d)( qr[0], qr[2] ))
circuit.append(Gates.CU1Gate(p_d935d2)( qr[3], qr[0] ))
circuit.append(Gates.CHGate( qr[3], qr[2] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.U1Gate(4.8767543643948805)( qr[0] ))
subcircuit.append(Gates.SwapGate( qr[2], qr[0] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.CHGate( qr[1], qr[2] ))
circuit.append(Gates.C3SXGate( qr[3], qr[0], qr[1], qr[2] ))
circuit.append(Gates.C3SXGate( qr[3], qr[1], qr[0], qr[2] ))
circuit.append(Gates.TGate( qr[2] ))
circuit.append(Gates.SXdgGate( qr[2] ))
circuit.append(Gates.TGate( qr[2] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(Gates.RCCXGate( qr[1], qr[0], qr[3] ))
circuit.append(Gates.RYYGate(p_acd0b1)( qr[2], qr[0] ))
circuit.append(Gates.RCCXGate( qr[2], qr[3], qr[0] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(Gates.SGate( qr[3] ))
circuit.append(Gates.CRZGate(p_643384)( qr[0], qr[1] ))
circuit.append(Gates.C3SXGate( qr[1], qr[2], qr[0], qr[3] ))
circuit.append(Gates.RYYGate(p_56ef16)( qr[2], qr[0] ))
circuit.append(Gates.SXdgGate( qr[0] ))
circuit.append(Gates.CU1Gate(p_27af66)( qr[0], qr[3] ))
circuit.append(Gates.iSwapGate( qr[1], qr[0] ))
circuit.append(Gates.CRXGate(p_4d1002)( qr[2], qr[0] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))



circuit = cirq.resolve_parameters(circuit, {
    "p_4d1002": 5.94477504571567,
    "p_95d4c5": 6.163759533339787,
    "p_c4621c": 5.897054719225356,
    "p_7c06d6": 2.3864521352475245,
    "p_1cef4d": 5.987304452123941,
    "p_643384": 2.9790366726895714,
    "p_0fdd04": 0.5112149185250571,
    "p_27af66": 3.2142159669963557,
    "p_c93870": 4.066449154047175,
    "p_acd0b1": 1.740253089260498,
    "p_d935d2": 5.154187354656876,
    "p_56ef16": 5.398622178940033
}, recursive=True)
        










simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=692)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

