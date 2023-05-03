
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(7)]



circuit = cirq.Circuit()

circuit.append(Gates.RZGate(6.163759533339787)( qr[6] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(cirq.measure(qr[5], key='cr0'))
circuit.append(cirq.measure(qr[3], key='cr1'))
circuit.append(cirq.measure(qr[1], key='cr2'))
circuit.append(cirq.measure(qr[2], key='cr3'))
circuit.append(cirq.measure(qr[6], key='cr4'))
circuit.append(cirq.measure(qr[4], key='cr5'))
circuit.append(cirq.measure(qr[0], key='cr6'))













simulator = cirq.DensityMatrixSimulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=1959)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

