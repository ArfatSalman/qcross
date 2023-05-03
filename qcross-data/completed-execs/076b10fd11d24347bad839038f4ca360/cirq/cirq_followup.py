
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(11)]

p_925c46 = Symbol('p_925c46')
p_b15ae8 = Symbol('p_b15ae8')
p_a28ef6 = Symbol('p_a28ef6')
p_40ca7b = Symbol('p_40ca7b')
p_26612a = Symbol('p_26612a')
p_0b1992 = Symbol('p_0b1992')
p_e50c6e = Symbol('p_e50c6e')
p_01d286 = Symbol('p_01d286')
p_635d83 = Symbol('p_635d83')
p_8885ef = Symbol('p_8885ef')
p_60901c = Symbol('p_60901c')
p_2c0ff7 = Symbol('p_2c0ff7')
p_97cf30 = Symbol('p_97cf30')

circuit = cirq.Circuit()


subcircuit = cirq.Circuit()
subcircuit.append(Gates.ECRGate( qr[2], qr[5] ))
subcircuit.append(Gates.RZGate(p_0b1992)( qr[1] ))
subcircuit.append(Gates.DCXGate( qr[0], qr[5] ))
subcircuit.append(Gates.SXdgGate( qr[2] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.RZGate(p_e50c6e)( qr[3] ))
circuit.append(Gates.CRZGate(p_635d83)( qr[6], qr[2] ))
circuit.append(Gates.ZGate( qr[1] ))
circuit.append(Gates.CCXGate( qr[5], qr[9], qr[7] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.XGate( qr[7] ))
circuit.append(Gates.RCCXGate( qr[10], qr[6], qr[8] ))
circuit.append(Gates.RZGate(p_60901c)( qr[0] ))
circuit.append(Gates.CCXGate( qr[7], qr[10], qr[2] ))
circuit.append(Gates.SdgGate( qr[7] ))
circuit.append(Gates.U2Gate(p_01d286, p_2c0ff7)( qr[10] ))
circuit.append(Gates.CSXGate( qr[3], qr[2] ))
circuit.append(Gates.CHGate( qr[0], qr[7] ))
circuit.append(Gates.CU1Gate(p_a28ef6)( qr[9], qr[0] ))
circuit.append(Gates.RZGate(p_26612a)( qr[6] ))
circuit.append(Gates.U2Gate(p_97cf30, p_925c46)( qr[2] ))
circuit.append(Gates.TGate( qr[0] ))
circuit.append(Gates.RZZGate(p_b15ae8)( qr[4], qr[0] ))
circuit.append(Gates.TGate( qr[0] ))
circuit.append(Gates.TGate( qr[1] ))
circuit.append(Gates.SXdgGate( qr[5] ))
circuit.append(Gates.RZGate(p_8885ef)( qr[2] ))
circuit.append(Gates.CRZGate(p_40ca7b)( qr[5], qr[3] ))
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
    "p_925c46": 2.1276323672732023,
    "p_b15ae8": 3.950837470808744,
    "p_a28ef6": 4.028174522740928,
    "p_40ca7b": 0.6393443962862078,
    "p_26612a": 5.0063780207098425,
    "p_0b1992": 3.3407994338317226,
    "p_e50c6e": 6.163759533339787,
    "p_01d286": 4.214504315296764,
    "p_635d83": 4.2641612072511235,
    "p_8885ef": 4.722103101046168,
    "p_60901c": 4.229610589867865,
    "p_2c0ff7": 4.6235667602042065,
    "p_97cf30": 2.5163050709890156
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

