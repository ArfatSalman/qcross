
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(7)]

p_57577b = Symbol('p_57577b')
p_68346f = Symbol('p_68346f')
p_92d853 = Symbol('p_92d853')
p_8852a5 = Symbol('p_8852a5')
p_86d3c5 = Symbol('p_86d3c5')
p_877ff6 = Symbol('p_877ff6')
p_a29d5d = Symbol('p_a29d5d')
p_03605d = Symbol('p_03605d')
p_f61ac5 = Symbol('p_f61ac5')
p_9d2b67 = Symbol('p_9d2b67')
p_a10a46 = Symbol('p_a10a46')
p_aa393d = Symbol('p_aa393d')
p_17cd9d = Symbol('p_17cd9d')
p_8a5847 = Symbol('p_8a5847')
p_ec60d4 = Symbol('p_ec60d4')
p_4c3455 = Symbol('p_4c3455')
p_0783a3 = Symbol('p_0783a3')
p_655fcc = Symbol('p_655fcc')
p_169d88 = Symbol('p_169d88')
p_6773c4 = Symbol('p_6773c4')
p_b5202c = Symbol('p_b5202c')
p_fa03ad = Symbol('p_fa03ad')
p_823d76 = Symbol('p_823d76')

circuit = cirq.Circuit()

circuit.append(Gates.RYYGate(p_86d3c5)( qr[0], qr[5] ))
circuit.append(Gates.PhaseGate(p_03605d)( qr[6] ))
circuit.append(Gates.RYGate(p_a29d5d)( qr[2] ))
circuit.append(Gates.CU1Gate(p_823d76)( qr[4], qr[1] ))
circuit.append(Gates.CCXGate( qr[4], qr[3], qr[2] ))
circuit.append(Gates.ECRGate( qr[0], qr[6] ))
circuit.append(Gates.CSwapGate( qr[0], qr[6], qr[4] ))
circuit.append(Gates.ECRGate( qr[2], qr[0] ))
circuit.append(Gates.SwapGate( qr[3], qr[5] ))
circuit.append(Gates.CSwapGate( qr[3], qr[6], qr[1] ))
circuit.append(Gates.RC3XGate( qr[6], qr[1], qr[4], qr[0] ))
circuit.append(Gates.HGate( qr[2] ))
circuit.append(Gates.UGate(p_68346f, p_fa03ad, p_92d853)( qr[2] ))
circuit.append(Gates.U2Gate(p_8852a5, p_4c3455)( qr[4] ))
circuit.append(Gates.CSGate( qr[2], qr[5] ))
circuit.append(Gates.U2Gate(p_0783a3, p_169d88)( qr[6] ))
circuit.append(Gates.RYYGate(p_6773c4)( qr[1], qr[5] ))
circuit.append(Gates.RC3XGate( qr[3], qr[1], qr[4], qr[5] ))
circuit.append(Gates.UGate(p_aa393d, p_8a5847, p_655fcc)( qr[3] ))
circuit.append(Gates.CUGate(p_877ff6, p_ec60d4, p_f61ac5, p_b5202c)( qr[3], qr[5] ))
circuit.append(Gates.U2Gate(p_17cd9d, p_a10a46)( qr[6] ))
circuit.append(Gates.RC3XGate( qr[1], qr[3], qr[2], qr[0] ))
circuit.append(Gates.RXGate(p_57577b)( qr[0] ))
circuit.append(Gates.CRYGate(p_9d2b67)( qr[6], qr[1] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))



circuit = cirq.resolve_parameters(circuit, {
    "p_57577b": 5.129266867572668,
    "p_68346f": 5.066050249739578,
    "p_92d853": 2.5510590709018732,
    "p_8852a5": 4.9702527118009066,
    "p_86d3c5": 1.7892872835005398,
    "p_877ff6": 5.814210499839879,
    "p_a29d5d": 3.6138974545836176,
    "p_03605d": 3.7964394792576885,
    "p_f61ac5": 5.986977817617511,
    "p_9d2b67": 2.998268232293747,
    "p_a10a46": 2.4524844691285543,
    "p_aa393d": 0.8822742453157227,
    "p_17cd9d": 4.95448520957096,
    "p_8a5847": 3.4849606070943584,
    "p_ec60d4": 2.2396990253899713,
    "p_4c3455": 3.5114983819004046,
    "p_0783a3": 1.6924855892819173,
    "p_655fcc": 4.713462039096519,
    "p_169d88": 6.035455549292343,
    "p_6773c4": 3.0928548495797905,
    "p_b5202c": 6.091448724065051,
    "p_fa03ad": 3.676251393433825,
    "p_823d76": 4.877167017151953
}, recursive=True)
        










simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=1959)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

