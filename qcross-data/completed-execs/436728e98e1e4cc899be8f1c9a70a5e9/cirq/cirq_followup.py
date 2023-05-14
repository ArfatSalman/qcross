
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(8)]

p_f36ce2 = Symbol('p_f36ce2')
p_3c5b38 = Symbol('p_3c5b38')
p_2be356 = Symbol('p_2be356')
p_a02e63 = Symbol('p_a02e63')
p_230af2 = Symbol('p_230af2')
p_e694fd = Symbol('p_e694fd')
p_6036fe = Symbol('p_6036fe')
p_feb03e = Symbol('p_feb03e')
p_8056eb = Symbol('p_8056eb')
p_02880f = Symbol('p_02880f')
p_2ba9cb = Symbol('p_2ba9cb')
p_383aef = Symbol('p_383aef')
p_22cd76 = Symbol('p_22cd76')
p_13a733 = Symbol('p_13a733')
p_4c6189 = Symbol('p_4c6189')
p_4e6bd3 = Symbol('p_4e6bd3')
p_872d56 = Symbol('p_872d56')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_02880f)( qr[4] ))
circuit.append(Gates.ZGate( qr[6] ))
circuit.append(Gates.XGate( qr[6] ))
circuit.append(Gates.CRXGate(p_f36ce2)( qr[0], qr[6] ))
circuit.append(Gates.CRZGate(p_a02e63)( qr[1], qr[6] ))
circuit.append(Gates.C3SXGate( qr[0], qr[7], qr[6], qr[3] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.RYYGate(p_22cd76)( qr[6], qr[7] ))
circuit.append(Gates.CRZGate(p_6036fe)( qr[1], qr[7] ))
circuit.append(Gates.RZGate(p_3c5b38)( qr[1] ))
circuit.append(Gates.SXGate( qr[0] ))
circuit.append(Gates.CU1Gate(p_2ba9cb)( qr[4], qr[0] ))
circuit.append(Gates.CRXGate(p_13a733)( qr[6], qr[4] ))
circuit.append(Gates.RZZGate(p_383aef)( qr[7], qr[0] ))
circuit.append(Gates.CSXGate( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[6] ))
circuit.append(Gates.RZGate(p_4c6189)( qr[4] ))
circuit.append(Gates.CRXGate(p_feb03e)( qr[0], qr[3] ))
circuit.append(Gates.CUGate(p_872d56, p_2be356, 3.1562533916051736, p_8056eb)( qr[6], qr[2] ))
circuit.append(Gates.U2Gate(p_4e6bd3, p_e694fd)( qr[2] ))
circuit.append(Gates.TGate( qr[6] ))
circuit.append(Gates.SdgGate( qr[0] ))
circuit.append(Gates.RZZGate(p_230af2)( qr[3], qr[4] ))
circuit.append(Gates.TGate( qr[5] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))
circuit.append(cirq.measure(qr[7], key='cr7'))



circuit = cirq.resolve_parameters(circuit, {
    "p_f36ce2": 5.987304452123941,
    "p_3c5b38": 4.229610589867865,
    "p_2be356": 5.0063780207098425,
    "p_a02e63": 1.0296448789776642,
    "p_230af2": 3.950837470808744,
    "p_e694fd": 2.1276323672732023,
    "p_6036fe": 4.167661441102218,
    "p_feb03e": 0.7279391018916035,
    "p_8056eb": 4.940217775579305,
    "p_02880f": 6.163759533339787,
    "p_2ba9cb": 3.2142159669963557,
    "p_383aef": 5.1829934776392745,
    "p_22cd76": 1.740253089260498,
    "p_13a733": 5.94477504571567,
    "p_4c6189": 3.775592041307464,
    "p_4e6bd3": 2.5163050709890156,
    "p_872d56": 5.03147076606842
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

