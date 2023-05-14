
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(5)]

p_4b58f7 = Symbol('p_4b58f7')
p_b10c48 = Symbol('p_b10c48')
p_da461d = Symbol('p_da461d')
p_a1b5f5 = Symbol('p_a1b5f5')
p_69e8c5 = Symbol('p_69e8c5')
p_eb8e6b = Symbol('p_eb8e6b')
p_7fdc7e = Symbol('p_7fdc7e')
p_c0b116 = Symbol('p_c0b116')
p_669459 = Symbol('p_669459')
p_c6c4c2 = Symbol('p_c6c4c2')
p_eb23fe = Symbol('p_eb23fe')
p_33d287 = Symbol('p_33d287')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(6.163759533339787)( qr[3] ))
circuit.append(Gates.SXdgGate( qr[2] ))
circuit.append(Gates.CSXGate( qr[1], qr[0] ))
circuit.append(Gates.ECRGate( qr[3], qr[2] ))
circuit.append(Gates.CRXGate(p_eb8e6b)( qr[4], qr[3] ))
circuit.append(Gates.SGate( qr[0] ))
circuit.append(Gates.CRZGate(p_c6c4c2)( qr[3], qr[4] ))
circuit.append(Gates.CHGate( qr[1], qr[4] ))
circuit.append(Gates.RYYGate(1.6723037552953224)( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.TGate( qr[4] ))
circuit.append(Gates.CSXGate( qr[1], qr[4] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(Gates.SGate( qr[4] ))
circuit.append(Gates.CUGate(p_c0b116, p_eb23fe, p_a1b5f5, p_669459)( qr[1], qr[4] ))
circuit.append(Gates.RZGate(p_da461d)( qr[1] ))
circuit.append(Gates.RYYGate(p_7fdc7e)( qr[0], qr[2] ))
circuit.append(Gates.CU1Gate(p_33d287)( qr[3], qr[0] ))
circuit.append(Gates.UGate(p_69e8c5, p_4b58f7, p_b10c48)( qr[4] ))
circuit.append(Gates.CHGate( qr[2], qr[0] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.SGate( qr[2] ))
circuit.append(Gates.CSXGate( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[3] ))
circuit.append(Gates.CHGate( qr[0], qr[4] ))
circuit.append(Gates.CHGate( qr[0], qr[1] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))



circuit = cirq.resolve_parameters(circuit, {
    "p_4b58f7": 0.07157463504881167,
    "p_b10c48": 1.4112277317699358,
    "p_da461d": 4.229610589867865,
    "p_a1b5f5": 4.623446645668956,
    "p_69e8c5": 5.887184334931191,
    "p_eb8e6b": 2.0099472182748075,
    "p_7fdc7e": 5.398622178940033,
    "p_c0b116": 5.708725119517347,
    "p_669459": 3.865496458458116,
    "p_c6c4c2": 1.0296448789776642,
    "p_eb23fe": 4.167661441102218,
    "p_33d287": 3.2142159669963557
}, recursive=True)
        










simulator = cirq.DensityMatrixSimulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=979)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

