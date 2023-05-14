
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(9)]

p_0272f7 = Symbol('p_0272f7')
p_ea3f54 = Symbol('p_ea3f54')
p_0ac6c9 = Symbol('p_0ac6c9')
p_4e1de3 = Symbol('p_4e1de3')
p_7a489b = Symbol('p_7a489b')
p_74b354 = Symbol('p_74b354')
p_331ab9 = Symbol('p_331ab9')
p_2c12c6 = Symbol('p_2c12c6')
p_41dadf = Symbol('p_41dadf')
p_12df2a = Symbol('p_12df2a')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_2c12c6)( qr[8] ))
circuit.append(Gates.CSXGate( qr[2], qr[4] ))
circuit.append(Gates.CUGate(p_41dadf, p_7a489b, p_12df2a, p_4e1de3)( qr[0], qr[6] ))
circuit.append(Gates.SdgGate( qr[1] ))
circuit.append(Gates.C3SXGate( qr[0], qr[8], qr[7], qr[5] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.XGate( qr[5] ))
circuit.append(Gates.SGate( qr[0] ))
circuit.append(Gates.SGate( qr[8] ))
circuit.append(Gates.C3SXGate( qr[1], qr[3], qr[2], qr[0] ))
circuit.append(Gates.SXGate( qr[0] ))
circuit.append(Gates.CU1Gate(p_0ac6c9)( qr[8], qr[3] ))
circuit.append(Gates.CRZGate(p_74b354)( qr[5], qr[8] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.CSXGate( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[7] ))
circuit.append(Gates.CHGate( qr[6], qr[1] ))
circuit.append(Gates.CSXGate( qr[3], qr[0] ))
circuit.append(Gates.CRZGate(p_ea3f54)( qr[1], qr[2] ))
circuit.append(Gates.U2Gate(p_0272f7, p_331ab9)( qr[2] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))
circuit.append(cirq.measure(qr[7], key='cr7'))
circuit.append(cirq.measure(qr[8], key='cr8'))



circuit = cirq.resolve_parameters(circuit, {
    "p_0272f7": 2.5163050709890156,
    "p_ea3f54": 2.586208953975239,
    "p_0ac6c9": 3.2142159669963557,
    "p_4e1de3": 5.987304452123941,
    "p_7a489b": 5.897054719225356,
    "p_74b354": 1.4112277317699358,
    "p_331ab9": 2.1276323672732023,
    "p_2c12c6": 6.163759533339787,
    "p_41dadf": 0.5112149185250571,
    "p_12df2a": 2.3864521352475245
}, recursive=True)
        










simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=3919)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7', 'cr8'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

