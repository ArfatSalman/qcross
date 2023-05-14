
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(2)]



circuit = cirq.Circuit()

circuit.append(Gates.UGate(1.0932143214299395, 6.100531540039404, 4.859714896792146)( qr[1] ))
circuit.append(Gates.CYGate( qr[0], qr[1] ))
circuit.append(Gates.RXGate(4.335996068527454)( qr[0] ))
circuit.append(Gates.SGate( qr[1] ))
circuit.append(Gates.RXGate(6.070601620234646)( qr[0] ))
circuit.append(Gates.RZXGate(3.9660842997699097)( qr[0], qr[1] ))
circuit.append(Gates.HGate( qr[1] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))













simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=346)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })
