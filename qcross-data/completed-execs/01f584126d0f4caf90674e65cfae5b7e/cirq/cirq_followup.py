
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(4)]



circuit = cirq.Circuit()

circuit.append(Gates.RZGate(6.163759533339787)( qr[3] ))
circuit.append(Gates.RZZGate(4.066449154047175)( qr[2], qr[0] ))
circuit.append(Gates.iSwapGate( qr[2], qr[0] ))
circuit.append(Gates.CSXGate( qr[3], qr[1] ))
circuit.append(Gates.XGate( qr[2] ))
circuit.append(Gates.CUGate(0.5112149185250571, 5.897054719225356, 2.3864521352475245, 5.987304452123941)( qr[1], qr[2] ))
circuit.append(Gates.CU1Gate(5.154187354656876)( qr[0], qr[1] ))
circuit.append(Gates.CHGate( qr[0], qr[2] ))
circuit.append(Gates.CHGate( qr[3], qr[2] ))
circuit.append(cirq.measure(qr[1], key='cr0'))
circuit.append(cirq.measure(qr[3], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[0], key='cr3'))









qasm_output = cirq.qasm(cirq.expand_composite(circuit))
circuit = circuit_from_qasm(qasm_output) # new circuit





simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=692)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['m_cr0_0', 'm_cr1_0', 'm_cr2_0', 'm_cr3_0'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

