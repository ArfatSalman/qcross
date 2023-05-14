
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(8)]

p_023a7d = Symbol('p_023a7d')
p_21ba07 = Symbol('p_21ba07')
p_4a69b2 = Symbol('p_4a69b2')
p_b96fd4 = Symbol('p_b96fd4')
p_1c6cdf = Symbol('p_1c6cdf')
p_7d7c65 = Symbol('p_7d7c65')
p_66e932 = Symbol('p_66e932')
p_8b6baf = Symbol('p_8b6baf')
p_9ec620 = Symbol('p_9ec620')
p_628297 = Symbol('p_628297')
p_4c04c2 = Symbol('p_4c04c2')
p_f3b666 = Symbol('p_f3b666')
p_edb705 = Symbol('p_edb705')
p_1a21da = Symbol('p_1a21da')
p_52c99c = Symbol('p_52c99c')
p_7fc368 = Symbol('p_7fc368')
p_ad4dbb = Symbol('p_ad4dbb')
p_d7b9ee = Symbol('p_d7b9ee')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_7fc368)( qr[4] ))
circuit.append(Gates.ZGate( qr[6] ))
circuit.append(Gates.XGate( qr[6] ))
circuit.append(Gates.CRXGate(p_1a21da)( qr[0], qr[6] ))
circuit.append(Gates.CRZGate(p_52c99c)( qr[1], qr[6] ))
circuit.append(Gates.C3SXGate( qr[0], qr[7], qr[6], qr[3] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.RYYGate(p_d7b9ee)( qr[6], qr[7] ))
circuit.append(Gates.CRZGate(4.167661441102218)( qr[1], qr[7] ))
circuit.append(Gates.RZGate(p_1c6cdf)( qr[1] ))
circuit.append(Gates.SXGate( qr[0] ))
circuit.append(Gates.CU1Gate(p_7d7c65)( qr[4], qr[0] ))
circuit.append(Gates.CRXGate(p_4a69b2)( qr[6], qr[4] ))
circuit.append(Gates.RZZGate(p_f3b666)( qr[7], qr[0] ))
circuit.append(Gates.CSXGate( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[6] ))
circuit.append(Gates.RZGate(p_66e932)( qr[4] ))
circuit.append(Gates.CRXGate(p_edb705)( qr[0], qr[3] ))
circuit.append(Gates.CUGate(p_21ba07, p_628297, p_8b6baf, p_023a7d)( qr[6], qr[2] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.CU3Gate(5.583322729510212, 4.773422973876057, 0.8960434543694032)( qr[4], qr[3] ))
subcircuit.append(Gates.RCCXGate( qr[1], qr[6], qr[7] ))
subcircuit.append(Gates.RXGate(1.723121374211541)( qr[1] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.U2Gate(p_b96fd4, p_ad4dbb)( qr[2] ))
circuit.append(Gates.TGate( qr[6] ))
circuit.append(Gates.SdgGate( qr[0] ))
circuit.append(Gates.RZZGate(p_9ec620)( qr[3], qr[4] ))
circuit.append(Gates.TGate( qr[5] ))
circuit.append(Gates.RYYGate(p_4c04c2)( qr[4], qr[2] ))
circuit.append(Gates.C3SXGate( qr[1], qr[3], qr[2], qr[5] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))
circuit.append(cirq.measure(qr[7], key='cr7'))



circuit = cirq.resolve_parameters(circuit, {
    "p_023a7d": 4.940217775579305,
    "p_21ba07": 5.03147076606842,
    "p_4a69b2": 5.94477504571567,
    "p_b96fd4": 2.5163050709890156,
    "p_1c6cdf": 4.229610589867865,
    "p_7d7c65": 3.2142159669963557,
    "p_66e932": 3.775592041307464,
    "p_8b6baf": 3.1562533916051736,
    "p_9ec620": 3.950837470808744,
    "p_628297": 5.0063780207098425,
    "p_4c04c2": 1.9669252191306448,
    "p_f3b666": 5.1829934776392745,
    "p_edb705": 0.7279391018916035,
    "p_1a21da": 5.987304452123941,
    "p_52c99c": 1.0296448789776642,
    "p_7fc368": 6.163759533339787,
    "p_ad4dbb": 2.1276323672732023,
    "p_d7b9ee": 1.740253089260498
}, recursive=True)
        






qasm_output = cirq.qasm(cirq.expand_composite(circuit))
circuit = circuit_from_qasm(qasm_output) # new circuit





simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=2771)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['m_cr0_0', 'm_cr1_0', 'm_cr2_0', 'm_cr3_0', 'm_cr4_0', 'm_cr5_0', 'm_cr6_0', 'm_cr7_0'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

