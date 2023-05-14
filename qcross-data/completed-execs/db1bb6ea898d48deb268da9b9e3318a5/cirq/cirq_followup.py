
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(8)]



circuit = cirq.Circuit()

circuit.append(Gates.RZGate(6.163759533339787)( qr[7] ))
circuit.append(Gates.ZGate( qr[3] ))
circuit.append(Gates.XGate( qr[3] ))
circuit.append(Gates.CRXGate(5.987304452123941)( qr[4], qr[3] ))
circuit.append(cirq.measure(qr[4], key='cr0'))
circuit.append(cirq.measure(qr[6], key='cr1'))
circuit.append(cirq.measure(qr[5], key='cr2'))
circuit.append(cirq.measure(qr[1], key='cr3'))
circuit.append(cirq.measure(qr[7], key='cr4'))
circuit.append(cirq.measure(qr[0], key='cr5'))
circuit.append(cirq.measure(qr[3], key='cr6'))
circuit.append(cirq.measure(qr[2], key='cr7'))









qasm_output = cirq.qasm(cirq.expand_composite(circuit))
circuit = circuit_from_qasm(qasm_output) # new circuit





simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=2771)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['m_cr0_0', 'm_cr1_0', 'm_cr2_0', 'm_cr3_0', 'm_cr4_0', 'm_cr5_0', 'm_cr6_0', 'm_cr7_0'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

