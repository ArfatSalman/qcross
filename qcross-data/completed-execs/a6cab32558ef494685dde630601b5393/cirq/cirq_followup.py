
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(9)]

p_af69ea = Symbol('p_af69ea')
p_66b890 = Symbol('p_66b890')
p_8a1de7 = Symbol('p_8a1de7')

circuit = cirq.Circuit()

circuit.append(Gates.RZGate(p_66b890)( qr[8] ))
circuit.append(Gates.CSXGate( qr[2], qr[4] ))
circuit.append(Gates.CUGate(p_8a1de7, 5.897054719225356, p_af69ea, 5.987304452123941)( qr[0], qr[6] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))
circuit.append(cirq.measure(qr[7], key='cr7'))
circuit.append(cirq.measure(qr[8], key='cr8'))



circuit = cirq.resolve_parameters(circuit, {
    "p_af69ea": 2.3864521352475245,
    "p_66b890": 6.163759533339787,
    "p_8a1de7": 0.5112149185250571
}, recursive=True)
        










simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=3919)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['cr0', 'cr1', 'cr2', 'cr3', 'cr4', 'cr5', 'cr6', 'cr7', 'cr8'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

