
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(5)]

p_628a76 = Symbol('p_628a76')
p_7b2ce0 = Symbol('p_7b2ce0')
p_1b05b2 = Symbol('p_1b05b2')
p_cb0ae5 = Symbol('p_cb0ae5')
p_af3d09 = Symbol('p_af3d09')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_cb0ae5)( qr[3] ))
circuit.append(Gates.SXdgGate( qr[2] ))
circuit.append(Gates.CSXGate( qr[1], qr[0] ))
circuit.append(Gates.ECRGate( qr[3], qr[2] ))
circuit.append(Gates.CRXGate(p_628a76)( qr[4], qr[3] ))
circuit.append(Gates.SGate( qr[0] ))
circuit.append(Gates.CRZGate(1.0296448789776642)( qr[3], qr[4] ))
circuit.append(Gates.CHGate( qr[1], qr[4] ))
circuit.append(Gates.RYYGate(1.6723037552953224)( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.TGate( qr[4] ))
circuit.append(Gates.CSXGate( qr[1], qr[4] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(Gates.SGate( qr[4] ))
circuit.append(Gates.CUGate(p_af3d09, 4.167661441102218, p_7b2ce0, p_1b05b2)( qr[1], qr[4] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))



circuit = cirq.resolve_parameters(circuit, {
    "p_628a76": 2.0099472182748075,
    "p_7b2ce0": 4.623446645668956,
    "p_1b05b2": 3.865496458458116,
    "p_cb0ae5": 6.163759533339787,
    "p_af3d09": 5.708725119517347
}, recursive=True)
        










simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=979)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

