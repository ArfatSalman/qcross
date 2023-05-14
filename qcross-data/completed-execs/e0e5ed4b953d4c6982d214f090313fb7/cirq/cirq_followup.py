
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(9)]



circuit = cirq.Circuit()

circuit.append(Gates.RZGate(6.163759533339787)( qr[5] ))
circuit.append(Gates.CSXGate( qr[0], qr[4] ))
circuit.append(Gates.CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245, 5.987304452123941)( qr[7], qr[1] ))
circuit.append(Gates.SdgGate( qr[3] ))
circuit.append(Gates.C3SXGate( qr[7], qr[5], qr[2], qr[8] ))
circuit.append(Gates.ZGate( qr[0] ))
circuit.append(cirq.measure(qr[7], key='cr0'))
circuit.append(cirq.measure(qr[3], key='cr1'))
circuit.append(cirq.measure(qr[0], key='cr2'))
circuit.append(cirq.measure(qr[6], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[8], key='cr5'))
circuit.append(cirq.measure(qr[1], key='cr6'))
circuit.append(cirq.measure(qr[2], key='cr7'))
circuit.append(cirq.measure(qr[5], key='cr8'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=3919)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7', 'cr8'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })
