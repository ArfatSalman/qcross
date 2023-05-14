
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(6)]

p_1ee909 = Symbol('p_1ee909')
p_8f01e6 = Symbol('p_8f01e6')
p_c6f972 = Symbol('p_c6f972')
p_924711 = Symbol('p_924711')
p_58a2b5 = Symbol('p_58a2b5')
p_4927d2 = Symbol('p_4927d2')
p_cc3cec = Symbol('p_cc3cec')
p_8e5127 = Symbol('p_8e5127')
p_4616e5 = Symbol('p_4616e5')
p_cc7cb0 = Symbol('p_cc7cb0')
p_1adccb = Symbol('p_1adccb')
p_683702 = Symbol('p_683702')
p_ba4e5e = Symbol('p_ba4e5e')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_1ee909)( qr[3] ))
circuit.append(Gates.ZGate( qr[4] ))
circuit.append(Gates.CRZGate(p_1adccb)( qr[5], qr[3] ))
circuit.append(Gates.CUGate(p_4616e5, p_924711, p_c6f972, p_ba4e5e)( qr[5], qr[4] ))
circuit.append(Gates.C3SXGate( qr[1], qr[3], qr[0], qr[5] ))
circuit.append(Gates.CCXGate( qr[1], qr[2], qr[0] ))
circuit.append(Gates.C3SXGate( qr[3], qr[4], qr[2], qr[0] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.ZGate( qr[5] ))
circuit.append(Gates.TGate( qr[3] ))
circuit.append(Gates.RCCXGate( qr[2], qr[4], qr[3] ))
circuit.append(Gates.SGate( qr[2] ))
circuit.append(Gates.CRZGate(p_8e5127)( qr[1], qr[2] ))
circuit.append(Gates.RZGate(p_cc3cec)( qr[1] ))
circuit.append(Gates.C3SXGate( qr[0], qr[5], qr[1], qr[4] ))
circuit.append(Gates.CU1Gate(p_cc7cb0)( qr[4], qr[0] ))
circuit.append(Gates.UGate(p_8f01e6, p_4927d2, p_683702)( qr[2] ))
circuit.append(Gates.RZZGate(p_58a2b5)( qr[0], qr[2] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[5], key='cr2'))
circuit.append(cirq.measure(qr[4], key='cr3'))
circuit.append(cirq.measure(qr[3], key='cr4'))
circuit.append(cirq.measure(qr[2], key='cr5'))



circuit = cirq.resolve_parameters(circuit, {
    "p_1ee909": 6.163759533339787,
    "p_8f01e6": 5.887184334931191,
    "p_c6f972": 2.3864521352475245,
    "p_924711": 5.897054719225356,
    "p_58a2b5": 5.1829934776392745,
    "p_4927d2": 0.07157463504881167,
    "p_cc3cec": 4.229610589867865,
    "p_8e5127": 4.167661441102218,
    "p_4616e5": 0.5112149185250571,
    "p_cc7cb0": 3.2142159669963557,
    "p_1adccb": 4.2641612072511235,
    "p_683702": 1.4112277317699358,
    "p_ba4e5e": 5.987304452123941
}, recursive=True)
        






qasm_output = cirq.qasm(cirq.expand_composite(circuit))
circuit = circuit_from_qasm(qasm_output) # new circuit





simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=1385)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['m_cr0_0', 'm_cr1_0', 'm_cr2_0', 'm_cr3_0', 'm_cr4_0', 'm_cr5_0'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

