
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(9)]



circuit = cirq.Circuit()

circuit.append(cirq.measure(qr[2], key='cr0'))
circuit.append(cirq.measure(qr[4], key='cr1'))
circuit.append(cirq.measure(qr[3], key='cr2'))
circuit.append(cirq.measure(qr[8], key='cr3'))
circuit.append(cirq.measure(qr[1], key='cr4'))
circuit.append(cirq.measure(qr[7], key='cr5'))
circuit.append(cirq.measure(qr[5], key='cr6'))
circuit.append(cirq.measure(qr[0], key='cr7'))
circuit.append(cirq.measure(qr[6], key='cr8'))













simulator = cirq.DensityMatrixSimulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=3919)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7', 'cr8'])
RESULT = counts

if __name__ == '__main__':
    import json
    print(json.dumps(RESULT, sort_keys=True))
