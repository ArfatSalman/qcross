
import cirq

from bloqs.ext.cirq import Gates
from bloqs.ext.cirq.utils import get_qiskit_like_output
from sympy import Symbol
from cirq.contrib.qasm_import import circuit_from_qasm
import numpy as np


qr = [cirq.NamedQubit('q' + str(i)) for i in range(7)]



circuit = cirq.Circuit()

circuit.append(Gates.RVGate(5.730485179497036, 5.1815317617582535, 4.954506343035782)( qr[0] ))
circuit.append(Gates.U1Gate(5.5351729304729)( qr[6] ))
circuit.append(Gates.IGate( qr[1] ))
circuit.append(Gates.RXXGate(1.620673138384231)( qr[1], qr[4] ))
circuit.append(Gates.SwapGate( qr[0], qr[3] ))
circuit.append(Gates.CUGate(2.5179284740661867, 4.218025714484969, 5.538801185807778, 0.2277932967359332)( qr[4], qr[5] ))
circuit.append(Gates.SXGate( qr[3] ))
circuit.append(Gates.SXGate( qr[0] ))
circuit.append(Gates.CHGate( qr[0], qr[2] ))
circuit.append(Gates.RGate(2.373112537407949, 2.0806292204834302)( qr[1] ))
circuit.append(Gates.CCZGate( qr[4], qr[1], qr[5] ))
circuit.append(Gates.YGate( qr[4] ))
circuit.append(Gates.RGate(1.3139288690051985, 5.834685188574328)( qr[6] ))
circuit.append(Gates.CCZGate( qr[2], qr[5], qr[1] ))
circuit.append(Gates.XGate( qr[0] ))
circuit.append(Gates.U1Gate(0.5163920678872455)( qr[5] ))
circuit.append(Gates.SGate( qr[2] ))
circuit.append(Gates.CCXGate( qr[4], qr[0], qr[5] ))
circuit.append(cirq.measure(qr[0], key='cr0'))
circuit.append(cirq.measure(qr[1], key='cr1'))
circuit.append(cirq.measure(qr[2], key='cr2'))
circuit.append(cirq.measure(qr[3], key='cr3'))
circuit.append(cirq.measure(qr[4], key='cr4'))
circuit.append(cirq.measure(qr[5], key='cr5'))
circuit.append(cirq.measure(qr[6], key='cr6'))









qasm_output = cirq.qasm(cirq.expand_composite(circuit))
circuit = circuit_from_qasm(qasm_output) # new circuit





simulator = cirq.Simulator(seed=np.random.RandomState())


result = simulator.run(circuit, repetitions=1959)
# result_dict = dict(result.multi_measurement_histogram()
# keys = list(map(lambda arr: reduce(lambda x, y: str(x) + str(y), arr[::-1]), result_dict.keys()))
counts = get_qiskit_like_output(result, keys=['m_cr0_0', 'm_cr1_0', 'm_cr2_0', 'm_cr3_0', 'm_cr4_0', 'm_cr5_0', 'm_cr6_0'])

RESULT = counts


if __name__ == '__main__':
    from qcross.utils import display_results
    display_results( {"result": RESULT })

