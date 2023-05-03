
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(6)]



circuit = cirq.Circuit()

circuit.append(Gates.CSGate( qr[5], qr[0] ))
circuit.append(Gates.SXGate( qr[5] ))
circuit.append(Gates.CHGate( qr[1], qr[4] ))
circuit.append(Gates.RC3XGate( qr[5], qr[0], qr[4], qr[2] ))
circuit.append(Gates.RZGate(4.9678427199825475)( qr[2] ))

subcircuit = cirq.Circuit()
subcircuit.append(Gates.CSGate( qr[0], qr[2] ))
subcircuit.append(Gates.XGate( qr[1] ))
subcircuit.append(Gates.UGate(0.21975397537203006, 2.6790197391768045, 5.406299174556028)( qr[3] ))
circuit.append(subcircuit)
circuit.append(cirq.inverse(cirq.expand_composite(subcircuit)))

circuit.append(Gates.CXGate( qr[3], qr[1] ))
circuit.append(Gates.RC3XGate( qr[4], qr[2], qr[0], qr[5] ))
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
    from qcross.utils import display_results
    display_results( {"result": RESULT })

