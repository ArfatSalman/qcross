
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(10)]

p_bef792 = Symbol('p_bef792')
p_16c66f = Symbol('p_16c66f')
p_72801a = Symbol('p_72801a')
p_adfdc7 = Symbol('p_adfdc7')
p_a3b68b = Symbol('p_a3b68b')
p_35f264 = Symbol('p_35f264')
p_477e3c = Symbol('p_477e3c')
p_e721ac = Symbol('p_e721ac')
p_70b332 = Symbol('p_70b332')
p_8ead38 = Symbol('p_8ead38')
p_dc333a = Symbol('p_dc333a')
p_f7eb17 = Symbol('p_f7eb17')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(6.163759533339787)( qr[3] ))
circuit.append(Gates.CRZGate(p_adfdc7)( qr[6], qr[3] ))
circuit.append(Gates.CRXGate(p_e721ac)( qr[1], qr[7] ))
circuit.append(Gates.CCXGate( qr[5], qr[9], qr[7] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.TGate( qr[9] ))
circuit.append(Gates.XGate( qr[8] ))
circuit.append(Gates.CRZGate(4.167661441102218)( qr[1], qr[6] ))
circuit.append(Gates.RZGate(p_70b332)( qr[1] ))
circuit.append(Gates.SXGate( qr[2] ))
circuit.append(Gates.CSXGate( qr[4], qr[8] ))
circuit.append(Gates.CCXGate( qr[4], qr[9], qr[5] ))
circuit.append(Gates.C3SXGate( qr[2], qr[4], qr[0], qr[9] ))
circuit.append(Gates.CSXGate( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.CHGate( qr[7], qr[1] ))
circuit.append(Gates.CSXGate( qr[2], qr[0] ))
circuit.append(Gates.CRZGate(p_35f264)( qr[1], qr[2] ))
circuit.append(Gates.U2Gate(p_a3b68b, p_72801a)( qr[2] ))
circuit.append(Gates.TGate( qr[0] ))
circuit.append(Gates.SXdgGate( qr[9] ))
circuit.append(Gates.TGate( qr[8] ))
circuit.append(Gates.RZGate(p_bef792)( qr[1] ))
circuit.append(Gates.CRXGate(p_8ead38)( qr[7], qr[1] ))
circuit.append(Gates.UGate(p_16c66f, p_477e3c, p_f7eb17)( qr[2] ))
circuit.append(Gates.ECRGate( qr[4], qr[8] ))
circuit.append(Gates.ZGate( qr[3] ))
circuit.append(Gates.ZGate( qr[8] ))
circuit.append(Gates.CSXGate( qr[1], qr[7] ))
circuit.append(Gates.RZGate(p_dc333a)( qr[5] ))
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



circuit = cirq.resolve_parameters(circuit, {
    "p_bef792": 5.014941143947427,
    "p_16c66f": 5.080799300534071,
    "p_72801a": 2.1276323672732023,
    "p_adfdc7": 4.2641612072511235,
    "p_a3b68b": 2.5163050709890156,
    "p_35f264": 2.586208953975239,
    "p_477e3c": 5.023617931957853,
    "p_e721ac": 5.987304452123941,
    "p_70b332": 4.229610589867865,
    "p_8ead38": 5.970852306777193,
    "p_dc333a": 3.6614081973587154,
    "p_f7eb17": 2.271164628944128
}, recursive=True)
        










simulator = cirq.DensityMatrixSimulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=5542)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7', 'cr8', 'cr9'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

