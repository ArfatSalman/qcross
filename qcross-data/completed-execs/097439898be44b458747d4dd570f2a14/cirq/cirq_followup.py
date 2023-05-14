
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(8)]

p_38d9cb = Symbol('p_38d9cb')
p_6fbfe4 = Symbol('p_6fbfe4')
p_6b711e = Symbol('p_6b711e')
p_bb0c9a = Symbol('p_bb0c9a')
p_afbfa9 = Symbol('p_afbfa9')
p_985fe0 = Symbol('p_985fe0')
p_f413fb = Symbol('p_f413fb')
p_dc4e0f = Symbol('p_dc4e0f')
p_7ac4d4 = Symbol('p_7ac4d4')
p_559ba5 = Symbol('p_559ba5')
p_6b4cf2 = Symbol('p_6b4cf2')
p_30bc99 = Symbol('p_30bc99')
p_3e628e = Symbol('p_3e628e')
p_e762e6 = Symbol('p_e762e6')
p_f754b8 = Symbol('p_f754b8')
p_a9c7f4 = Symbol('p_a9c7f4')
p_01c9cb = Symbol('p_01c9cb')
p_ae29cc = Symbol('p_ae29cc')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_559ba5)( qr[4] ))
circuit.append(Gates.ZGate( qr[6] ))
circuit.append(Gates.XGate( qr[6] ))
circuit.append(Gates.CRXGate(p_38d9cb)( qr[0], qr[6] ))
circuit.append(Gates.CRZGate(p_bb0c9a)( qr[1], qr[6] ))
circuit.append(Gates.C3SXGate( qr[0], qr[7], qr[6], qr[3] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(Gates.XGate( qr[1] ))
circuit.append(Gates.RYYGate(p_3e628e)( qr[6], qr[7] ))
circuit.append(Gates.CRZGate(p_f413fb)( qr[1], qr[7] ))
circuit.append(Gates.RZGate(p_6fbfe4)( qr[1] ))
circuit.append(Gates.SXGate( qr[0] ))
circuit.append(Gates.CU1Gate(p_6b4cf2)( qr[4], qr[0] ))
circuit.append(Gates.CRXGate(p_e762e6)( qr[6], qr[4] ))
circuit.append(Gates.RZZGate(p_30bc99)( qr[7], qr[0] ))
circuit.append(Gates.CSXGate( qr[0], qr[2] ))
circuit.append(Gates.ZGate( qr[6] ))
circuit.append(Gates.RZGate(p_f754b8)( qr[4] ))
circuit.append(Gates.CRXGate(p_dc4e0f)( qr[0], qr[3] ))
circuit.append(Gates.CUGate(p_01c9cb, p_6b711e, p_ae29cc, p_7ac4d4)( qr[6], qr[2] ))
circuit.append(Gates.U2Gate(p_a9c7f4, p_985fe0)( qr[2] ))
circuit.append(Gates.TGate( qr[6] ))
circuit.append(Gates.SdgGate( qr[0] ))
circuit.append(Gates.RZZGate(p_afbfa9)( qr[3], qr[4] ))
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
    "p_38d9cb": 5.987304452123941,
    "p_6fbfe4": 4.229610589867865,
    "p_6b711e": 5.0063780207098425,
    "p_bb0c9a": 1.0296448789776642,
    "p_afbfa9": 3.950837470808744,
    "p_985fe0": 2.1276323672732023,
    "p_f413fb": 4.167661441102218,
    "p_dc4e0f": 0.7279391018916035,
    "p_7ac4d4": 4.940217775579305,
    "p_559ba5": 6.163759533339787,
    "p_6b4cf2": 3.2142159669963557,
    "p_30bc99": 5.1829934776392745,
    "p_3e628e": 1.740253089260498,
    "p_e762e6": 5.94477504571567,
    "p_f754b8": 3.775592041307464,
    "p_a9c7f4": 2.5163050709890156,
    "p_01c9cb": 5.03147076606842,
    "p_ae29cc": 3.1562533916051736
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

