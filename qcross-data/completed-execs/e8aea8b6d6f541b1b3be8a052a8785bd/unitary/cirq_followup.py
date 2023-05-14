
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(6)]

p_830596 = Symbol('p_830596')
p_e2029e = Symbol('p_e2029e')
p_fa1a24 = Symbol('p_fa1a24')
p_a95f84 = Symbol('p_a95f84')
p_b2df8c = Symbol('p_b2df8c')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_fa1a24)( qr[4] ))
circuit.append(Gates.ZGate( qr[3] ))
circuit.append(Gates.CRZGate(4.2641612072511235)( qr[2], qr[4] ))
circuit.append(Gates.CUGate(p_a95f84, p_b2df8c, p_830596, p_e2029e)( qr[2], qr[3] ))
circuit.append(Gates.C3SXGate( qr[1], qr[4], qr[0], qr[2] ))
circuit.append(Gates.CCXGate( qr[1], qr[5], qr[0] ))
circuit.append(Gates.C3SXGate( qr[4], qr[3], qr[5], qr[0] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.CU3Gate(1.2827690425732097, 1.3283826543858017, 3.672121211148789)( qr[2], qr[5] ))
subcircuit.append(Gates.TGate( qr[1] ))
subcircuit.append(Gates.CUGate(4.229610589867865, 2.696266694818697, 5.631160518436971, 2.9151388486514547)( qr[0], qr[3] ))
subcircuit.append(Gates.TGate( qr[2] ))
subcircuit.append(Gates.RZXGate(4.563562108824195)( qr[4], qr[0] ))
subcircuit.append(Gates.C3XGate(5.94477504571567)( qr[4], qr[5], qr[2], qr[1] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.ZGate( qr[0] ))
circuit.append(Gates.ZGate( qr[2] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))



circuit = cirq.resolve_parameters(circuit, {
    "p_830596": 2.3864521352475245,
    "p_e2029e": 5.987304452123941,
    "p_fa1a24": 6.163759533339787,
    "p_a95f84": 0.5112149185250571,
    "p_b2df8c": 5.897054719225356
}, recursive=True)
        

UNITARY = cirq.unitary(circuit)








simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=1385)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

