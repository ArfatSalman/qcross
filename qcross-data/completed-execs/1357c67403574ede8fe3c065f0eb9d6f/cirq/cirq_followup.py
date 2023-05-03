
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(10)]



circuit = cirq.Circuit()


subcircuit = cirq.Circuit()
subcircuit.append(Gates.RXGate(6.033961191253911)( qr[4] ))
subcircuit.append(Gates.UGate(5.01836135520768, 5.190931186022931, 1.2128092629174942)( qr[5] ))
subcircuit.append(Gates.DCXGate( qr[9], qr[6] ))
subcircuit.append(Gates.CUGate(4.229610589867865, 2.696266694818697, 5.631160518436971, 2.9151388486514547)( qr[0], qr[2] ))
subcircuit.append(Gates.ECRGate( qr[2], qr[0] ))
subcircuit.append(Gates.C3XGate(5.94477504571567)( qr[8], qr[5], qr[6], qr[2] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.RZGate(6.163759533339787)( qr[3] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[9], key='cr1'))
circuit.append(cirq.measure(qr[4], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[5], key='cr4'))
circuit.append(cirq.measure(qr[1], key='cr5'))
circuit.append(cirq.measure(qr[8], key='cr6'))
circuit.append(cirq.measure(qr[7], key='cr7'))
circuit.append(cirq.measure(qr[6], key='cr8'))
circuit.append(cirq.measure(qr[2], key='cr9'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=5542)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7', 'cr8', 'cr9'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

