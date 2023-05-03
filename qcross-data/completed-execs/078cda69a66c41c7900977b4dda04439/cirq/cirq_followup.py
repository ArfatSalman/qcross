
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(4)]



circuit = cirq.Circuit()

circuit.append(Gates.YGate( qr[3] ))
circuit.append(Gates.CUGate(4.742596091504256, 5.602098424672528, 4.320385518485325, 3.3796506020234154)( qr[1], qr[2] ))
circuit.append(Gates.DCXGate( qr[1], qr[3] ))
circuit.append(Gates.CHGate( qr[3], qr[2] ))
circuit.append(Gates.CHGate( qr[1], qr[3] ))
circuit.append(Gates.CHGate( qr[0], qr[3] ))
circuit.append(Gates.YGate( qr[0] ))
circuit.append(Gates.CUGate(0.4698264522024645, 5.497223780656133, 0.6973970453004443, 4.135242097973106)( qr[2], qr[3] ))
circuit.append(Gates.DCXGate( qr[2], qr[0] ))
circuit.append(Gates.CZGate( qr[3], qr[2] ))
circuit.append(Gates.SGate( qr[2] ))
circuit.append(Gates.RZXGate(3.1312684847539773)( qr[3], qr[0] ))
circuit.append(Gates.SGate( qr[1] ))
circuit.append(Gates.CHGate( qr[0], qr[2] ))
circuit.append(Gates.iSwapGate( qr[2], qr[0] ))
circuit.append(Gates.RXGate(2.6717356275928497)( qr[0] ))
circuit.append(Gates.CZGate( qr[2], qr[0] ))
circuit.append(Gates.CHGate( qr[2], qr[1] ))
circuit.append(Gates.RYYGate(5.131718958124352)( qr[1], qr[3] ))
circuit.append(Gates.RYYGate(2.939587764936891)( qr[1], qr[3] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))









qasm_output = cirq.qasm(cirq.expand_composite(circuit))
circuit = circuit_from_qasm(qasm_output) # new circuit





simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=692)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['m_cr0_0', 'm_cr1_0', 'm_cr2_0', 'm_cr3_0'])
RESULT = counts

if __name__ == '__main__':
    import json
    print(json.dumps(RESULT, sort_keys=True))
