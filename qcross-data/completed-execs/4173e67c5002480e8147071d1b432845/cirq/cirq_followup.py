
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(8)]

p_aab82c = Symbol('p_aab82c')
p_61e37c = Symbol('p_61e37c')
p_3f39bf = Symbol('p_3f39bf')
p_e66f86 = Symbol('p_e66f86')
p_d9b3b7 = Symbol('p_d9b3b7')
p_58380b = Symbol('p_58380b')
p_4bf6d4 = Symbol('p_4bf6d4')
p_457d2e = Symbol('p_457d2e')
p_dc6a99 = Symbol('p_dc6a99')
p_2fe099 = Symbol('p_2fe099')
p_b5cb9c = Symbol('p_b5cb9c')
p_251638 = Symbol('p_251638')
p_f86d7f = Symbol('p_f86d7f')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(6.163759533339787)( qr[4] ))
circuit.append(Gates.ZGate( qr[6] ))
circuit.append(Gates.XGate( qr[6] ))
circuit.append(Gates.CRXGate(p_58380b)( qr[0], qr[6] ))
circuit.append(Gates.CRZGate(p_f86d7f)( qr[1], qr[6] ))
circuit.append(Gates.C3SXGate( qr[0], qr[7], qr[6], qr[3] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.RYYGate(p_b5cb9c)( qr[6], qr[7] ))
circuit.append(Gates.CRZGate(p_3f39bf)( qr[1], qr[7] ))
circuit.append(Gates.RZGate(p_aab82c)( qr[1] ))
circuit.append(Gates.SXGate( qr[0] ))
circuit.append(Gates.CU1Gate(p_4bf6d4)( qr[4], qr[0] ))
circuit.append(Gates.CRXGate(5.94477504571567)( qr[6], qr[4] ))
circuit.append(Gates.RZZGate(p_251638)( qr[7], qr[0] ))
circuit.append(Gates.CSXGate( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[6] ))
circuit.append(Gates.RZGate(3.775592041307464)( qr[4] ))
circuit.append(Gates.CRXGate(p_dc6a99)( qr[0], qr[3] ))
circuit.append(Gates.CUGate(p_457d2e, p_d9b3b7, p_2fe099, p_e66f86)( qr[6], qr[2] ))
circuit.append(Gates.U2Gate(2.5163050709890156, p_61e37c)( qr[2] ))
circuit.append(Gates.TGate( qr[6] ))
circuit.append(Gates.SdgGate( qr[0] ))
circuit.append(Gates.RZZGate(3.950837470808744)( qr[3], qr[4] ))
circuit.append(Gates.TGate( qr[5] ))
circuit.append(Gates.RYYGate(1.9669252191306448)( qr[4], qr[2] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))
circuit.append(cirq.measure(qr[7], key='cr7'))



circuit = cirq.resolve_parameters(circuit, {
    "p_aab82c": 4.229610589867865,
    "p_61e37c": 2.1276323672732023,
    "p_3f39bf": 4.167661441102218,
    "p_e66f86": 4.940217775579305,
    "p_d9b3b7": 5.0063780207098425,
    "p_58380b": 5.987304452123941,
    "p_4bf6d4": 3.2142159669963557,
    "p_457d2e": 5.03147076606842,
    "p_dc6a99": 0.7279391018916035,
    "p_2fe099": 3.1562533916051736,
    "p_b5cb9c": 1.740253089260498,
    "p_251638": 5.1829934776392745,
    "p_f86d7f": 1.0296448789776642
}, recursive=True)
        










simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=2771)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

