
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(10)]

p_ce7cb6 = Symbol('p_ce7cb6')
p_97c5b0 = Symbol('p_97c5b0')
p_3124eb = Symbol('p_3124eb')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_3124eb)( qr[4] ))
circuit.append(Gates.CRZGate(4.2641612072511235)( qr[2], qr[4] ))
circuit.append(Gates.CRXGate(p_ce7cb6)( qr[1], qr[3] ))
circuit.append(Gates.CCXGate( qr[5], qr[9], qr[3] ))
circuit.append(Gates.ZGate( qr[6] ))
circuit.append(Gates.TGate( qr[9] ))
circuit.append(Gates.XGate( qr[8] ))
circuit.append(Gates.CRZGate(4.167661441102218)( qr[1], qr[2] ))
circuit.append(Gates.RZGate(p_97c5b0)( qr[1] ))
circuit.append(Gates.SXGate( qr[6] ))
circuit.append(Gates.CSXGate( qr[7], qr[8] ))
circuit.append(Gates.CCXGate( qr[7], qr[9], qr[5] ))
circuit.append(Gates.C3SXGate( qr[6], qr[7], qr[0], qr[9] ))
circuit.append(Gates.CSXGate( qr[0], qr[6] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.CHGate( qr[3], qr[1] ))
circuit.append(Gates.CSXGate( qr[6], qr[0] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[6], key='cr2'))
circuit.append(cirq.measure(qr[4], key='cr3'))
circuit.append(cirq.measure(qr[7], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[2], key='cr6'))
circuit.append(cirq.measure(qr[3], key='cr7'))
circuit.append(cirq.measure(qr[8], key='cr8'))
circuit.append(cirq.measure(qr[9], key='cr9'))



circuit = cirq.resolve_parameters(circuit, {
    "p_ce7cb6": 5.987304452123941,
    "p_97c5b0": 4.229610589867865,
    "p_3124eb": 6.163759533339787
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

