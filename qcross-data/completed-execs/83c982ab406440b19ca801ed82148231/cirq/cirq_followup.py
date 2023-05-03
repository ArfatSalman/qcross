
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(6)]



circuit = cirq.Circuit()

circuit.append(Gates.CUGate(4.8953107059252625, 2.6758072220615388, 3.2748083473946528, 6.236176216437301)( qr[4], qr[3] ))
circuit.append(Gates.SdgGate( qr[4] ))
circuit.append(Gates.RC3XGate( qr[4], qr[2], qr[1], qr[3] ))
circuit.append(Gates.CUGate(3.8548770506419117, 4.254344154816252, 1.4586583527810086, 0.6558022908747309)( qr[1], qr[4] ))
circuit.append(Gates.U2Gate(4.508908477229367, 4.339644176014044)( qr[5] ))
circuit.append(Gates.C4XGate( qr[5], qr[2], qr[4], qr[1], qr[0] ))
circuit.append(Gates.CUGate(2.0612495225167686, 0.9108049053481971, 1.7408688031064241, 2.2294210493888307)( qr[2], qr[4] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))









qasm_output = cirq.qasm(cirq.expand_composite(circuit))
circuit = circuit_from_qasm(qasm_output) # new circuit





simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=1385)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['m_cr0_0', 'm_cr1_0', 'm_cr2_0', 'm_cr3_0', 'm_cr4_0', 'm_cr5_0'])
RESULT = counts

if __name__ == '__main__':
    import json
    print(json.dumps(RESULT, sort_keys=True))
